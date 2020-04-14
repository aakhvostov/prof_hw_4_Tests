import json
import unittest
import os
from unittest.mock import patch
import app


documents = []
directories = {}


def setUpModule():
    current_path = str(os.path.dirname(os.path.abspath(__file__)))
    path_directories = os.path.join(current_path, '../fixtures/directories.json')
    path_documents = os.path.join(current_path, '../fixtures/documents.json')
    with open(path_directories, 'r', encoding='utf-8') as dir:
        directories.update(json.load(dir))
    with open(path_documents, 'r', encoding='utf-8') as doc:
        documents.extend(json.load(doc))


@patch('app.directories', directories)
@patch('app.documents', documents)
class TestSecretaryProgram(unittest.TestCase):
    @patch('app.input')
    def test_get_doc_owner_name(self, mock_input):
        mock_input.return_value = '10006'
        doc_number = app.get_doc_owner_name()
        self.assertEqual(doc_number, 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)

    def test_remove_doc_from_shelf(self):
        self.assertNotIn(app.remove_doc_from_shelf('10006'), documents[2])

    @patch('app.input')
    def test_move_doc_to_shelf(self, mock_input):
        mock_input.side_effect = [documents[1]['number'], '1']
        app.move_doc_to_shelf()
        self.assertIn(documents[1]['number'], directories['1'])
    
    def test_get_doc_shelf(self):
        with patch('app.input', return_value='2207 876234'):
            shelf_number = app.get_doc_shelf()
            self.assertEqual(shelf_number, '1')



if __name__ == '__main__':
    unittest.main()