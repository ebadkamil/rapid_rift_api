from datetime import datetime, timedelta, timezone
from unittest.mock import patch

from jose import jwt

from src.app.core.config import settings
from src.app.utils import create_access_token


@patch("src.app.utils.datetime")
def test_create_access_token_has_no_expiry(mock_datetime):
    random_datetime = datetime(2024, 12, 1, 0, 0, 0, tzinfo=timezone.utc)
    mock_datetime.utcnow.return_value = random_datetime
    data_to_token = "FAKE_USERNAME"
    token = create_access_token(data_to_token)
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    assert payload["sub"] == data_to_token

    expected_expiry = (
        random_datetime + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    ).timestamp()
    assert payload["exp"] == expected_expiry


@patch("src.app.utils.datetime")
def test_create_access_token_has_expiry(mock_datetime):
    random_datetime = datetime(2024, 12, 1, 0, 0, 0, tzinfo=timezone.utc)
    mock_datetime.utcnow.return_value = random_datetime
    data_to_token = "FAKE_USERNAME"

    expires_delta = timedelta(minutes=15)
    token = create_access_token(data_to_token, expires_delta=expires_delta)
    payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

    expected_expiry = (random_datetime + expires_delta).timestamp()
    assert payload["exp"] == expected_expiry
