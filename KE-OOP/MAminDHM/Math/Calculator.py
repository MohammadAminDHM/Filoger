class Calculator:
    """if you want use complex
    write like that :
    'x+iy'"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x1 = 0
        self.x2 = 0
        self.y1 = 0
        self.y2 = 0        
        
    def __str__(self):
        return f"x: {self.x}, y: {self.y}"
    def __len__(self):
        return self.x
    def add(self):
        return self.x + self.y
    def subtract(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y


class Complex(Calculator):
    def set_numbers(self):
        if type(self.x) != str or type(self.y) != str:
            print('write your number to string')
        else:
            # 100+300i
            self.x1 = float(self.x.split('+')[0])
            self.y1 = float(self.x.split('+')[1][:-1])
            self.x2 = float(self.y.split('+')[0])
            self.y2 = float(self.y.split('+')[1][:-1])
    def add_complex(self):
        self.set_numbers()
        return "{} + {}i".format(self.x1 + self.x2, self.y1 + self.y2)