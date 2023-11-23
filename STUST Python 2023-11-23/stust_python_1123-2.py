class Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        self.hours_workedsalary = 0  # 初始化加班工資為0
    
    #使用“assign_department”方法更改員工的部門
    def assign_department(self,new_department):
        self.emp_department=new_department

    #使用“print_employee_details”方法列印員工的詳細資料
    def print_employee_details(self):
        print("ID:{}\nName:{}\nSalary:{}\nDepartment:{}\n".format(self.emp_id,self.emp_name,self.emp_salary,self.emp_department))

    #使用「calculate_emp_salary」方法需要兩個參數：工資和工作小時數，即員工的工作小時數。如果工作時間超過 50 小時
    # 此方法會計算加班時間並將其加到薪資中。加班時間計算公式如下：
    #加班 = 工作時數 – 50
    #加班金額 = (加班 * (薪資 / 50))
    def calculate_emp_salary(self,hours_worked):
        work_overtime=hours_worked-50 if hours_worked > 50 else 0

        if hours_worked>=50:
            self.hours_workedsalary=work_overtime*(self.emp_salary/50)

        self.emp_salary=self.emp_salary + self.hours_workedsalary
        

#Sample Employee Data:
#"ADAMS", "E7876", 50000, "ACCOUNTING"
#"JONES", "E7499", 45000, "RESEARCH"
#"MARTIN", "E7900", 50000, "SALES"
#"SMITH", "E7698", 55000, "OPERATIONS"

employee1=Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
employee2=Employee("JONES", "E7499", 45000, "RESEARCH")
employee3=Employee("MARTIN", "E7900", 50000, "SALES")
employee4=Employee("SMITH", "E7698", 55000, "OPERATIONS")

#測試部門是否可以更改
employee1.print_employee_details()
employee1.assign_department("RESEARCH")
employee1.print_employee_details()

#測試薪資計算
employee2.print_employee_details()
employee2.calculate_emp_salary(60)
employee2.print_employee_details()