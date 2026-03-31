from json import JSONDecodeError

from src.abstract_classes import AbstractSaveInfoPlane
from src.aeraplane import Aeroplane
import json
import os
from config import DATA_DIR


class SaveInfoPlane(AbstractSaveInfoPlane):
    """ класс для работы с файлами """
    def __init__(self, filename="info_plane.json"):
        """Инициализатор класса JSONSaver"""
        self.__file_path = os.path.join(DATA_DIR, filename)

    def save_to_file(self, airplanes: list[dict]) -> None:
        """Сохраняет данные в json-файл"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(airplanes, f, ensure_ascii=False)

    def read_file(self) -> list[dict]:
        """Считывает данные из json-файла"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except JSONDecodeError:
            data = []

        return data

    def add_airplane(self, airplane: Aeroplane) -> None:
        """Добавляет самолет в файл"""
        airplanes_list = self.read_file()

        if airplane.url not in [vac["url"] for vac in airplanes_list]:
            airplanes_list.append(airplane.to_dict())
            self.save_to_file(airplanes_list)

    def add_airplanes(self, airplanes: list[dict]) -> None:
        """Добавляет самолеты в файл"""
        self.save_to_file(airplanes)

    def del_airplane(self, url: str) -> None:
        """Удаляет самолет из файла"""
        airplanes_list = self.read_file()
        for index, vac in enumerate(airplanes_list):
            if vac["url"] == url:
                airplanes_list.pop(index)

        self.save_to_file(airplanes_list)

    def get_airplane_by_name(self, word: str) -> list[Aeroplane]:
        """Возвращает список самолетов по ключевому слову"""
        found_airplanes = []

        for vac in self.read_file():
            if word in vac.get("name").lower():
                found_airplanes.append(vac)

        return Aeroplane.cast_to_object_list(found_airplanes)

if __name__ == '__main__':
    airplanes = Aeroplane("UAL1621", "United States", 268.79, 10203.18)
    airplanes.geo_altitude
    print(airplanes )