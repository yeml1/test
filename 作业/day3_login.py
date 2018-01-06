f = open('d:\\user.txt', 'a+', encoding='utf-8')  # 打开文件
all_user = {}
f.seek(0)
a = f.read()  # 读取文件中的值
if a:  # 为空的时候，不转化
 all_user = eval(a)  # 将字符串强制转化为字典格式，并保存在字典中
username = input('输入用户名:').strip()
pwd = input('输入密码:').strip()
if username and pwd:
    if username in all_user:
        scr_pwd = all_user[username]  # 获取密码
        if scr_pwd == pwd:
            print('登录成功')
        else:
            print('密码不正确')
    else:
        print('用户名不存在')
else:
    print('用户名或密码不能为空')
f.close()  # 关闭文件
