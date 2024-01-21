import os

import pytest


@pytest.fixture
def valid_oracle_env_variable():
    env_variables = {
        "ORACLE_SERVER": "test_host",
        "ORACLE_PORT": "test_port",
        "ORACLE_USER": "test_user",
        "ORACLE_PASSWORD": "test_pass",
        "ORACLE_SERVICE": "test_service",
        "ORACLE_ENCODING": "test_encoding",
    }

    for key, value in env_variables.items():
        os.environ[key] = value

    yield
    for env_var in env_variables:
        del os.environ[env_var]
