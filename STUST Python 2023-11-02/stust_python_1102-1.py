def main():
    #讓使用者先進行輸入
    str=input()
    #reversed()反轉字串
    str1=(list(reversed(str)))
    #for迴圈把字串跑一次輸出，end=''不換行顯示
    for i in str1:
       print(i,end='')
    

if __name__=="__main__":
    main()