import string
import random
f = open('d:\\password.txt', 'a+', encoding='utf-8')  # 打开文件
all_passwds = []
num = int(input('请输入要生成密码的条数是：'))
for i in range(num):
    first = random.sample(string.digits, 1)  # 随机取1位数字
    lower = random.sample(string.ascii_lowercase, 1)  # 随机取1位小写字母
    upper = random.sample(string.ascii_uppercase, 1)  # 随机取1位大写字母
    other = random.sample(string.ascii_letters + string.digits, 5)  # 随机取5
    password=first+lower+upper+other # 拼接成8位的密码
    password = ''.join(password)+'\n' #把list中的字符串连起来组合是一个8位的密码
    all_passwds.append(password) # 添加到字典中去.
    print(all_passwds)
    f.seek(0)  # 把指针移到最前面，从头开始取值
    f.truncate()  # 清空文件
    f.writelines(all_passwds) # 读到文件中去
f.close()