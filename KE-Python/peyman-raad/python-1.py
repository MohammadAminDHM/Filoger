def counts_char(txt):
    chars = {}
    for char in txt:
        if char != ' ':
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

user_input = input("Please enter an English text: ")
character_counts = counts_char(user_input)

print("+-------+-----------+")
print("| NAME  | FREQUENCY |")
print("+=======+===========+")
for char, count in character_counts.items():
    print(f"|{char}\t| {count:9d} |")
    print("+-------+-----------+")