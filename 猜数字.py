
import random
random_num = random.randint(1,1000)
count =0
while count <7:
    count +=1
    num = int(input('请输入数字：'))
    if num > random_num:
        print('你猜的太大了')
        continue
    elif num < random_num:
        print('你猜的太小了')
        continue
    else:
        print('恭喜你猜对了')

