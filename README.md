# Ethan Fine Takehome Assessment Submission for Illumio

## How to run the program:
1. Open Terminal (MacOS) or Command Prompt (Windows) - assuming Python3 is installed
2. Move input files for predefined words and words to count into input_data folder within project directory as two separate txt files (there are already two input files available there as examples)
3. Type commands as follow:
  i. cd path/to/root/of/program/folder  (navigates to project - verify you are within ethan_fine_illumio_takehome)
  ii. python -m venv venv    (sets up virtual environment)
  iii. source venv/bin/activate (MacOS) or venv\Scripts\activate (Windows)   (activates virtual environment)
  iv. pip install -r requirements.txt   (installs project dependencies within virtual environment)
  v. python src/main.py input_data/<predefined_words_file_name>.txt input_data/<words_to_count_file_name>.txt
  vi. pytest tests/   (runs tests)
  vii. deactivate (MacOS) or venv\Scripts\deactivate (Windows)   (exit the venv, only once done using the program)

Note that I only have the ability to test the above commands on a Mac. Please reach out to me at ef376@cornell.edu if you need assistance running this program on a Windows machine.

## What has been tested:
- Unit tests for file processor (which ingests input files and extracts a list of their words in lowercase)
  - File not found case
  - Non-empty, multi-line file case. This case includes having punctuation in the text, as well as the same words with different capitalizations.
- Unit tests for word match counter (which given predefined words file path and words to count file path generates a dictionary or formatted text mapping of predefined words to their match count in the words to count file). Assumes the file processor, which is tested separately, returns the proper output.
Both the dictionary and formatted text mapping output types are tested for each case.
  - Non-existent predefined words and words to count files case
  - Non-existent predefined words and populated words to count files case
  - Populated predefined words and non-existent populated words to count files case
  - Empty predefined words and words to count files case
  - Empty predefined words and populated words to count files case
  - Populated predefined words and empty words to count files case
  - Populated predefined words and populated words to count files case (with some words to count that are not predefined words as well as some predefined words that have no match in the words to count)
- Manual testing of all cases above through running the program with varied inputs
- Manual testing of incomplete arguments at runtime triggering proper usage message

## Assumptions:
- There is no UI required for this project. A command-line interface suffices.
- A word is defined as a set of characters with no space in between, stripped of punctuation. Spaces or new lines between two sets of characters denotes a separation of two words.
- Although the predefined words will not contain exact duplicates, there may be predefined words that are duplicate once they are converted to lower case. In this case, since matches should be case-insensitive, the predefined words falling under this category should be only listed once in the output table, with their case-insensitive match count.
- Output should list words in descending order of match counts. In the case of match count ties, words should be listed in lexicographical order.
- Output should include the match count for every word in the predefined words list, regardless of whether this count is 0 or greater than 0
