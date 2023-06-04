text = input("Enter a text: ").replace(" ", "")
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

      
print(f"{'+-------+------------+'}\n| NAME\t| FREQUENCY  |\n{'+=======+============+'}")
for key, val in freq.items():
  print(f"|{' '*3}{key}\t|{' '*5}{val}\t{' '*5}|")
  print("+" + "-"*7 + "+" + "-"*12 + "+")