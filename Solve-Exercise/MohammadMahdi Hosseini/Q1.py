# Import the PrettyTable module for creating formatted tables
from prettytable import PrettyTable

# Prompt the user to enter a string of characters
user_input = input()

# Define a list of valid letters and digits
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Define an empty PrettyTable to store the letter frequencies
letters_in_input = PrettyTable()

# Add columns to the table for the letter names and frequencies
letters_in_input.field_names = ["NAME", "FREQUENCY"]

# Define an empty list to store the letters and their frequencies
letters_in_inp = list()

# Define a function to check if a character is in the list of valid letters and digits
def is_found_letter(char):
    for letter in letters:
        if letter == char:
            return True
    return False

# Define a function to check if a given character is already in the list of letters and frequencies
def is_exist(char):
    for i in range(0, len(letters_in_inp)):
        if letters_in_inp[i] == char:
            return True
    return False

# Define a function to find the index of a given character in the list of letters and frequencies
def find_index(char):
    for i in range(0, len(letters_in_inp)+1):
        if letters_in_inp[i] == char:
            return i

# Define a function to count the number of occurrences of each valid character in the input string
def letters_counter(str):
    for letter in str:
        if is_found_letter(letter):
            if is_exist(letter):
                # If the letter is already in the list, increment its frequency
                index_of_letter = find_index(letter)
                letters_in_inp[index_of_letter + 1] += 1
            else:
                # If the letter isn't in the list yet, add it with a frequency of 1
                letters_in_inp.append(letter)
                letters_in_inp.append(1)

# Define a function to add the letters and their frequencies to the PrettyTable
def add_to_table():
    for i in range(0, len(letters_in_inp), 2):
        letters_in_input.add_row([letters_in_inp[i], letters_in_inp[i+1]])

# Define a function to print the PrettyTable to the console
def print_table():
    print (letters_in_input)

# Call the letters_counter function to count the letter frequencies in the user's input
letters_counter(user_input)

# Call the add_to_table function to add the letter frequencies to the PrettyTable
add_to_table()

# Call the print_table function to print the PrettyTable to the console
print_table()
