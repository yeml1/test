all_user = {}  # 定义空字典
f = open('d:\\user.txt', 'a+', encoding='utf-8')  # 打开文件
f.seek(0)  # 把指针移到最前面，从头开始取值
a = f.read()  # 读取文件中的值
if a:  # 为空的时候，报错，不转化
    all_user = eval(a) ## 将文件中的字符串强制转化为字典格式
while True:
    username = input('输入用户名:').strip()  # strip 去空格
    pwd = input('输入密码:').strip()
    cpwd = input('再次输入密码:').strip()
    if username and pwd and cpwd: # 非空即真
        if username in all_user:
            print('用户名已经存在，请重新输入')
        else:
            if pwd == cpwd:
                all_user[username] = pwd  # 把账户和密码以key-value 形式存到字典中
                f.seek(0)  # 把指针移到最前面，清空文件
                f.truncate()  # 清空文件
                f.writelines(str(all_user)) # 把字典写入文件中
                f.close()  # 关闭文件
                print('注册成功')
                break
            else:
                print('两次输入密码不一致，请重新输入')
    else:
        print('用户或密码不能为空')