import csv

def main():

    file='C:/Users/Zero/Desktop/20231102.csv'

    with open(file, newline='') as csvfile:

  # 讀取 CSV 檔案內容
        rows = csv.reader(csvfile)

        score_name = []

  # 以迴圈輸出每一列
        for row in rows:
            print(row)

if __name__=="__main__":
    main()