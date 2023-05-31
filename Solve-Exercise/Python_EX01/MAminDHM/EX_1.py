# Intput Sentence
sentence = input("Enter Your Sentence : \n")

# Drop Space
sentence = sentence.replace(" ", "")

# Count Of Letters
specific_letter = set(sentence)
result = {'Name': [], 'Frequency': []}

for letter in specific_letter:
    count = 0
    for character in sentence:
        if character==letter:
            count+=1
    result["Name"].append(letter)
    result["Frequency"].append(count)

# Show Result in Table

## Get column
columns = list(result.keys())

## Print header
print('+' + 8 * '-' + '+' + 13 * '-' + '+')
print(f"|  {columns[0]:^5} |  {columns[1]:^10} |")
print('+' + 8 * '=' + '+' + 13 * '=' + '+')

## Print Data
for name, frequency in zip(*result.values()): # type: ignore
    print(f"|   {name:^2}   |     {frequency:^4}    |")
    print('+' + 8 * '-' + '+' + 13 * '-' + '+')