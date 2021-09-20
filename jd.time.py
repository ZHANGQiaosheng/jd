import requests
import datetime

while True:
    class Jingdongtime(object):
        r1 = requests.get(url='https://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5',
                          headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'})

        x = eval(r1.text)
        timeNum = int(x['currentTime2'])


        def funcname():
            timeStamp = float(Jingdongtime.timeNum) / 1000
            ret_datetime = datetime.datetime.utcfromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S.%f")
            return ret_datetime

    t = Jingdongtime.funcname()
    print(t)



