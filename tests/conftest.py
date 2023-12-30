import pytest


@pytest.fixture(scope="function")
def test_dataframe():
    data = [
        ("a", "aa", 1.0, 2.0, 3.0, 4.0),
        ("b", "bb", -1.0, -2.0, -3.0, -4.0),
        ("c", "cc", 5.0, 6.0, 7.0, 8.0),
    ] * 10

    return data
