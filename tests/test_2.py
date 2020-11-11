import unittest
import yaupload


class TestYandexCreateFolder(unittest.TestCase):

    def test_make_folder(self):
        self.assertEqual(yaupload.Yandex('AgAAAAABi8gVAADLW0CcC5xw1U7EgXu1aWgdbB8'
                                         ).make_folder('test_folder'), 201) # Папка создана отлично

    def test_make_folder_second(self):
        self.assertEqual(yaupload.Yandex('AgAAAAABi8gVAADLW0CcC5xw1U7EgXu1aWgdbB8'
                                         ).make_folder('test_folder'), 409) # Такая папка уже существует

    def test_make_folder_fail_auth(self):
        self.assertEqual(yaupload.Yandex('token'
                                         ).make_folder('test_folder'), 401) # Ошибка авторизации


if __name__ == '__main__':
    unittest.main()
