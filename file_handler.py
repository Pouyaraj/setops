import re

class FileHandler:
    @staticmethod
    def read_file_to_words(filename):
        if not filename:
            print("Usage: python your_script.py <filename>")
            return []

        try:
            with open(filename, 'r') as f:
                content = f.read()

                if not content.strip():
                    print("No input parameters are provided.")
                    return []

                content = content.replace(',', ' ').replace(';', ' ').replace('\'', ' ').replace('"', ' ')
                words = content.split()

                cleaned_words = []
                for word in words:
                    if '.' in word and all(char.isdigit() or char == '.' for char in word):
                        cleaned_words.append(word)
                    else:
                        cleaned_words.extend(re.findall(r'\b[a-zA-Z0-9]+\b', word))

                return cleaned_words
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
            return []
        except Exception as e:
            print(f"Error reading file '{filename}': {str(e)}")
            return []
