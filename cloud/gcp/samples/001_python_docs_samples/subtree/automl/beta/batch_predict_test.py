# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific ladnguage governing permissions and
# limitations under the License.

import datetime
import os

from google.api_core.retry import Retry

import batch_predict

PROJECT_ID = os.environ["AUTOML_PROJECT_ID"]
BUCKET_ID = f"{PROJECT_ID}-lcm"
MODEL_ID = "TEN0000000000000000000"
PREFIX = "TEST_EXPORT_OUTPUT_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")


@Retry()
def test_batch_predict(capsys):
    # As batch prediction can take a long time. Try to batch predict on a model
    # and confirm that the model was not found, but other elements of the
    # request were valid.
    try:
        input_uri = f"gs://{BUCKET_ID}/entity-extraction/input.jsonl"
        output_uri = f"gs://{BUCKET_ID}/{PREFIX}/"
        batch_predict.batch_predict(PROJECT_ID, MODEL_ID, input_uri, output_uri)
        out, _ = capsys.readouterr()
        assert "does not exist" in out
    except Exception as e:
        assert "does not exist" in e.message
