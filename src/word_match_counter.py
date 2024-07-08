import sys
sys.path.append("./")

from src.file_processor import FileProcessor
from typing import Dict, List

class WordMatchCounter:

    WORD_COL_HEADER = 'Predefined word'
    COUNT_COL_HEADER = 'Match count'

    def __init__(self, predefined_words_file_path: str, words_to_count_file_path: str):
        predefined_words = FileProcessor.get_file_words(predefined_words_file_path)
        self.predefined_words = set(predefined_words) if predefined_words != None else None
        self.words_to_count = FileProcessor.get_file_words(words_to_count_file_path)
    
    def get_word_match_count_map(self) -> Dict[str, int]:
        if self.predefined_words == None or self.words_to_count == None:
          return None

        word_match_count_map = {}
        for predefined_word in self.predefined_words:
            word_match_count_map[predefined_word] = 0
        for word_to_count in self.words_to_count:
            if word_to_count not in self.predefined_words:
                continue
            word_match_count_map[word_to_count] += 1
        
        return word_match_count_map
    
    def get_word_match_count_table(self) -> str:
        word_match_count_map = self.get_word_match_count_map()
        if word_match_count_map == None:
            return None

        sorted_word_match_count_entries = sorted(word_match_count_map.items(), key=lambda x: (-x[1], x[0]))

        word_col_rows = [WordMatchCounter.WORD_COL_HEADER]
        count_col_rows = [WordMatchCounter.COUNT_COL_HEADER]
        max_word_col_length = len(WordMatchCounter.WORD_COL_HEADER)
        
        for word, count in sorted_word_match_count_entries:
            max_word_col_length = max(max_word_col_length, len(word))
            word_col_rows.append(word)
            count_col_rows.append(str(count))
        
        chars_prior_to_count_col_start = max_word_col_length + 10
        header_separator_line = '-' * (chars_prior_to_count_col_start + len(WordMatchCounter.COUNT_COL_HEADER))

        formatted_word_match_count_table = ''
        for table_row_index in range(len(word_col_rows)):
            word_col_entry = word_col_rows[table_row_index]
            count_col_entry = count_col_rows[table_row_index]

            spacing_between_cols = ' ' * (chars_prior_to_count_col_start - len(word_col_entry))
            formatted_row = word_col_entry + spacing_between_cols + count_col_entry
            formatted_word_match_count_table += formatted_row + '\n'
            if table_row_index == 0:
                formatted_word_match_count_table += header_separator_line + '\n'
        
        return formatted_word_match_count_table
