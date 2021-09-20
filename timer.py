# -*- coding:utf-8 -*-
import time
import requests
import json

from datetime import datetime
from jd_logger import logger
from config import global_config


class Timer(object):
    def __init__(self, sleep_interval=0.5):
        # '2018-09-28 22:45:50.000'
        # buy_time = 2020-12-22 09:59:59.500
        buy_time_everyday = global_config.getRaw('config', 'buy_time').__str__()
        localtime = time.localtime(time.time())
        self.buy_time = datetime.strptime(
            localtime.tm_year.__str__() + '-' + localtime.tm_mon.__str__() + '-' + localtime.tm_mday.__str__()
            + ' ' + buy_time_everyday,
            "%Y-%m-%d %H:%M:%S.%f")
        self.buy_time_ms = int(time.mktime(self.buy_time.timetuple()) * 1000.0 + self.buy_time.microsecond / 1000)
        # print("buy_time_ms:", self.buy_time_ms)
        self.sleep_interval = sleep_interval
        # print(self.sleep_interval)

        self.diff_time = self.local_jd_time_diff()
        # print("diff_time", self.diff_time)

    def jd_time(self):
        """
        从京东服务器获取时间戳毫秒
        :return:
        """
        r1 = requests.get(url='https://api.m.jd.com/client.action?functionId=queryMaterialProducts&client=wh5',
                          headers={
                              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'})

        x = eval(r1.text)
        timeNum = int(x['currentTime2'])
        timeStamp = float(timeNum) / 1000
        # ret_datetime = datetime.utcfromtimestamp(timeStamp).strftime("%Y-%m-%d %H:%M:%S.%f")
        print("京东服务器的时间戳：", timeStamp)
        return timeStamp

    def local_time(self):
        """
        获取本地毫秒时间
        :return:
        """
        dt_ms = (round(time.time() * 1000))
        # print("这个是本地的时间：", dt_ms)

        return dt_ms

    def local_jd_time_diff(self):
        """
        计算本地与京东服务器时间差
        :return:
        """
        jd_sjc = self.local_time() - self.jd_time()
        # print("京东时间和本地时间差：", jd_sjc)
        return jd_sjc

    def start(self):
        logger.info('正在等待到达设定时间:{}，检测本地时间与京东服务器时间误差为【{}】毫秒'.format(self.buy_time, self.diff_time))
        while True:
            # 本地时间减去与京东的时间差，能够将时间误差提升到0.1秒附近
            # 具体精度依赖获取京东服务器时间的网络时间损耗
            if self.local_time() - self.diff_time >= self.buy_time_ms:
                logger.info('时间到达，开始执行……')
                break
            else:
                try:
                    time.sleep(0.5)
                    logger.info('时间未到，等待一下下在来…')
                except:
                    print("手动终止")
                    break


if __name__ == '__main__':
    Timer().start()
    # print(723000 - 663000)
