# گرفتن ورودی از کاربر
text = input("Please Enter Text: ")
char_count = {}   

# شمارش تعداد کاراکترها بدون در نظر گرفتن فاصله
for char in text:
    if char != " ":
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

# چاپ جدول و چاپ کاراکترها و تعداد هرکدام از آنها
print("+-------+----------+")
print("| name  | frequency|")
print("+-------+----------+")
for char, count in char_count.items():
    print("| {:<5} | {:<8} |".format(char, count))
    print("+-------+----------+")

# برنامهای بنویسید که یک متن انگلیسی را از کاربر دریافت کند و تعداد تکرار هر کدام از
# کاراکترهای آن متن بجز فاصله را در یک جدول چاپ نماید.