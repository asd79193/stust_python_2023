#程式用途:傳入一個字母陣列 判斷每個字母是不是母音 回傳不是母音的字母

#list of alphabets
#陣列
alphabets=['a','b','d','e','i','j','o']
vowel=['a','e','i','o','u']
filtered_aplphabets=[]

#define a self-defined sub-method to filter out vowels
#len 返回字符字串長度或項目個數
#if...elif...else,elif相當於c語言的else if 
#or等於c語言的||
#.append()將資料加入空列表
def filter_vowels_from_list(alphabets):
    print("length of the alphabts list={}".format(len(alphabets)))
   
    for elem in alphabets:
        if elem =='a' or elem =='e' or elem =='i' or elem =='o'or elem =='u':
            
            print("vowel:",elem)
            
        #elif elem =='e':
            
            #print("vowel:",elem)
        #elif elem =='i':
            
            #print("vowel:",elem)
        #elif elem =='o':
            
            #print("vowel:",elem)
        #elif elem =='u':
         
            #print("vowel:",elem)
        
        else:
            print("not vowel",elem)
            filtered_aplphabets.append(elem)
            
        #if elem in vowel:
            #print("vowel:",elem)
        #else:
            #print("none vowel:",elem)


#
def main():
    filter_vowels_from_list(alphabets)
    #new_list = [x for x in alphabets for y in vowel if x == y]
    #print(new_list)
    print("filtered_aplphabets=",filtered_aplphabets)
    for elem1 in filtered_aplphabets:
        print(elem1)


if __name__=="__main__":
    main()
