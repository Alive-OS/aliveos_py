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

from rospy import get_param, Publisher
from aliveos_msgs import msg
from .get import publisher


def perception_concept() -> Publisher:
    return publisher(topic_name=get_param("TOPIC_PC"), data_class=msg.PerceptionConcept)


def ego_commands() -> Publisher:
    return publisher(topic_name=get_param("TOPIC_EGOCMD"), data_class=msg.EgoCommands)


def device_cmd() -> Publisher:
    return publisher(topic_name=get_param("TOPIC_DEV_CMD"), data_class=msg.DeviceCmd)


def device_data() -> Publisher:
    return publisher(topic_name=get_param("TOPIC_DEV_DATA"), data_class=msg.DeviceData)


def emotion_params() -> Publisher:
    return publisher(topic_name=get_param("TOPIC_EPARAM"), data_class=msg.EmotionParams)
