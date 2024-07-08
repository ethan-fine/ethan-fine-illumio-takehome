import sys
sys.path.append("./")

import unittest
from src.file_processor import FileProcessor

class TestFileProcessor(unittest.TestCase):

    TEST_FILE_DIR = 'tests/data/'
    TEST_FILE_PATH = TEST_FILE_DIR + 'test.txt'

    def setUp(self):
        self.file_contents = 'Testing is an essential part of coding.\nImproper testing can lead to bugs, financial loss, and more bad consequences.'
        with open(TestFileProcessor.TEST_FILE_PATH, 'w', encoding=FileProcessor.TXT_FILE_ENCODING) as file:
            file.write(self.file_contents)

    def test_get_file_words_file_not_found(self):
        assert FileProcessor.get_file_words(TestFileProcessor.TEST_FILE_DIR + 'file_not_found.txt') == None
        
    def test_get_file_words(self):
        expected_output = ['testing', 'is', 'an', 'essential', 'part', 'of', 'coding', 'improper', 'testing', 'can', 'lead', 'to', 'bugs', 'financial', 'loss', 'and', 'more', 'bad', 'consequences']
        output = FileProcessor.get_file_words(TestFileProcessor.TEST_FILE_PATH)
        assert expected_output == output

    def test_get_file_contents_file_not_found(self):
        assert FileProcessor.get_file_contents(TestFileProcessor.TEST_FILE_DIR + 'file_not_found.txt') == None

    def test_get_file_contents(self):
        output = FileProcessor.get_file_contents(TestFileProcessor.TEST_FILE_PATH)
        assert output == self.file_contents

if __name__ == '__main__':
    unittest.main()
