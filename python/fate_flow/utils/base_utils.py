#
#  Copyright 2019 The FATE Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
import os
import uuid
from fate_arch.common.base_utils import json_dumps

FATE_BASE = os.getenv("FATE_FLOW_BASE")


def get_fate_flow_directory(*args):
    global FATE_BASE
    if FATE_BASE is None:
        FATE_BASE = os.path.abspath(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                os.pardir,
                os.pardir,
                os.pardir,
            )
        )
    if args:
        return os.path.join(FATE_BASE, *args)
    return FATE_BASE


def get_fate_flow_python_directory(*args):
    return get_fate_flow_directory("python", *args)

def new_unique_id():
    #todo: may be using snowflake?
    return uuid.uuid1().hex


def jprint(src: dict, indent: int = 4):
    print(json_dumps(src, indent=indent))