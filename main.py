import os
import re
from collections import Counter

class StringFunctions:
    def __init__(self, filepath):
        self.filepath = filepath
        self.lines = []
        self.words = []
        self.load_file()

    def load_file(self):
        """Load the file content."""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"The file {self.filepath} does not exist.")
        
        with open(self.filepath, 'r') as file:
            content = file.read()
        
        self.words = re.findall(r'\b\w+\b', content.lower())  # Find all words
        self.lines = content.splitlines()  # Get lines in the file

    def count_lines(self):
        """Count the number of lines."""
        return len(self.lines)

    def count_unique_words(self):
        """Count unique words."""
        return len(set(self.words))

    def word_frequencies(self):
        """Count the frequency of each word."""
        return dict(Counter(self.words))

    def capitalize_first_last_chars(self):
        """Capitalize first and last characters of each line."""
        modified_lines = []
        for line in self.lines:
            if len(line) > 1:
                line = line[0].upper() + line[1:-1] + line[-1].upper()  
            elif len(line) == 1:
                line = line.upper() 
            modified_lines.append(line)
        return modified_lines
