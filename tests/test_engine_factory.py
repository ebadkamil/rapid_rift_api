from unittest.mock import patch

import pytest

from src.app.db.constants import DbTypes
from src.app.db.engine_factory import BaseEngine, EngineFactory, OracleEngine


# TODO: Fix tests later
@pytest.mark.skip(reason="Find better way of testing")
def test_base_engine_initialization(valid_oracle_env_variable):
    base_engine = BaseEngine()

    assert "ORACLE_SERVER" in base_engine.config
    assert "ORACLE_PORT" in base_engine.config
    assert "ORACLE_USER" in base_engine.config
    assert "ORACLE_PASSWORD" in base_engine.config
    assert "ORACLE_SERVICE" in base_engine.config
    assert "ORACLE_ENCODING" in base_engine.config


@pytest.mark.skip(reason="Find better way of testing")
@patch("sqlmodel.create_engine")
def test_oracle_engine_get_engine(mock_sql_create_engine, valid_oracle_env_variable):
    oracle_engine = OracleEngine()
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
