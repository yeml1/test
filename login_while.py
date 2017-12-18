

count=0
while count< 3:
    username = input('输入用户名')
    password = input('输入密码')
    count+=1
    if username =='yeml'and password== '123456':
       print(username+'欢迎登录')
       break
    elif username.strip() ==''or password.strip()=='':
        print('输入的用户名或密码不能为空')
    else:
        print('输入的账号密码不正确')
else:
    print('连续登录失败3次，请半小时后再尝试登录')



