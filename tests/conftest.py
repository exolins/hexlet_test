#conftest.py
import pytest
@pytest.fixture
def db(scope="session"):
    conn = "connect('sqlite:///memory')"
    return conn
