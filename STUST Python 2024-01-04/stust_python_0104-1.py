#題目1
class FriedChicken:

    #屬性：名稱、食材、價格、烹飪時間、熱量、辣度
    def __init__(self,name,ingredients,money,time,heat,spiciness):
        self.name=name
        self.ingredients=ingredients
        self.money=money
        self.time=time
        self.heat=heat
        self.spiciness = spiciness

    # 計算總熱量
    def calculate_total_heat(self):
        total_heat = self.heat
        return total_heat
    
    # 更新價格
    def update_price(self, new_price):
        self.money = new_price

    # 辣度
    def display_spiciness(self):
        print(f"辣度選擇：{self.spiciness}")
    
    # 顯示炸雞的明細
    def display_info(self):
        print(f"炸雞品項：{self.name}")
        print(f"食材：{', '.join(self.ingredients)}")
        print(f"價格：{self.money}")
        print(f"烹飪時間：{self.time} 分鐘")
        print(f"熱量：{self.calculate_total_heat()} 卡路里")
        print("\n")

def main():
    # 4個炸雞物件
    test1 = FriedChicken("炸雞腿", ["雞腿", "麵粉", "蛋液", "香料"], 60, 30, 500, "中辣")
    test2 = FriedChicken("香酥雞", ["雞肉", "麵粉", "酥粉", "香料"], 50, 25, 450, "微辣")
    test3 = FriedChicken("炸雞翅", ["雞翅", "麵粉", "蛋液", "香料"], 30, 35, 550, "辣")
    test4 = FriedChicken("雞排", ["雞胸", "麵粉", "麵包糠", "香料"], 80, 28, 480, "不辣")

    # 呼叫炸雞副函式
    test1.display_info()
    test1.display_spiciness()
    test1.update_price(70)
    test1.display_info()
    print("\n")

    test2.display_info()
    test2.display_spiciness()
    test2.update_price(60)
    test2.display_info()
    print("\n")


    test3.display_info()
    test3.display_spiciness()
    test3.update_price(45)
    test3.display_info()
    print("\n")

    test4.display_info()
    test4.display_spiciness()
    test4.update_price(95)
    test4.display_info()
    print("\n")


if __name__ == '__main__':
    main()