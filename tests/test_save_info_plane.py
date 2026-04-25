import unittest

from unittest.mock import mock_open, patch

import json

from src.save_info_plane import SaveInfoPlane


class TestSaveInfoPlane(unittest.TestCase):
    def setUp(self):
        self.path = 'test_data.json'
        self.work_with_file = SaveInfoPlane(self.path)

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        'items': [
            {
                'callsign': 'N5641X',
                'country': 'United States',
                'velocity': 341.57,
                'geo_altitude': 10203.18
            }
        ]
    }))
    def test_read_file(self, mock_file):
        # Тестируем чтение данных из файла
        self.work_with_file.read_file()
        self.assertEqual(len(self.work_with_file.info_about_airplane), 1)
        self.assertEqual(self.work_with_file.info_about_airplane[0].callsign, 'N5641X')
        self.assertEqual(self.work_with_file.info_about_airplane[0].country, 'United States')
        self.assertEqual(self.work_with_file.info_about_airplane[0].velocity, 341.57)
        self.assertEqual(self.work_with_file.info_about_airplane[0].geo_altitude, 10203.18)


    def test_return_airplanes(self):
        # Тестируем метод возвращения вакансий
        self.work_with_file.info_about_airplane = [{'callsign': 'Test N5641X'}]
        airplanes = SaveInfoPlane.return_airplanes()
        self.assertEqual(airplanes, [])


    def test_str_method(self):
        # Тестируем str метод
        self.work_with_file.info_about_airplane = [{'callsign': 'Test N5641X'}]
        expected_output = "[{'callsign': 'Test N5641X'}]"
        self.assertEqual(str(self.work_with_file), expected_output)