import unittest

import pytest

from src.aeraplane import Aeroplane


class TestAeroplane(unittest.TestCase):
    """ класс тестирует Aeroplane """

    def test_aeroplane_init(self):
        aeroplane = Aeroplane(callsign="N5641X", country="United States", velocity=341.57,
                          geo_altitude=10203.18)

        self.assertEqual(aeroplane.callsign, "N5641X")
        self.assertEqual(aeroplane.country, "United States")
        self.assertEqual(aeroplane.velocity, 341.57)
        self.assertEqual(aeroplane.geo_altitude, 10203.18)


    def test_comparison_velocity_geo_altitude_1(self):
        """Тестирование магического метода __ge__, __eq__ (сравнение объектов)."""
        aeroplane1 = Aeroplane(callsign="N5641X", country="United States", velocity=341.57,
                           geo_altitude=10203.18)
        aeroplane2 = Aeroplane(callsign="PVL832", country="Canada", velocity=341.58,
                           geo_altitude=10203.19)

        self.assertFalse(aeroplane1 == aeroplane2)
        self.assertTrue(aeroplane2 >= aeroplane1)


    def test_comparison_velocity_geo_altitude_2(self):
        """Тестирование сравнения объектов с одинаковыми значениями"""
        aeroplane1 = Aeroplane(callsign="N5641X", country="United States", velocity=341.57,
                           geo_altitude=10203.19)
        aeroplane2 = Aeroplane(callsign="PVL832", country="Canada", velocity=341.57,
                           geo_altitude=10203.19)

        self.assertTrue(aeroplane1 == aeroplane2)
        self.assertTrue(aeroplane2 >= aeroplane1)


    def test_aeroplane_str_method(self):
        """Тестирование метода __str__ для корректного вывода строки."""
        aeroplane = Aeroplane("UAL1621", "United States", 268.79, 10203.18)

        expected_str = "Позывной рейса: UAL1621, страна регистрации ВС: United States, горизонтальная скорость: 268.79 м/с, геометрическая высота: 10203.18 м."
        self.assertEqual(str(aeroplane), expected_str)
