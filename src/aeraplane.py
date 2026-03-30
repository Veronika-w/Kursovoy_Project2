class Aeroplane:
    """
        Класс для работы с информацией о самолетах
    """
    MIN_VELOCITY = 0  # минимальная скорость самолета (м/c)
    MAX_VELOCITY = 700  # максимальная скорость самолета (м/c)

    MIN_GEO_ALTITUDE = 0 # минимальная высота самолета (м)
    MAX_GEO_ALTITUDE = 37000 # максимальная высота самолета (м)

    def __init__(self, callsign, country, velocity, geo_altitude):
        self._velocity = None
        self._geo_altitude = None

        self.callsign = callsign
        self.country = country
        self.velocity = velocity
        self.geo_altitude = geo_altitude

    @classmethod
    def cast_to_object_list(cls, airplanes: list[dict]) -> list["Aeroplane"]:
        """Возвращает список экземпляров Aeroplane из списка словарей"""

        return [cls(**plane) for plane in airplanes]

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        """Сеттер для скорости с валидацией"""
        if value is not None:
            if value < self.MIN_VELOCITY or value > self.MAX_VELOCITY:
                raise ValueError(f"Скорость должна быть в диапазоне"
                                 f" от {self.MIN_VELOCITY} до {self.MAX_VELOCITY}")
            self._velocity = float(value)
        else:
            self.velocity = None

    def __ge__(self, other: 'Aerplane') -> bool:
        """Сравниваем скорости двух обьектов класса Aerplane"""
        if not isinstance(other, Aeroplane):
            return
        print(self.velocity, " >= ", other.velocity)
        return self.velocity >= other.velocity


    @property
    def geo_altitude(self):
        return self._geo_altitude

    @geo_altitude.setter
    def geo_altitude(self, value):
        """Сеттер для высоты с валидацией"""
        if value is not None:
            if value < self.MIN_GEO_ALTITUDE or value > self.MAX_GEO_ALTITUDE:
                raise ValueError(f"Высота должна быть в диапазоне"
                                 f" от {self.MIN_GEO_ALTITUDE} до {self.MAX_GEO_ALTITUDE}")
            self._geo_altitude = float(value)
        else:
            self.geo_altitude = None

    def __eq__(self, other: 'Aerplane') -> bool:
        """Сравниваем на равенство по высоте
        двух одинаковых обьектов класса Aerplane"""
        if not isinstance(other, Aeroplane):
            return
        print(self.geo_altitude, " == ", other.geo_altitude)
        return self.geo_altitude == other.geo_altitude



if __name__ == "__main__":
    aeroplane1 = Aeroplane(
        "N5641X",
        "United States",
        341.57,
        10203.18
    )

    aeroplane2 = Aeroplane(
        "PVL832",
        "Canada",
        341.58,
        10203.18
    )

    print(aeroplane1 == aeroplane2)
    print(aeroplane1 >= aeroplane2)