import pytest

from src.connectors.connection import Connector
from src.connectors.constants import DbTypes


def test_connector_returns_correct_engine_for_db_type():
    assert True


def test_connector_returns_not_implemented_error_for_unknown_db_type():
    with pytest.raises(NotImplementedError) as exc_info:
        Connector(DbTypes.UNKNOWN, "/PATH/TO/AUTHENTICATION")

    assert str(exc_info.value) == "Engine type DbTypes.UNKNOWN not implemented"
