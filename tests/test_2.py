import unittest
import ya_app



class TestYandexTranslator(unittest.TestCase):
    def test_translate(self):
        self.assertEqual(ya_app.translate_it('hi')['text'][0], 'привет')

    def test_request_code(self):
        self.assertEqual(ya_app.translate_it('hi')['code'], 200)
