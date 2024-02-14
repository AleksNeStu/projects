# Copyright 2021 Google LLC
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
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import os
import uuid

import pytest

from snippets.cloud_sql_connection_pool import (
    init_db,
    init_tcp_connection_engine,
)


@pytest.fixture(name="conn_vars")
def setup() -> dict[str, str]:
    try:
        conn_vars = {}
        conn_vars["db_user"] = os.environ["SQLSERVER_USER"]
        conn_vars["db_pass"] = os.environ["SQLSERVER_PASSWORD"]
        conn_vars["db_name"] = os.environ["SQLSERVER_DATABASE"]
        conn_vars["db_host"] = os.environ["SQLSERVER_HOST"]
        conn_vars["instance_conn_name"] = os.environ["SQLSERVER_INSTANCE"]
        conn_vars["db_socket_dir"] = os.getenv("DB_SOCKET_DIR", "/cloudsql")
    except KeyError:
        raise Exception(
            "The following env variables must be set to run these tests:"
            "SQLSERVER_USER, SQLSERVER_PASSWORD, SQLSERVER_DATABASE, SQLSERVER_HOST, "
            "SQLSERVER_INSTANCE"
        )
    else:
        yield conn_vars


def test_init_tcp_connection_engine(
    capsys: pytest.CaptureFixture, conn_vars: dict[str, str]
) -> None:
    init_tcp_connection_engine(
        db_user=conn_vars["db_user"],
        db_name=conn_vars["db_name"],
        db_pass=conn_vars["db_pass"],
        db_host=conn_vars["db_host"],
    )

    captured = capsys.readouterr().out
    assert "Created TCP connection pool" in captured


def test_init_db(capsys: pytest.CaptureFixture, conn_vars: dict[str, str]) -> None:
    table_name = f"votes_{uuid.uuid4().hex}"

    init_db(
        db_user=conn_vars["db_user"],
        db_name=conn_vars["db_name"],
        db_pass=conn_vars["db_pass"],
        db_host=conn_vars["db_host"],
        table_name=table_name,
    )

    captured = capsys.readouterr().out
    assert f"Created table {table_name} in db {conn_vars['db_name']}" in captured
