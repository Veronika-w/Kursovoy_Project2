import unittest

from unittest.mock import mock_open, patch

import json

from src.save_info_plane import SaveInfoPlane


class TestWorkWithFile(unittest.TestCase):
    def setUp(self):
        self.path = 'test_data.json'
        self.work_with_file = SaveInfoPlane(self.path)

    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        'items': [
            {
                'name': 'Python Developer',
                'apply_alternate_url': 'https://example.com/apply',
                'salary': {'from': 1000, 'to': 2000},
                'area': {'name': 'Москва'}
            }
        ]
    }))
    def test_read_data_json(self, mock_file):
        # Тестируем чтение данных из файла
        self.work_with_file.read_data_json()

        self.assertEqual(len(self.work_with_file.info_about_vacancies), 1)
        self.assertEqual(self.work_with_file.info_about_vacancies[0].vacancy_name, 'Python Developer')
        self.assertEqual(self.work_with_file.info_about_vacancies[0].vacancy_link, 'https://example.com/apply')
        self.assertEqual(self.work_with_file.info_about_vacancies[0].salary_from, 1000)
        self.assertEqual(self.work_with_file.info_about_vacancies[0].area, 'Москва')

    def test_return_vacancies(self):
        # Тестируем метод возвращения вакансий
        self.work_with_file.info_about_vacancies = [{'name': 'Test Vacancy'}]
        vacancies = SaveInfoPlane.return_vacancies()
        self.assertEqual(vacancies, [])

    def test_str_method(self):
        # Тестируем str метод
        self.work_with_file.info_about_vacancies = [{'name': 'Test Vacancy'}]
        expected_output = "[{'name': 'Test Vacancy'}]"
        self.assertEqual(str(self.work_with_file), expected_output)


if __name__ == '__main__':
    unittest.main()