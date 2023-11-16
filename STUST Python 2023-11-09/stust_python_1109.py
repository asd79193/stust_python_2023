def practise1 (name,age):
    print(name,age)
 
def practise2(*args):
    for i in args:
        print(i)
 
def practise3(a,b):
    add=a+b
    reduce=a-b
    print(add,',',reduce)
 
def practise4(name,money=9000):
    print('姓名:',name,'薪水:',money)
 
def practise5(a,b):
 
    def add(a,b):
        return a+b
 
    add1=add(a,b)+5
    return add1
   
def practise6(n):
 
    return 1 if (n == 1 or n == 0) else n + practise6(n - 1)
 
def practise7(name,age):
    print(name,age)
 
def practise8(start,last):
    print(list(range(start,last,2)))
 
def practise9(big):
    print(max(big))
 
def main():
 
    practise1('Kiki',20)
 
    practise2(20, 40, 60)
    practise2(80, 100)
   
    practise3(40,10)
 
    practise4("Ben", 12000)
    practise4("Jessa")
 
    res=practise5(5,10)
    print(res)
 
    res1=practise6(10)
    print(res1)
 
    practise7("Emma", 26)
    show_student=practise7
    show_student("Karry",23)
 
    practise8(4,30)
 
    x = [4, 6, 8, 24, 12, 2]
    practise9(x)
 
if __name__=="__main__":
    main()