# Input Sentence
sentence = input("Enter Your Sentence : \n")

# Drop Space
sentence = sentence.replace(" ", "")

# Count Of Letters
result = {}
for letter in sentence:
    if letter not in result:
        result[letter] = 1
    else:
        result[letter] += 1

# Show Result in Table

## Get column
columns = ['Name', 'Frequency']

## Print header
print('+' + 8 * '-' + '+' + 13 * '-' + '+')
print(f"|  {columns[0]:^5} |  {columns[1]:^10} |")
print('+' + 8 * '=' + '+' + 13 * '=' + '+')

## Print Data
for name, frequency in result.items():
    print(f"|   {name:^2}   |     {frequency:^4}    |")
    print('+' + 8 * '-' + '+' + 13 * '-' + '+')
