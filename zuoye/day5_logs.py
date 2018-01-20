# 作业一：
#  已上传的logs
#  1、写清理日志的脚本，要去传入一个路径，只保留3天以内的日志，剩下的全部删掉 clram_log.py
#  今天是2018-01-14 那么就保存12、13、14号的，如果明天时间是15，那么就保存13/14、15的日志

import sys
import time
import os

import day5_log_time

cur_time = time.strftime('%Y-%m-%d') #获取当前日期

def clean_log(path):
    for filename in os.listdir(path): #列出一个目录下的所有文件
        b = False
        for i in range(3):
            t1 =day5_log_time.strToTimestamp(cur_time) # 再将成格式化的时间转化成时间撮
            t1 = day5_log_time.JianTian(t1,i)# 取3天以内的日期的时间撮
            d1 = day5_log_time.timestmapToStr(t1) # 再将时间撮转化成格式化的日期
            if d1 in filename: # 判断是3天以内的文件
                b = True
        if not b: # b=false,不是3天以内的日志文件
            new_path=path+'/'+filename #拼接绝对路径
            ext = os.path.splitext(new_path)[1]# 返回文件名和扩展名的数组
            if (ext=='.log') or (ext=='.txt'): # 判断如果是以log 或.txt的就删除文件
                os.remove(new_path)
                print('删除'+new_path)

# # argv 是不能左键点击运行的，直接这样运行是不会传入参数的，在linxu或Terminal 中运行可以传入参数
args=sys.argv #获取pyhton运行时传入的参数
print(args) #运行结果是一个list
if len(args)>1: # 判断是否传入了参数
    path=args[1] # 取的是list中的第二个元素，也就是传入的参数（路径）
    if os.path.isdir(path):#判断是不是目录
     clean_log(path)
    else:
        print('路径不存在')
else:
    print('运行这个python 文件需要传入一个路径')
