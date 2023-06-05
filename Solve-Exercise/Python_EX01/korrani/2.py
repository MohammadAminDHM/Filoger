import collections,prettytable
t=prettytable.PrettyTable(['NAME', 'FREQUENCY'])
for key, val in dict(collections.Counter(sorted((input("\nPlease Enter Your Text: ").lower()).replace(" ","")))).items(): t.add_row([key, val])
print(t)