from unittest.mock import MagicMock, PropertyMock, patch

import pytest

from src.connectors.constants import DbTypes
from src.connectors.engine_factory import BaseEngine, EngineFactory, OracleEngine


def test_base_engine_initialization(temp_authentication_file):
    base_engine = BaseEngine(authentication=temp_authentication_file)

    assert "user" in base_engine.config
    assert "password" in base_engine.config
    assert "host" in base_engine.config
    assert "port" in base_engine.config
    assert "service" in base_engine.config
    assert "encoding" in base_engine.config


def test_oracle_engine_raises_value_error_for_invalid_config(
    invalid_authentication_file,
):
    with pytest.raises(
        ValueError, match="Missing or invalid configurations"
    ) as exc_info:
        OracleEngine(authentication=invalid_authentication_file)


@patch("sqlmodel.create_engine")
def test_oracle_engine_get_engine(mock_sql_create_engine, temp_authentication_file):
    oracle_engine = OracleEngine(authentication=temp_authentication_file)
    oracle_engine.get_engine()
    mock_sql_create_engine.assert_called_once_with(
        f"oracle+cx_oracle://test_user:test_pass@test_host:test_port/?service_name=test_service&test_encoding"
    )


def test_engine_factory_returns_not_implemented_error_for_unknown_db_type():
    with pytest.raises(
        NotImplementedError, match="DbTypes.UNKNOWN not implemented"
    ) as exc_info:
        EngineFactory.from_database_type(DbTypes.UNKNOWN)


def test_engine_factory_returns_oracle_engine():
    klass = EngineFactory.from_database_type(DbTypes.ORACLE)
    assert klass == OracleEngine
