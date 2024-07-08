import re
from typing import List

class FileProcessor:
  
    FILE_READ_MODE = 'r'
    TXT_FILE_ENCODING = 'ascii'
    WORD_PATTERN = re.compile(r'\b\w+\b')

    @staticmethod
    def get_file_words(file_path: str) -> List[str]:
        file_contents = FileProcessor.get_file_contents(file_path)
        if file_contents:
            return FileProcessor.WORD_PATTERN.findall(file_contents.lower())

        return None

    @staticmethod
    def get_file_contents(file_path: str) -> str:
        try:
            with open(file_path, FileProcessor.FILE_READ_MODE, encoding=FileProcessor.TXT_FILE_ENCODING) as file:
                return file.read()
        except FileNotFoundError:
            print(f"Please revise your run arguments.\nCould not find file at path {file_path}.")
        except Exception as e:
            print(f"Encountered an error while reading {file_path}. Error: {e}")

        return None