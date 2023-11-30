class Student:
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
    
    #姓名副函式
    def setName(self,new_name):
        self.name=new_name
        
    def getName(self):
        return self.name

    #學號副函式
    def setSid(self,new_sid):
        self.sid=new_sid

    def getSid(self):
        return self.sid

    #學校副函式
    def setSchool(self,new_school):
        self.school=new_school

    def getSchool(self):
        return self.school

    #科系副函式
    def setDepartment(self,new_department):
        self.department=new_department

    def getDepartment(self):
        return self.department

    #年級副函式
    def setGrade(self,new_grade):
        self.grade=new_grade

    def getGrade(self):
        return self.grade

    #系主任姓名副函式
    def setChair_name(self,new_chair_name):
        self.chair_name=new_chair_name

    def getChair_name(self):
        return self.chair_name

    #學分數副函式
    def setCredit(self,new_credit):
        self.credit=new_credit

    def getCredit(self):
       return self.credit

    #GPA副函式
    def setGPA(self,new_GPA):
        self.GPA=new_GPA

    def getGPA(self):
       return self.GPA

    #學校地址副函式
    def setSchool_address(self,new_school_address):
        self.school_address=new_school_address

    def getSchool_address(self):
        return self.school_address

    #個人地址副函式
    def setBody_address(self,new_body_address):
        self.body_address=new_body_address

    def getBody_address(self):
        return self.body_address


student1=Student("黃楷婷","4B0G0129","南臺科技大學","資訊工程系","三年級","洪國鈞","23","3.99"," 台南市永康區南台街一號"," 台南市永康區南台街54號")  
print("姓名:{}".format(student1.getName()))
print("學號:{}".format(student1.getSid()))
print("學校:{}".format(student1.getSchool()))
print("科系:{}".format(student1.getDepartment()))
print("年級:{}".format(student1.getGrade()))
print("系主任:{}".format(student1.getChair_name()))
print("已取得學分數:{}".format(student1.getCredit()))
print("GPA:{}".format(student1.getGPA()))
print("學校地址:{}".format(student1.getSchool_address()))
print("個人地址:{}".format(student1.getBody_address()))