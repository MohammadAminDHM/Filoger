from prettytable import PrettyTable

user_input = input()

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

letters_in_input = PrettyTable()

letters_in_input.field_names = ["NAME", "FREQUENCY"]

letters_in_inp = list()

def is_found_letter(char):
    for letter in letters:
        if letter == char:
            return True
    return False

def is_exist(char):
    for i in range(0, len(letters_in_inp)):
        if letters_in_inp[i] == char:
            return True
    return False

def find_index(char):
    for i in range(0, len(letters_in_inp)+1):
        if letters_in_inp[i] == char:
            return i

def letters_counter(str):
    for letter in str:
        if is_found_letter(letter):
            if is_exist(letter):
                index_of_letter = find_index(letter)
                letters_in_inp[index_of_letter + 1] += 1
            else:
                letters_in_inp.append(letter)
                letters_in_inp.append(1)

def add_to_table():
    for i in range(0, len(letters_in_inp), 2):
        letters_in_input.add_row([letters_in_inp[i], letters_in_inp[i+1]])

def print_table():
    print (letters_in_input)

letters_counter(user_input)
add_to_table()
print_table()

