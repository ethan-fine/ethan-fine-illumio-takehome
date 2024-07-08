import sys
from word_match_counter import WordMatchCounter

def output_word_match_count(predefined_words_file_path: str, words_to_count_file_path: str) -> None:
  word_match_counter = WordMatchCounter(predefined_words_file_path, words_to_count_file_path)
  word_match_count_table = word_match_counter.get_word_match_count_table()

  if word_match_count_table:
    print(word_match_count_table)

if __name__ == "__main__":
  run_args = sys.argv
  if len(run_args) == 3:
    predefined_words_file_path = run_args[1]
    words_to_count_file_path = run_args[2]

    output_word_match_count(predefined_words_file_path, words_to_count_file_path)
  else:
    print('Please revise your run arguments.\nUsage: python main.py <predefined words file path> <words to count file path>')

