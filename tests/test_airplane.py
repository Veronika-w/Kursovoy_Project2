import unittest

import pytest

from src.airplane import Airplane


class TestAirplane(unittest.TestCase):
    """ класс тестирует Airplane """


    def test_airplane_init(self):
        airplane = Airplane(callsign="N5641X", country="United States", velocity=341.57, geo_altitude=10203.18)
        assert airplane.callsign == "N5641X"
        assert airplane.country == "United States"
        assert airplane.velocity == 341.57
        assert airplane.geo_altitude == 10203.18


    def test_comparison_velocity_geo_altitude_1(self):
        """Тестирование магического метода __ge__, __eq__ (сравнение объектов)."""
        airplane1 = Airplane(callsign="N5641X", country="United States", velocity=341.57,
                               geo_altitude=10203.18)
        airplane2 = Airplane(callsign="PVL832", country="Canada", velocity=341.58,
                               geo_altitude=10203.19)

        assert airplane1 != airplane2
        assert airplane2 >= airplane1


    def test_comparison_velocity_geo_altitude_2(self):
        """Тестирование сравнения объектов с одинаковыми значениями"""
        airplane1 = Airplane(callsign="N5641X", country="United States", velocity=341.57,
                               geo_altitude=10203.19)
        airplane2 = Airplane(callsign="PVL832", country="Canada", velocity=341.57,
                               geo_altitude=10203.19)

        assert airplane1 == airplane2
        assert airplane2 >= airplane1


    def test_airplane_str_method(self):
        """Тестирование метода __str__ для корректного вывода строки."""
        airplane = Airplane("UAL1621", "United States", 268.79, 10203.18)

        expected_str = "Позывной рейса: UAL1621, страна регистрации ВС: United States, горизонтальная скорость: 268.79 м/с, геометрическая высота: 10203.18 м."
        assert str(airplane) == expected_str
