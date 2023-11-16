def recursion(n):
    
    #當n=1或者0的時候會返回1，否則減一，進行階層計算
    return 1 if (n == 1 or n == 0) else n * recursion(n - 1)
    

def main():

   #使用者輸入字串轉整數
   number=int(input())
   #呼叫遞迴函數
   recursion(number)
   print(recursion(number))

if __name__=="__main__":
    main()