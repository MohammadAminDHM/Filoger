# Define a function to count the number of occurrences of each character in a string
def counts_char(txt):
    # Create an empty dictionary to store the character counts
    chars = {}
    
    # Loop through each character in the input string
    for char in txt:
        # Ignore spaces
        if char != ' ':
            # If the character already exists in the dictionary, increment its count
            if char in chars:
                chars[char] += 1
            # Otherwise, add the character to the dictionary and set its count to 1
            else:
                chars[char] = 1
    
    # Return the dictionary containing the character counts
    return chars

# Prompt the user to enter a text string
user_input = input("Please enter an English text: ")

# Call the counts_char function to count the characters in the user's input
character_counts = counts_char(user_input)

# Print a formatted table showing the character counts
print("+-------+-----------+")
print("| NAME  | FREQUENCY |")
print("+=======+===========+")
for char, count in character_counts.items():
    print(f"|{char}\t| {count:9d} |")
    print("+-------+-----------+")
