
# 循环（就是重复去干）、迭代、遍历
# for 循环
#  while 循环

# while 循环，必须先有一个计数器
# continue 结束本次循环，继续下一次循环
# break 结束循环，遇到break立即马上停止
# count =0
# while count < 10:
#     print('啊哈哈哈哈')
#     count =count +1
#     continue
#     print('count',count)
# count+=1 与 count =count +1---count-=1 与count =count +1---count*=1与count =count *1 是一样的

# continue 结束本次循环，继续下一次循环.continue后面的代码不再执行
# break 结束循环
count1 =0
while count1<3:
    username =input('输入你的账号')
    pwd =input('输入你的密码')
    if username =='niuhanyang' and pwd =='123456':
        print('登录成功!!!')
        break
    else:
        print('账号密码错误')
    count1+=1
else:
    print('输入错误次数过多，明天在试')

