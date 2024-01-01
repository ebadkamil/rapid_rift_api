import tempfile
from pathlib import Path

import pytest
import yaml


@pytest.fixture
def temp_authentication_file():
    temp_file = tempfile.NamedTemporaryFile(mode="w", delete=False)
    auth_data = {
        "user": "test_user",
        "password": "test_pass",
        "host": "test_host",
        "port": "test_port",
        "service": "test_service",
        "encoding": "test_encoding",
    }
    yaml.dump(auth_data, temp_file)
    temp_file.close()

    yield Path(temp_file.name)
    Path(temp_file.name).unlink()
