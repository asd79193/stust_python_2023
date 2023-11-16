#人的類別
class Person:

    #name age address
     def __init__(self, name, age, address):

        self.__name = name
        self.__age = age
        self.__address = address
    
     def out(self):

        print(f"姓名:{self.__name} 年齡:{self.__age} 地址:{self.__address}")

class Student(Person):

    #student_ID major
    def __init__(self, name, age, address,student_ID, major):

        #調用Person的建構子
        super().__init__(name,age,address)
        self.__student_ID=student_ID
        self.__major=major

    def out(self):

        #呼叫Person類別
        super().out()

        print(f"學號:{self.__student_ID} 專業:{self.__major}")


def main():

    student=Student("張三",22,"南台街1號","4adl009","資訊工程系")
    student.out()

if __name__=="__main__":
    main()