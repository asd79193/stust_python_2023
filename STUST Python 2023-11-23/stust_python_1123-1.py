class Pet :

    def __init__(self,variety,bloodline,gender,age,character):
        self.variety=variety
        self.bloodline=bloodline
        self.gender=gender
        self.age=age
        self.character=character
    
    def Print_cat(self):
        print("品種:{}\n血統:{}\n性別:{}\n年齡:{}\n性格:{}\n".format(self.variety,self.bloodline,self.gender,self.age,self.character))


pet1=Pet("緬因貓","純血","girl","3個月","活潑")
pet2=Pet("曼赤肯","混血","boy","2個月","親人")

pet1.Print_cat()
pet2.Print_cat()
"""
def main():
    print("Hello World")


if __name__=="__main__":
    main()
"""