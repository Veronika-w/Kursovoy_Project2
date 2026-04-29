import os
import pytest

from dotenv import load_dotenv
from src.api_adapter import APIAdapter

from unittest.mock import patch

load_dotenv()
API_KEY = os.getenv("API_KEY")


@pytest.fixture()
def opensky_example():
    """Фикстура экземпляр класса APIAdapter"""
    return APIAdapter(opensky_url="https://opensky-network.org/api/states/all?")


def test_opensky_api_init(opensky_example):
    assert opensky_example.opensky_url == "https://opensky-network.org/api/states/all?"


@pytest.fixture
def mock_opensky_api():
    """Создаем mock-объект для APIAdapter."""
    platform = APIAdapter(opensky_url="https://opensky-network.org/api/states/all?")
    return platform

def test_connect_success(mock_opensky_api):
    """Тест на успешное подключение к API."""
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200

        assert mock_opensky_api.connect() is True


