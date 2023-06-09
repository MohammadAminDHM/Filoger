# Get text from user
text = input('please enter your text : ')

#Character counter function
def counter (txt) :

    counter = {}

    for i in text :
        if i.isalpha():
            counter[i] = counter.get(i,0) + 1

    return counter


# printer function
def printer (char_dict):

    # Determine the length of columns for table formatting
    char_width = 5
    count_width = 7

    # Print headers
    print('{:<{cw}} {:<{cw}}'.format('Char', 'Count', cw=count_width))
    print('-' * (count_width + char_width + 1)) # خط جدا کننده

    # Print data
    for char, count in char_dict.items():
        print('{:<{cw}} {:<{cw}}'.format(char, count, cw=count_width))


# Function instantiation
char_dict = counter(text)
result = printer(char_dict)

