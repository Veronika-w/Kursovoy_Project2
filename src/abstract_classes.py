from abc import ABC, abstractmethod


class AbstractAPIAdapter(ABC):

    @abstractmethod
    def get_coordinates(self, country: str) -> list:
        """Получить гео координаты страны"""
        pass

    @abstractmethod
    def get_airplanes_in_area(self, area_geo_coordinates: list) -> dict:
        """Получить информацию о самолетах в заданной области"""
        pass

    @abstractmethod
    def get_airplanes_by_country(self, country: str) -> dict:
        """Получить информацию о самолетах над указанной страной"""
        pass


class AbstractSaveInfoPlane(ABC):
    """абстрактный класс для класса SaveInfoPlane"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_to_file(self, airplanes):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def return_airplanes(self):
        pass
