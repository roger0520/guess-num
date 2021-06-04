#   產生一個隨機整數1~100
#   讓使用者重複輸入數字去猜
#   猜對的話 印出 "終於猜對了"
#   猜錯的話 要告訴他 比答案大或是小

import random
start = input('請輸入隨機數字開始值:')
end = input('請輸入隨機數字結束值:')
start = int(start)
end = int(end)
r = random.randint(start,end)
count = 0
while True :
    num = input('請猜數字: ')
    num = int(num)
    if num == r :
        print('你猜中了')
        count += 1
        break
    else :
        if num < r:
            print('比答案小')
            count += 1  #count = count + 1
        else :
            print('比答案大')
            count += 1 
    print('這是你猜的第', count, '次')

print('你總共猜了', count, '次')

