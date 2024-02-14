# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64

import pytest

import main


def test_functions_pubsub_subscribe_should_print_message(
    capsys: pytest.CaptureFixture,
) -> None:
    event = type("cloudevent", (object,), {"attributes": {}, "data": {}})

    event.data = {
        "message": {
            "data": base64.b64encode(b"world"),
        }
    }

    main.subscribe(event)

    out, _ = capsys.readouterr()
    assert "Hello, world!" in out
