import pytest
from unittest.mock import MagicMock
from src.word_match_counter import WordMatchCounter

PREDEFINED_WORDS_FILE_PATH = 'predefined_words.txt'
WORDS_TO_COUNT_FILE_PATH = 'words_to_count.txt'

NO_PREDEFINED_WORDS_OUTPUT = """Predefined word          Match count
------------------------------------
"""

### Testing predefined words and words to count files being non-existent ###
class MockNonExistentFilesProcessor:
    @staticmethod
    def get_file_words(file_path):
        return None

@pytest.fixture
def word_match_counter_non_existent_files(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockNonExistentFilesProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map_non_existent_files(word_match_counter_non_existent_files):
    output = word_match_counter_non_existent_files.get_word_match_count_map()
    assert output == None

def test_get_word_match_count_table_non_existent_files(word_match_counter_non_existent_files):
    output = word_match_counter_non_existent_files.get_word_match_count_table()
    assert output == None

### Testing predefined words file being non-existent, words to count file being populated ###
class MockNonExistentPredefinedWordsFileProcessor:
    @staticmethod
    def get_file_words(file_path):
        if file_path == PREDEFINED_WORDS_FILE_PATH:
            return None
        elif file_path == WORDS_TO_COUNT_FILE_PATH:
            return ['hello']

@pytest.fixture
def word_match_counter_non_existent_predefined_words_file(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockNonExistentPredefinedWordsFileProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map_non_existent_predefined_words_file(word_match_counter_non_existent_predefined_words_file):
    output = word_match_counter_non_existent_predefined_words_file.get_word_match_count_map()
    assert output == None

def test_get_word_match_count_table_non_existent_predefined_words_file(word_match_counter_non_existent_predefined_words_file):
    output = word_match_counter_non_existent_predefined_words_file.get_word_match_count_table()
    assert output == None

### Testing predefined words file being populated, words to count file being non-existent ###
class MockNonExistentWordsToCountFileProcessor:
    @staticmethod
    def get_file_words(file_path):
        if file_path == PREDEFINED_WORDS_FILE_PATH:
            return ['hello']
        elif file_path == WORDS_TO_COUNT_FILE_PATH:
            return None

@pytest.fixture
def word_match_counter_non_existent_words_to_count_file(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockNonExistentWordsToCountFileProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map_non_existent_words_to_count_file(word_match_counter_non_existent_words_to_count_file):
    output = word_match_counter_non_existent_words_to_count_file.get_word_match_count_map()
    assert output == None

def test_get_word_match_count_table_non_existent_words_to_count_file(word_match_counter_non_existent_words_to_count_file):
    output = word_match_counter_non_existent_words_to_count_file.get_word_match_count_table()
    assert output == None

### Testing predefined words and words to count files being empty ###
class MockEmptyFileProcessor:
    @staticmethod
    def get_file_words(file_path):
        if file_path == PREDEFINED_WORDS_FILE_PATH:
            return []
        elif file_path == WORDS_TO_COUNT_FILE_PATH:
            return ['hello']

@pytest.fixture
def word_match_counter_empty_files(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockEmptyFileProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map_empty_files(word_match_counter_empty_files):
    output = word_match_counter_empty_files.get_word_match_count_map()
    assert output == {}

def test_get_word_match_count_table_empty_files(word_match_counter_empty_files):
    output = word_match_counter_empty_files.get_word_match_count_table()
    assert output == NO_PREDEFINED_WORDS_OUTPUT

### Testing predefined words file being empty, words to count file being populated ###
class MockEmptyPredefinedWordsFileProcessor:
    @staticmethod
    def get_file_words(file_path):
        if file_path == PREDEFINED_WORDS_FILE_PATH:
            return []
        elif file_path == WORDS_TO_COUNT_FILE_PATH:
            return ['hello']

@pytest.fixture
def word_match_counter_empty_predefined_words_file(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockEmptyPredefinedWordsFileProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map_empty_predefined_words_file(word_match_counter_empty_predefined_words_file):
    output = word_match_counter_empty_predefined_words_file.get_word_match_count_map()
    assert output == {}

def test_get_word_match_count_table_empty_predefined_words_file(word_match_counter_empty_predefined_words_file):
    output = word_match_counter_empty_predefined_words_file.get_word_match_count_table()
    assert output == NO_PREDEFINED_WORDS_OUTPUT

### Testing predefined words file being populated, words to count file being empty ###
class MockEmptyWordsToCountFileProcessor:
    @staticmethod
    def get_file_words(file_path):
        if file_path == PREDEFINED_WORDS_FILE_PATH:
            return ['hello', 'world']
        elif file_path == WORDS_TO_COUNT_FILE_PATH:
            return []

@pytest.fixture
def word_match_counter_empty_words_to_count_file(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockEmptyWordsToCountFileProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map_empty_words_to_count_file(word_match_counter_empty_words_to_count_file):
    output = word_match_counter_empty_words_to_count_file.get_word_match_count_map()
    assert output == {'hello': 0, 'world': 0}

def test_get_word_match_count_table_empty_words_to_count_file(word_match_counter_empty_words_to_count_file):
    output = word_match_counter_empty_words_to_count_file.get_word_match_count_table()
    expected_output = """Predefined word          Match count
------------------------------------
hello                    0
world                    0
"""
    assert output == expected_output

### Testing predefined words and words to count files being populated ###
class MockPopulatedFilesProcessor:
    @staticmethod
    def get_file_words(file_path):
        if file_path == PREDEFINED_WORDS_FILE_PATH:
            return ['how', 'a', 'day', 'you', 'today', 'hello', 'unmatched']
        elif file_path == WORDS_TO_COUNT_FILE_PATH:
            return ['hello', 'how', 'are', 'you', 'doing', 'today', 'it', 'is', 'a', 'beautiful', 'day', 'today', 'we', 'should', 'have', 'a', 'picnic']

@pytest.fixture
def word_match_counter(monkeypatch):
    monkeypatch.setattr('src.word_match_counter.FileProcessor', MockPopulatedFilesProcessor)
    return WordMatchCounter(PREDEFINED_WORDS_FILE_PATH, WORDS_TO_COUNT_FILE_PATH)

def test_get_word_match_count_map(word_match_counter):
    output = word_match_counter.get_word_match_count_map()
    expected_output = {'a': 2, 'today': 2, 'day': 1, 'hello': 1, 'how': 1, 'you': 1, 'unmatched': 0}
    assert output == expected_output

def test_get_word_match_count_table(word_match_counter):
    output = word_match_counter.get_word_match_count_table()
    expected_output = """Predefined word          Match count
------------------------------------
a                        2
today                    2
day                      1
hello                    1
how                      1
you                      1
unmatched                0
"""
    assert output == expected_output

