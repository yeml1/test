# %s(str) --是站位符，有多少个站位符就有多少变量 %d 是int类型 %f 是float类型
for i in range(10):
    username =input('请输入你的名字')
    time ='2017年12月17号 17点20分'
    print(username+'，欢迎光临'+'，时间是：'+time)
    print('%s，欢迎光临，时间是：%s'%(username,time))
    print(
       '{},欢迎光临，时间是：{}'.format(username,time)
    )
    print(
        '{name},欢迎光临，时间是：{date}'.format(name=username,date=time)
    )