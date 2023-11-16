
#一次註解 使用'''
'''

註解內容

'''

#使用模組
import math

#輸出文字
def printString():
    print("Good Night")

def HelloWorld():
    print("Hello World!")

#傳入文字 
# 方法有兩種 1.是直接在主涵式先宣告再呼叫副涵式 2.直接打在主涵式的括號中傳入並印出
def printText(input_text):
    print(input_text)

#計算字串長度 加入字串
#python中加入字串可使用"+"的符號
#計算字串長度 可使用語法len()進行計算 此語法不用導入模組
def sayHellToSomeone(name):
    print("Hello,"+ name)
    print("length of name=",len(name))

# 語法type()告訴我們型態 abs()取絕對值
#.format會將值放入{} 一定要互相匹配 否則會錯誤 沒有指定位置案默認順序傳入 {}大括號的用法相當於C語言的%
def MathFunction():
    print(abs(-300))
    integer=-20
    print('Absolute value of -20 is:',abs(integer))
    print('Type of value:',type(integer))
    print('Absolute value of -20 is: {} and Type of varable is {}'.format(abs(integer),type(integer)))

    floating=-30.33
    print('Absolute value of -30.33 is:',abs(floating))
    print('Type of value:',type(floating))

#for迴圈使用
#in後面是條件 i會先=1再=2最後=3
def Squareresult():
    for i in [1,2,3]:
        result=Square(i)
        print("square of {} = {}".format(i,result))

#平方
def Square(num):
    return num*num

#主函式
def main():
    HelloWorld()
    printString()
    #input_text="How are you?"
    #printText(input_text)
    printText("How are you?")
    sayHellToSomeone("Katty")
    MathFunction()
    Squareresult()
if __name__=="__main__":
    main()