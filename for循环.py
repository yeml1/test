import random
random_num = random.randint(1,1000)
print(random_num)
for i in range(10):
    num = int(input('请输入数字：'))
    if num > random_num:
        print('你猜的太大了')
        continue
    elif num < random_num:
        print('你猜的太小了')
        continue
    else:
        print('恭喜你猜对了')
