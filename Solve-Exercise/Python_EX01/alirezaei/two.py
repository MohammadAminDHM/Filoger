import collections , tabulate , string
text = input('please enter your text : ')
char_count = collections.Counter(char for char in text if char.isalpha())
print(tabulate.tabulate([(word, count) for word, count in char_count.items()], headers=['Name', 'Frequency'], tablefmt='fancy_grid'))


