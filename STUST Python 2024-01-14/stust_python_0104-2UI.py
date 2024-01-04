from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys

class Employee:
    def __init__(self, name, seniority, work_hours):
        self.name = name
        self.seniority = seniority
        self.work_hours = work_hours

    def query_name(self):
        return f"員工姓名：{self.name}"
    
    def query_seniority(self):
        return f"員工年資：{self.seniority}"
    
    def query_work_hours(self):
        return f"工作時數：{self.work_hours}"

    def calculate_monthly_salary(self):
        hourly_wage = 182
        return f"月薪：{hourly_wage * self.work_hours}"
    
    def increase_work_hours(self, additional_hours):
        self.work_hours += additional_hours
        return f"增加工時：{additional_hours} 小時"

    def increase_seniority(self, additional_years):
        self.seniority += additional_years
        return f"增加年資：{additional_years} 年"


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("南台飲料店")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()

        employee_button = QPushButton("員工")
        employee_button.clicked.connect(self.display_employee_info)
        self.main_layout.addWidget(employee_button)

        self.central_widget.setLayout(self.main_layout)

        self.employee_1 = Employee("天天", 3, 160)
        self.employee_2 = Employee("大雄", 1, 180)
        self.employee_3 = Employee("CoCo", 2, 150)

    def display_employee_info(self):
        info = ""
        for employee in [self.employee_1, self.employee_2, self.employee_3]:
            info += employee.query_name() + "\n"
            info += employee.query_seniority() + "\n"
            info += employee.query_work_hours() + "\n\n"
        self.show_info(info)

    def show_info(self, text):
        central_widget = QWidget()
        layout = QVBoxLayout()

        info_label = QLabel(text)
        layout.addWidget(info_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.add_return_button()

    def add_return_button(self):
        return_button = QPushButton("返回")
        return_button.clicked.connect(self.return_to_main)
        self.main_layout.addWidget(return_button)

    def return_to_main(self):
        self.setCentralWidget(self.central_widget)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
