import datetime

# dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
dt_ms = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')  # 含微秒的日期时间，来源 比特量化
# print(dt)
print(type(dt_ms))
int(dt_ms)
print(type(dt_ms))