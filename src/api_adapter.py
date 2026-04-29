from abc import ABC, abstractmethod
import requests
from src.abstract_classes import AbstractAPIAdapter


class APIAdapter(AbstractAPIAdapter):
    """
        Класс для работы с 'https://nominatim.openstreetmap.org/search'
        и 'https://opensky-network.org/api/states/all?'
    """

    def __init__(self, opensky_url="https://opensky-network.org/api/states/all?") -> None:
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = opensky_url
        self.aeroplanes = None


    def connect(self) -> bool:
        """Метод проверяющий доступность API"""
        try:
            response = requests.get(self.opensky_url)
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Ошибка подключения: {e}")
            return False

    def get_coordinates(self, country: str) -> list:
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = requests.get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        geo_coordinates = data[0].get('boundingbox')

        return geo_coordinates

    def get_airplanes_in_area(self, area_geo_coordinates: list) -> dict:
        # Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': area_geo_coordinates[0],
            'lamax': area_geo_coordinates[1],
            'lomin': area_geo_coordinates[2],
            'lomax': area_geo_coordinates[3],
        }

        response = requests.get(url=self.opensky_url, params=params)

        return response.json()

    def get_airplanes_by_country(self, country: str) -> dict:
        get_coordinates = api.get_coordinates(country)
        self.aeroplanes = self.get_airplanes_in_area(get_coordinates)
        return self.aeroplanes


if __name__ == "__main__":
    api = APIAdapter()
    get_coordinates = api.get_airplanes_by_country("Canada")
    print(get_coordinates)