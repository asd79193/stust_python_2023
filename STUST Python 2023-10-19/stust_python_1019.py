'''
解題想法:
1.抓取句子並且消除句子中的符號
2.使用單詞和單詞中間的空白進行分割
3.進行排序將相同的單詞都排列到一起
    進行排序要按照a~z的方式下去排序
4.進行次數計算:
    先設定一個null的變數
    再將單詞初始次數設為1
    使用for迴圈將所有單詞都跑一次
    null的變數初始為空 所以將第一個單詞放入
    如果下一個單詞和前一個單詞是一樣的 單詞次數就+1
    當下一個單詞和前一個單詞不一樣了 就輸出
    變數的單詞需要替換成不一樣的那一個
    單詞的次數 因為計算結束所以需要回歸初始
    如果沒有重複 迴圈結束就直接輸出


問題解決:
1.消除逗號&句號
    .replace(",", "").replace(".", "")
    https://coin028.com/python/python-string-remove-punctuation/
2.使用空白分割
    .split()
    https://www.geeksforgeeks.org/python-spilt-a-sentence-into-list-of-words/
3.排序
    sorted()
    https://www.freecodecamp.org/chinese/news/python-sort-how-to-sort-a-list-in-python/
4.按照a~z的方式下去排序
    str.lower
    https://badgameshow.com/steven/python/python-string-lower-upper/

5.設一個變數為null
    在C++是使用NULL，Python是使用None
    https://blog.csdn.net/lemonbit/article/details/127218869
6.輸出時首字母要是大寫
    .title()
    https://www.delftstack.com/zh-tw/howto/python/python-capitalize-first-letter/#%e5%9c%a8-python-%e4%b8%ad%e4%bd%bf%e7%94%a8-title-%e6%96%b9%e6%b3%95%e5%a4%a7%e5%af%ab%e5%ad%97%e4%b8%b2%e7%9a%84%e7%ac%ac%e4%b8%80%e5%80%8b%e5%ad%97%e6%af%8d
'''



#切割句子並排序
def splitSentence(sentence):
    #.replace(",", "").replace(".", "")消除逗號&句號
    remove_symbols=sentence.replace(",", "").replace(".", "")
    #.split()使用空白分割
    word_list = remove_symbols.split()
    #sorted()排序 str.lower將每個字母轉成小寫進行排序
    sorted_word_list = sorted(word_list,key=str.lower)
    return sorted_word_list



#計算單詞數量
def countWord(sorted_word_list):
    #設變數為null(在python的用法是none)
    forward_word = None
    #單詞的初始次數
    count = 1
    #單詞迴圈 比較單詞是否相同如果相同 單詞次數+1
    for word in sorted_word_list:
        if forward_word is None:
            forward_word = word
        elif word == forward_word:
            count += 1
        else:
            #.title()將首字母轉成大寫字母
            print("{} {}".format(forward_word.title(),count))
            forward_word = word
            count = 1
    print("{} {}".format(forward_word.title(),count))


def main():
    #要傳入的句子
    sentence="This is an example sentence. It contains some example words, and example words are good to use."
    #排列後的文字存到sorted_words 
    sorted_words = splitSentence(sentence)
    #將sorted_words丟入計算函式
    countWord(sorted_words)


if __name__=="__main__":
    main()



