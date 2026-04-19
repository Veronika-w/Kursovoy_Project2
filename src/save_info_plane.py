from src.abstract_classes import AbstractSaveInfoPlane
from src.airplane import Airplane
import json



class SaveInfoPlane(AbstractSaveInfoPlane):
    """ класс для работы с файлами """
    info_about_airplane: list = []

    def __init__(self, path: str = 'data/info_plane.json'):
        self.__path = path
        self.info_about_airplane = []

    # блок функций для добавления в файлы
    def add_to_file(self, airplanes: list[dict]):
        """ функция добавляет данные формата json в файл"""
        with open(self.__path, 'w', encoding='utf-8') as json_file:
            json.dump(airplanes, json_file, ensure_ascii=False, indent=4)

    # блок функций для чтения из файла
    def read_file(self):
        """ чтение json файла """
        try:
            with open(self.__path, 'r', encoding='utf-8') as json_file:
                data = json.load(json_file)
            airplanes = []
            for airplane in data['items']:
                airplanes.append(Airplane(
                    airplane['callsign'],
                    airplane['country'],
                    airplane['velocity'],
                    airplane['geo_altitude']
                ))

                self.info_about_airplane = airplanes
        except FileNotFoundError:
            print(f"Файл {self.__path} не найден.")
            self.info_about_airplane = []

    @classmethod
    def return_airplanes(cls):
        """ чтение json файла """
        return cls.info_about_airplane

    # удаление данных из файла
    def remove_from_file(self):
        """ функция удаляет данные из файла """
        with open(self.__path, 'w'):
            pass

    def __str__(self):
        return str(getattr(self, 'info_about_airplane', ''))


if __name__ == "__main__":
    airplane1 = Airplane(
        "N5641X",
        "United States",
        341.57,
        10203.18
    )

    airplane2 = Airplane(
        "PVL832",
        "Canada",
        341.58,
        10203.18
    )

    new_airplane1 = SaveInfoPlane.add_to_file('../data/info_plane.json', 'airplane1')
    print(airplane1)
