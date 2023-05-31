s=input('Please enter your text:')

hd=['name','frequency']
tbl = [[i, str(s.count(i))] for i in set(s) if ('a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9')]

# maximum chars of different columns is calculated here.
# in order to find the widths we need the transpose of the table which is obtained by zip(hd, *tbl)

col_widths = [max(len(str(item)) for item in col) for col in zip(hd, *tbl)]

# above the header. width in each column is added by two(because of '+' charachters)
print("+" + "+".join("-" * (width + 2) for width in col_widths) + "+")

# header. In this example the header is: "| name | frequency |"
print("|" + "|".join(header.center(width + 2) for header, width in zip(hd, col_widths)) + "|")

#under the header.
print("+" + "+".join("=" * (width + 2) for width in col_widths) + "+")

# Print the tbl rows
for row in tbl:
    print( "|"+"|".join(str(item).center(width + 2) for item, width in zip(row, col_widths)) + "|")

# Print the bottom border
print("+" + "+".join("-" * (width + 2) for width in col_widths) + "+")


