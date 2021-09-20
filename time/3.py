# 获得当前时间时间戳
import time

# now = int(time.time())

now = round(time.time() * 1000)
print(now)
# 转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
timeArray = time.localtime(now)
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S.%f", timeArray)
print(otherStyleTime)
print(timeArray)
