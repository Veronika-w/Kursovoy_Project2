from src.save_info_plane import SaveInfoPlane
from src.api_adapter import APIAdapter
from src.airplane import Airplane

class Aeroplane:

    result = []

    def __init__(self, callsign=None, country=None, velocity=None, geo_altitude=None):
        self.callsign = callsign
        self.country = country
        self.velocity = velocity
        self.geo_altitude = geo_altitude

    @classmethod
    def cast_to_object_list(cls, country_aeroplanes):
        for item in country_aeroplanes:
            one_aeroplane = {"callsign": item[1],
                        "country": item[2],
                        "velocity": item[5],
                        "geo_altitude": item[7]}
            callsign = item[1]
            country = item[2]
            velocity = item[5]
            geo_altitude = item[7]
            cls.result.append(one_aeroplane)
            cls(callsign, country, velocity, geo_altitude)

# Создание экземпляра класса для работы с API сайтов с самолетами
api = APIAdapter()

# Получение информации о самолетах с opensky-network.org
aeroplanes = api.get_coordinates('Spain')

# Преобразование набора данных в список объектов
aeroplanes = Aeroplane.cast_to_object_list(aeroplanes)

# Пример работы контструктора класса с одним самолетом
aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)


json_saver = SaveInfoPlane()
json_saver.add_to_file(aeroplanes)
# json_saver.remove_from_file(aeroplanes)

# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
    altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000

    filtered_aeroplanes = get_airplanes_by_country(aeroplanes, filter_words)

    ranged_aeroplanes = geo_altitude(aeroplanes, altitude_range)

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print_aeroplanes(top_aeroplanes)


if __name__ == "__main__":
    user_interaction()