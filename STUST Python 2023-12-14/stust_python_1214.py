class Student:
    def __init__(self,name,sid,major):
        #姓名 學號 科系
        self.name=name
        self.sid=sid
        self.major=major
        self.courses = []  # 儲存修課項目的列表
    
    #查詢修課項目
    @property
    def Course(self):
        return self.courses
    #加課
    def Add_Selection(self,course):
        self.courses.append(course)
        print(f"{self.name}已成功加選課程：{course}")
    #退選
    def Withdraw(self,course):  
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name}已成功退選課程：{course}")
        else:
            print(f"{self.name}並未選修此課程：{course}")



if __name__=="__main__":
    student1 = Student("KK", "S0001", "資訊工程系")
    student2 = Student("Pair","S101","資訊工程系")

    student1.Add_Selection("機率與統計")
    student1.Add_Selection("軟體工程")
    student1.Add_Selection("演算法")

    student2.Add_Selection("Python")
    student2.Add_Selection("人工智慧概論")
    student2.Add_Selection("作業系統")

    print(f"{student1.name}修習的課程有：{student1.Course}\n")

    student1.Withdraw("機率與統計")
    print(f"{student1.name}修習的課程有：{student1.Course}\n")

    print(f"{student2.name}修習的課程有：{student2.Course}\n")

    student1.Withdraw("機率與統計")
    print(f"{student2.name}修習的課程有：{student2.Course}\n")

