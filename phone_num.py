import string
import random
first=1
f=open("d:/1.txt",'w')
num = int(input('请输入要生成电话号码的条数是：'))
for i in range(num):
    start = str(first) + ''.join(random.sample(string.digits, 2))
    end = ''.join(random.sample(string.digits, 8))
    phonenum = start + end
    f.writelines(phonenum+'\n')
    print('电话号码是：'+phonenum)
print('电话号码存放的路径：d:/1.txt')
f.close()
