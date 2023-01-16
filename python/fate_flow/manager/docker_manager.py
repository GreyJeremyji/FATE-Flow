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
import docker

from fate_flow.settings import WORKER


class DockerManager:
    config = WORKER.get('docker', {}).get('config', {})
    image = WORKER.get('docker', {}).get('image', '')

    def __init__(self):
        self.client = docker.DockerClient(**self.config)

    def start(self, name, command, environment, volumes):
        self.client.containers.run(
            self.image, command,
            auto_remove=True, detach=True, environment=environment,
            name=name, volumes=volumes,
        )

    def stop(self, name):
        try:
            container = self.client.containers.get(name)
        except docker.errors.NotFound:
            return
        container.remove(force=True)

    def is_running(self, name):
        try:
            container = self.client.containers.get(name)
        except docker.errors.NotFound:
            return False
        return container.status == 'running'
