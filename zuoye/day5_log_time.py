import time

# 再将成格式化的时间转化成时间撮
def strToTimestamp(time_st,format='%Y-%m-%d'):
    t = time.strptime(time_st, format)  # 把格式化好的时间转成时间元组
    res = time.mktime(t)  # 时间元组转成时间戳
    return res

# 再将时间撮转化成格式化的日期
def timestmapToStr(time_stramp,format='%Y-%m-%d'):
    cur_time = time.localtime(time_stramp) #时间撮转成时间元祖
    res = time.strftime(format, cur_time) #在把时间元祖转成格式化好的时间
    return res

def JianTian(time,day):
    res = time - day * 86400 # 一天的时间撮为86400
    return res