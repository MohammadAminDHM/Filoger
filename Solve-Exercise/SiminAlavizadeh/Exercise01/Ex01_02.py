#please use python 3.8 

#Import the required libraries
from prettytable import PrettyTable 
from collections import Counter
#import string

# using ':=' operation (known as the walrus operator) which is introduced in Python 3.8
(table := PrettyTable(["NAME", "FREQUENCY"])).add_rows(Counter(filter(lambda char: not char.isspace() and char.isascii(), input("Please enter an English text: "))).items())
print(table)
