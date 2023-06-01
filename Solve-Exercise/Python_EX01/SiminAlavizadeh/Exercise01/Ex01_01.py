#Define the function get text and return the dictionary with the character counts if character is ascii and is not space
def count_characters(text):
    character_counts = {}  
    for char in text:
        if not char.isspace() and char.isascii():  
            character_counts[char] = character_counts.get(char, 0) + 1 
    return character_counts
    
def print_table(header, data):   
    # Determine the maximum length of the key and value columns including headers of the key and value given
    max_key_length =max(len(header[0]), max(len(col[0]) for col in data))
    max_value_length =max(len(header[1]), max(len(str(col[1])) for col in data))     
    #create grid and seperator line using calculated length
    l_pading = 1 
    r_pading = 3
    grid_line = ("+{}+{}+".format("-"*(max_key_length+l_pading+r_pading), "-"*(max_value_length+l_pading+r_pading)))    
    header_separator =("+{}+{}+".format("="*(max_key_length+l_pading+r_pading), "="*(max_value_length+l_pading+r_pading)))        
    #Create header line using name of headers and calculated length
    header= f"|{' '*l_pading }{header[0].ljust(max_key_length)}{' '*r_pading}|{' '*r_pading}{ header[1].rjust(max_value_length)}{' '*l_pading}|"
    # Print the separator line, header , and  header_separator line
    print(grid_line)    
    print(header)
    print(header_separator)    
    ## Iterate over each row of data as an input and print it in the table format
    for row in data:   
        print(f"|{' '*l_pading }{row[0].ljust(max_key_length)}{' '*r_pading}|{' '*r_pading}{str(row[1]).rjust(max_value_length)}{' '*l_pading}|")        
        print(grid_line)
    
    
#get input from user check not entring empty 
text ="" #input("Enter text: ")
while not text:
    text = input("Please enter an English text: ")
    
#count characters calling count_characters function
character_counts = count_characters(text)

#assign  a tuple to variable header contains columns header ffortable
header = ("NAME", "FREQUENCY")

#creates a new list of tuple of key-value pair from character_counts
data = [(key, value) for key, value in character_counts.items()]

#print formated table calling print_table function
print_table(header, data)