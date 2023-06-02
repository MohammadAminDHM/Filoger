class TextCounter:

    def NumberOfCharacters(self,text): 
        char_count = {}
        for char in text:
            if char in char_count:
                char_count[char] += 1 
            else: 
                char_count[char] = 1

        return char_count


    def table (self,data):
        MaxKeyLenght = len("Name")
        MaxValueLenght = len("Frequency")
        HorizentalLine = '+' + '-' * (MaxKeyLenght + 2) + '+' + '-' * ( MaxValueLenght + 2) + '+'
        print(HorizentalLine)
        print(f'| {"Name":^{MaxKeyLenght}} | {"Frequency":^{MaxValueLenght}} |')
        print('+' + '=' * (MaxKeyLenght + 2) + '+' + '=' * (MaxValueLenght+2) +'+')
        for key , value in data.items():
            print(f'| {key :^{MaxKeyLenght}} | {value :^{MaxValueLenght}} |')
            print(HorizentalLine)

text_counter = TextCounter()  
Text = input('please enter your text:')
text = Text.replace(" ","")
char_count = text_counter.NumberOfCharacters(text)
text_counter.table(char_count)
