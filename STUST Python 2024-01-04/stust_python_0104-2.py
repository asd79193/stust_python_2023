#題目2

#南台飲料店子類別-員工
#要有六個副函式：顯示名字、顯示年資、顯示工時、計算月薪、增加工時、增加年資
class Employee:
        #建構子-姓名、年資、工時
        def __init__(self, name, seniority, work_hours):
            self.name = name
            self.seniority = seniority
            self.work_hours = work_hours

        #顯示員工姓名
        def query_name(self):
            return f"員工姓名：{self.name}"

        #顯示員工姓名
        def query_seniority(self):
            return f"員工年資：{self.seniority}"

        #顯示工作時數
        def query_work_hours(self):
            return f"工作時數：{self.work_hours}"

        #月薪計算，時薪為：182 計算公式：時薪＊工時
        def calculate_monthly_salary(self):
            hourly_wage = 182
            return f"月薪：{hourly_wage * self.work_hours}"

        #增加工時＝原本工時+要增加的工時
        def increase_work_hours(self, additional_hours):
            self.work_hours += additional_hours
            return f"增加工時：{additional_hours} 小時"

        #增加年資＝原本年資+新增年資
        def increase_seniority(self, additional_years):
            self.seniority += additional_years
            return f"增加年資：{additional_years} 年"

        #顯示呼叫員工的清單
        def display_employee_info(employee):
            print(employee.query_name())
            print(employee.query_seniority())
            print(employee.query_work_hours())
            print(employee.calculate_monthly_salary())
            print("\n")


#父類別-飲料
class Beverage:
        #屬性:品名、價格、冰量、甜度
        def __init__(self, name, price, ice_amount, sweetness):
            self.name = name
            self.price = price
            self.ice_amount = ice_amount
            self.sweetness = sweetness

#飲料子類別-冷飲
class ColdBeverage(Beverage):
        def __init__(self, name, price, ice_amount, sweetness):
            super().__init__(name, price, ice_amount, sweetness)
        
        def display_info(self):
            return f"{self.name}, 價格：{self.price}元, 冰量：{self.ice_amount}, 甜度：{self.sweetness}"

#飲料子類別-熱飲
class HotBeverage(Beverage):
        def __init__(self, name, price, sweetness):
            super().__init__(name, price, None, sweetness)
        
        def display_info(self):
            return f"{self.name}, 價格：{self.price}元, 甜度：{self.sweetness}"


def main():
    #3個員工物件
    employee_1 = Employee("天天", 3, 160)
    employee_2 = Employee("大雄", 1, 180)
    employee_3 = Employee("CoCo", 2, 150)

    #呼叫員工副函式
    Employee.display_employee_info(employee_1)
    employee_1.increase_work_hours(10)
    employee_1.increase_seniority(1)
    Employee.display_employee_info(employee_1)

    Employee.display_employee_info(employee_2)
    employee_2.increase_work_hours(10)
    employee_2.increase_seniority(1)
    Employee.display_employee_info(employee_2)

    Employee.display_employee_info(employee_3)
    employee_3.increase_work_hours(10)
    employee_3.increase_seniority(1)
    Employee.display_employee_info(employee_3)


    #3個飲料物件
    drinks = [ColdBeverage("綠茶", 30, "多冰", "無糖"), HotBeverage("奶茶", 40, "全糖"), ColdBeverage("紅茶", 25, "少冰", "半糖")]

    #判斷是冷飲還是熱飲
    for drink in drinks:
        if isinstance(drink, ColdBeverage):
            print("冷飲:")
        elif isinstance(drink, HotBeverage):
            print("熱飲:")
        print(drink.display_info())


if __name__ == '__main__':
    main()
