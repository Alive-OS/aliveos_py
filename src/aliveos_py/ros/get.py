# *************************************************************************
#
# Copyright (c) 2021 Andrei Gramakov. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# site:    https://agramakov.me
# e-mail:  mail@agramakov.me
#
# *************************************************************************

from rospy import Service, ServiceProxy, Publisher, Subscriber, wait_for_service
from rospy import logerr, logdebug, loginfo, ROSException, get_param
from rospy.client import _unspecified
from time import time, sleep
from typing import Any, Callable


def server(name: str, service, handler: Callable) -> Service:
    logdebug("Service \'%s\' is loading..." % name)
    s = Service(name, service, handler)
    logdebug("Service \'%s\' is ready" % name)
    return s


def client(srv_name: str, service, timeout: float = 5) -> ServiceProxy:
    """
    If timeout < 0 will return None
    """
    logdebug("Client \'%s\' is loading..." % srv_name)
    if timeout < 0:
        return None
    if timeout > 0:
        try:
            loginfo(f"Waiting for the service {srv_name} ({timeout} sec)")
            wait_for_service(srv_name, timeout)
            loginfo(f"Service {srv_name} online")
        except ROSException:
            logerr(f"Service {srv_name} is offline!")
    c = ServiceProxy(srv_name, service)
    logdebug("Client \'%s\' is ready" % srv_name)
    return c


def publisher(topic_name: str, data_class) -> Publisher:
    logdebug("Publisher \'%s\' is loading..." % topic_name)
    p = Publisher(topic_name, data_class, queue_size=10)
    logdebug("Publisher \'%s\' is ready" % topic_name)
    return p


def subscriber(topic_name: str, data_class, callback: Callable, callback_args=None) -> Subscriber:
    logdebug("Subscriber \'%s\' is loading..." % topic_name)
    s = Subscriber(topic_name, data_class, callback, callback_args)
    logdebug("Subscriber \'%s\' is ready" % topic_name)
    return s


def param(name: str, default: Any = _unspecified, timeout_s: int = 0) -> Any:
    """
    Parameters
    ----------
    name : str
    default : Any
    timeout_s : int
        timeout_s > 0  - try to read the parameter during the timeout
        timeout_s == 0 - try to read the parameter one time without a timeout
        timeout < 0 - try to read the parameter until success
    """
    if timeout_s > 0:
        start = time()
        while ((time() - start) < timeout_s):
            try:
                return get_param(name, default)
            except (ROSException, KeyError):
                sleep(.1)
    elif timeout_s < 0:
        while 1:
            try:
                return get_param(name, default)
            except (ROSException, KeyError):
                sleep(.1)
    else:
        return get_param(name, default)
