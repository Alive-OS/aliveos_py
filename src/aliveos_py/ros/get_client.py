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

from rospy import get_param, ServiceProxy
from aliveos_msgs import srv
from .get import client


def command_concept() -> ServiceProxy:
    return client(srv_name=get_param("SRV_C2C_CMDC"), service=srv.CommandConcept)


def command_concept_descriptor() -> ServiceProxy:
    return client(srv_name=get_param("SRV_C2C_CMDDSC"), service=srv.CommandConceptDescriptor)


def emotion_core_write() -> ServiceProxy:
    return client(srv_name=get_param("SRV_ECORE_W"), service=srv.EmotionCoreWrite)


def emotion_code_data_descriptor() -> ServiceProxy:
    return client(srv_name=get_param("SRV_ECORE_DDSC"), service=srv.EmotionCoreDataDescriptor)


def hw(server_name) -> ServiceProxy:
    return client(srv_name=server_name, service=srv.Hw)
