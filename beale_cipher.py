# Amir Abu Hani
# In addition to this file there is another file declaration_of_independence.txt

# To create an iterator, At first I create a BealeCipher class
class BealeCipher:
    # Constructor
    def __init__(self, keys, file_path):
        self.keys = keys
        self.file_path = file_path
        # Opening the declaration_of_independence.txt to read the words
        self.file = open(file_path, 'r')

    # Iterator
    def __iter__(self):
        return self

    # moving to the next key from the keys list
    def __next__(self):
        # At first, we try to read the file
        text = self.file.read()
        # By split, every word in the text entered to a list, ignoring the whitespace
        words = text.split()
        message = ""
        # if the text is empty, close the file
        if not text:
            self.file.close()
            raise StopIteration
        else:
            for key in self.keys:
                # if the current key is smaller than the length of the words list
                if key < len(words):
                    # extract the word in index key - 1(because  the list indexes starts from 0)
                    extract_word = words[key - 1]
                    # get the first letter from the word and make it uppercase
                    first_letter = extract_word[0].upper()
                    # concatenation the letter to the message
                    message += first_letter

        return message


keys = [4, 93, 52, 12, 41, 23, 9, 1, 34, 2, 11, 111, 6, 13, 24, 99, 100,
        30, 10, 26, 16, 29, 155, 32, 37, 61, 15, 42, 3, 633, 27, 70, 77,
        45, 55, 43, 35, 108, 103, 56, 159, 166, 7, 8, 174, 36]
# The path to the declaration_of_independence.txt file(both files are in the same folder)
file_path = "declaration_of_independence.txt"
# Create an iterator that takes the keys list and the file by the path
my_iterator = BealeCipher(keys, file_path)
for letter in my_iterator:
    print(letter)
