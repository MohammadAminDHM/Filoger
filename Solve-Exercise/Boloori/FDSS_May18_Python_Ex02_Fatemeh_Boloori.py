from tabulate import tabulate
s=input('Please enter your text:')
charList = [[i, s.count(i)] for i in set(s) if ('a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9')]
print(tabulate(charList , headers=['NAME','FREQUENCY'], tablefmt="pretty"))