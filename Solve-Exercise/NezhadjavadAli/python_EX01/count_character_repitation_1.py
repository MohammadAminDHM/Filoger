text = input("Enter the English text: ")
table = {ch: text.count(ch) for ch in set(text) if ch != ' '}
print("+" + "-" * 9 + "+" + "-" * 11 + "+\n|" + " Name".center(8) + " |" + " Frequency".center(10) + " |\n+" + "-" * 9 + "+" + "-" * 11 + "+\n" + "\n".join([f"| {str(name).center(6)}  | {str(frequency).center(10)}|\n+" + "-" * 9 + "+" + "-" * 11 + "+" for name, frequency in table.items()]))


