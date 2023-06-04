from prettytable import PrettyTable
from collections import Counter
table = PrettyTable(['Name', 'Frequency'])
[table.add_row([k, v]) for k, v in Counter(input("Enter Your Text: ").replace(" ", "")).items()] ; print(table)