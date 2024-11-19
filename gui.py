import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from main import TextAnalyzer  

class gui:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Text File Analyzer")
        self.root.geometry("500x600")
        # instance of String func
        self.root.text_analyzer = None 

        # -----------load File button------
        self.load_button = Button(self.root, text="Load File", command=self.load_file, bd = 6, font = ("sans-serif", 10, "bold"), padx=15)
        self.load_button.pack(pady=20)

        # -----------modified text area----------
        self.modified_text_area = Text(self.root, width=60, height=8)
        self.modified_text_area.pack(pady=10)

        # -----------stats button-----------
        self.stats_button = Button(self.root, text="Show Statistics", command=self.display_summary, bg = "green", bd = 6, font = ("sans-serif", 10, "bold"))
        self.stats_button.pack(pady=5)

        # ----------statistics text box-----------
        self.stats_textbox = Text(self.root, width=60, height=200, wrap=tk.WORD, bg="light gray")
        self.stats_textbox.pack(pady=10)

    def load_file(self):
        """
        Loads a file using a file dialog and processes it to make first and last char as upper
        """
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            try:
                self.text_analyzer = TextAnalyzer(file_path)
                self.display_modified_text()
            except Exception as e:
                messagebox.showerror("Error", f"Error loading file: {e}")

    def display_modified_text(self):
        """
        Display the modified text with capitalized first and last characters of each line.
        """
        if self.text_analyzer:
            modified_lines = self.text_analyzer.capitalize_first_last_chars()
            self.modified_text_area.delete(1.0, END) 
            for line in modified_lines:
                self.modified_text_area.insert(END, line + '\n')

    def display_summary(self):
        """
        Display file statistics
        """
        if self.text_analyzer:
            lines_count = self.text_analyzer.count_lines()
            unique_words_count = self.text_analyzer.count_unique_words()
            word_freq = self.text_analyzer.word_frequencies()

            summary_text = f"Number of Lines: {lines_count}\n"
            summary_text += f"Unique Words: {unique_words_count}\n\n"
            summary_text += "Word Frequencies:\n"
            for word, freq in word_freq.items():
                summary_text += f"{word}: {freq}\n"

            self.stats_textbox.delete(1.0, END)
            self.stats_textbox.insert(END, summary_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = gui(root)
    root.mainloop()
