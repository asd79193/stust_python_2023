"""
class Preson :

    #self:本身
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def __str__(self):
        return f" Name:{self.name} Age={self.age}"

    def myfunc(self):
        print("Hello my name is " + self.name)

p1=Preson("John", 36)
p2=Preson("Jennifer",25)

print(p1.name)
print(p1.age)
print(p1.myfunc())
"""


class MyShape:
    #square_side邊 length長 width寬 radius半徑
    def __init__(self,square_side,length,width,radius):
       self.square_side=square_side
       self.length=length
       self.width=width
       self.radius=radius
    
    #計算正方形面積
    def square_area(self):
        return self.square_side*self.square_side

    #計算長方形面積
    def rectangle_area(self):
        return self.length*self.width

    #計算圓形面積
    def circular_area(self):
        return self.radius*self.radius*3.14

square=MyShape(5,0,0,0)
rectangle=MyShape(0,5,3,0)
circular=MyShape(0,0,0,5)

print(square.square_area())
print(rectangle.rectangle_area())
print(circular.circular_area())
 

"""
def main():
    print("Hello World")


if __name__=="__main__":
    main()
"""