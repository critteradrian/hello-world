import random

letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
               "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "!"]

target_string = "hello world!"
string = ""

while string != target_string:
    random_letter = random.choice(letter_list)
    for char in target_string:
        while random_letter != char:
            random_letter = random.choice(letter_list)
            print(string + random_letter)
        string += random_letter
