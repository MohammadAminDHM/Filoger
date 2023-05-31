import prettytable as pt
text = input("Enter the English text: ")
table = pt.PrettyTable(["Name", "Frequency"])
table.add_rows([(ch, text.replace(' ', '').count(ch)) for ch in set(text) if ch != ' '])\
    ;table.hrules = True;print(table)