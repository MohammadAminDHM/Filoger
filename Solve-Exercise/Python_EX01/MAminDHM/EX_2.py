from tabulate import tabulate
from collections import Counter 
print(tabulate(Counter(input("Enter Your Text : \n").replace(" ", ""))\
    .items(), headers=["Name", "Frequency"], tablefmt="pretty", numalign='center', stralign='center'))
