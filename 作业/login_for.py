b = False
for i in range(3):
    username = input('输入用户名')
    password = input('输入密码')
    if username =='yeml'and password== '123456':
       print(username+'欢迎登录')
       b=True
       break
    elif username.strip() ==''or password.strip()=='':
        print('输入的用户名或密码不能为空')
    else:
        print('输入的账号密码不正确')
if not b :
    print('连续登录失败3次，请半小时后再尝试登录')

# 作业用非空即真来实现：
for i in range(3):
    username=input('输入用户名').strip()
    password=input('输入密码').strip()
    if username and password: # 非空即真，不是空的，那么就继续进行判断用户或密码是否正确，否则，提示账号密码为空
        if username=='yeml' and password=='123456':
            print('登录成功！！！')
            break
        else:
            print('用户或密码不对')
    else:
        print('输入的用户名或密码为空')
else:
    print('输入的错误次数太多了！！！')