class MyPrettyTable:
    CharacterFrequencyDict={}
    MaxFrequencyColumnSize=0
    RowDiscriminantString=" "
    HeaderStirng=" "
    TableString=" "

    def MakeTable(self,CharacterFrequencyDict):
        #this functions find the size of columns,
        #build the lines between rows and makes the whole string which must be printed as output

        self.CharacterFrequencyDict=CharacterFrequencyDict

        self.MaxFrequencyColumnSize=self.CalculateMaxFrequencyColumnSize(self.CharacterFrequencyDict)
        self.RowDiscriminantString=self.MakeRowDiscriminantString(self.MaxFrequencyColumnSize)
        self.MakePrintString(self.RowDiscriminantString)

  

    def MakePrintString(self,RowDiscriminantString):
        #this function  makes the whole string which must be printed as output

        self.TableString = self.MakeTableHeader(RowDiscriminantString)
   
        LeftSpaceCount=RightSpacCount=0
        
        for CharacterFrequency in list(self.CharacterFrequencyDict.items()):
            LeftSpaceCount,RightSpaceCount=self.PrintStringSpaceCount(self.MaxFrequencyColumnSize,len(str(CharacterFrequency[1])))
            self.TableString+="|  "+ CharacterFrequency[0]+ "   |"+LeftSpaceCount*" "+str(CharacterFrequency[1])+RightSpaceCount*" "+"|\n"
           
        self.TableString+=self.RowDiscriminantString


    def MakeTableHeader(self,RowDiscriminantString):
        #this Function makes the header of table

        self.HeaderStirng=(RowDiscriminantString)+"\n"
        self.HeaderStirng+=(("| NAME |"+(self.MaxFrequencyColumnSize//2-3)*" "+"FREQUENCY"+(self.MaxFrequencyColumnSize//2-3)*" "+"|"))+"\n"
        self.HeaderStirng+=(RowDiscriminantString+"\n")
        return self.HeaderStirng
      
    def MakeRowDiscriminantString(self,FrequencyColumnSize):
        #This Function makes the Lines between rows of tables

        FrequencyColumnSize=max(9,FrequencyColumnSize)
        self.RowDiscriminantString=("+"  +  6 * "-"  +  "+"  + (FrequencyColumnSize+2)*"-"  +  "+")
        return self.RowDiscriminantString

    def CalculateMaxFrequencyColumnSize(self,CharacterFrequencyDict):
        #this function find the Frequncy column
        #9 is the lenghth of "FREQUENCY" word, However digits of Frenquencies may be over than 9 digits!

        Frequencies=list(CharacterFrequencyDict.values())
        return max(9, len(str(max(Frequencies))) )

    def PrintStringSpaceCount(self,ColumnSize,DigitSize):
        #this function determines the spaces needed in each Frequncy Column item for Center Indent

        LeftSpace=RightSpace=0
        LeftSpace=(ColumnSize-DigitSize)//2+(ColumnSize-DigitSize)%2+1
        RightSpace=(ColumnSize-DigitSize)//2+1
        return LeftSpace,RightSpace
       


def BuildCharacterFrequencyDict(UserText):
    #This function makes a dictionary of characters and their related Frequency in the input text

    CharacterFrequency={}
    UserText=(UserText.replace(" ","")).lower()
    UserText=sorted(UserText)

    for CurrentCharacter in UserText:
        if CurrentCharacter not in CharacterFrequency:
            CharacterFrequency[CurrentCharacter]=1
        else :
            CharacterFrequency[CurrentCharacter] += 1
    
    return CharacterFrequency


UserText=input("\nPlesae Enter Your Text: ")
Frequencies=BuildCharacterFrequencyDict(UserText) 


FrequencyTable=MyPrettyTable()
FrequencyTable.MakeTable(Frequencies)


print(FrequencyTable.TableString)
