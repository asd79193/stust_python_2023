def repeat(str1):
    #刪除重複元素
    ss=(list(set(str1)))
    #排序
    ss.sort()
    print(ss)

def main():
    str=input()
    #用逗號分割
    str1=str.split(',')
    repeat(str1)

if __name__=="__main__":
    main()