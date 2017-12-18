
# if else
# if 、else后面必须加冒号,有冒号后一行必须是缩进的
username =input('输入你的用户名')
passwad =input('输入你的密码')
if username =='niuhanyang' and passwad =='123456':
    print('登录成功！！！')
else:
    print('账号或密码错误！！')
# input 接受到的都是str类型的,如果输入int类型，需要强制转换
score =input('请输入你的分数:')
score = int(score)
if score <60:
    print("不及格")
elif score >=60 and score <80:
    print('及格')
elif score >80 and score <90:
    print('优秀')
else:
    print('优秀')

# x先在代码前点击，设置断点，然后右键debug来调试，可以查看每一步的处理逻辑

# or 的用法
sex =input('请输入你的性别：')
if sex =='男' or sex =='女':
    print('ok')
else:
    print('泰国人妖？？')