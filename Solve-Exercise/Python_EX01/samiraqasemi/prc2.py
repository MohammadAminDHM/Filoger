# گرفتن ورودی از کاربر و چاپ جدول با استفاده از کتابخانه
from tabulate import tabulate  
from collections import Counter  
print(tabulate([[char, count] for char, count in Counter(input("Please Enter Text: ").replace(" ","")).items()], headers=["name", "frequency"], tablefmt="grid"))
# کشیدن جدول شمارش کاراکترها با کمترین خط کد ممکن