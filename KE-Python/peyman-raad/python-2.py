
from prettytable import PrettyTable
user_input = input("Please enter an English text: ")
table = PrettyTable(["NAME", "FREQUENCY"])
[table.add_row([char, user_input.count(char)]) for char in set(user_input) if char != ' ']
print(table)