from abc import ABC, abstractmethod


class AbstractAPIAdapter(ABC):

    @abstractmethod
    def get_coordinates(self, country: str) -> list:
        """
            Получить гео координаты страны
        """
        pass

    @abstractmethod
    def get_aeroplanes_in_area(self, area_geo_coordinates: list) -> dict:
        """
             Получить информацию о самолетах в заданной области
        """
        pass

    @abstractmethod
    def get_aeroplanes_by_country(self, country: str) -> dict:
        """
            Получить информацию о самолетах над указанной страной
        """
        pass


class AbstractSaveInfoPlane(ABC):
    """ абстрактный класс для класса SaveInfoPlane"""

    @abstractmethod
    def add_airplane(self, airplane):
        pass

    @abstractmethod
    def get_airplane_by_name(self, word):
        pass

    @abstractmethod
    def del_airplane(self, airplane):
        pass