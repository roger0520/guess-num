#   產生一個隨機整數1~100
#   讓使用者重複輸入數字去猜
#   猜對的話 印出 "終於猜對了"
#   猜錯的話 要告訴他 比答案大或是小

import random

r = random.randint(1,100)

while True :
    num = input('請猜數字: ')
    num = int(num)
    if num == r :
        print('你猜中了')
        break
    else :
        if num < r:
            print('比答案小')
        else :
            print('比答案大')



