class Student:
    '''
    def __init__(self,name,sid,school,department,grade,chair_name,credit,GPA,school_address,body_address):
        #姓名 學號 學校 科系 年級 系主任姓名 學分數 GPA 學校地址 個人地址 
        self.name=name
        self.sid=sid
        self.school=school
        self.department=department
        self.grade=grade
        self.chair_name=chair_name
        self.credit=credit
        self.GPA=GPA
        self.school_address=school_address
        self.body_address=body_address
    '''

    def __init__(self,name):
        self.name=name
    
    @property
    def student_name(self):
        print(f'"{self.name}"was accessed.')
        return self.name

    @student_name.setter
    def student_name(self, value):
        print(f'"{self.name}"is now "{value}".')
        self.name = value

    @student_name.deleter
    def student_name(self):
        print(f'"{self.name}" was deleted.')
        del self.name

if __name__=="__main__":
    Student1= Student("John Doe")

    print(Student1.student_name)
    Student1.student_name="Peter Pan"
    del Student1.student_name
