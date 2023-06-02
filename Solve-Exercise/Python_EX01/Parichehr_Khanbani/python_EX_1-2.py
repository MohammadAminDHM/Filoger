from collections import Counter
from texttable import Texttable
table = Texttable().add_rows([["Name", "Frequency"]] + list(Counter(input("please enter a text:").replace(" " , "")).items()))
print(table.draw())