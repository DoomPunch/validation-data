import time
import random


# 15位的不重复id
class RandomSelf:
    def __init__(self):
        pass

    # 不重复的15位id
    @staticmethod
    def random_id() -> str:
        return str(int(time.time()*100000))

    # 精确到秒的YYYYMMDDHHMMSS 当年当月当天
    @staticmethod
    def random_secondtime() -> str:
        # year = time.strftime("%Y", time.localtime())
        year = '2022'
        # year = '2003'
        month = time.strftime("%m", time.localtime())
        # month = '04'
        # day = time.strftime("%d", time.localtime())
        day = "{:02d}".format(random.randint(11, 19))
        hour = "{:02d}".format(random.randint(0, 18))
        # hour = time.strftime("%H", time.localtime())
        minute = "{:02d}".format(random.randint(0, 59))
        # minute = time.strftime("%M", time.localtime())
        second = "{:02d}".format(random.randint(0, 59))
        # second = time.strftime("%S", time.localtime())

        time_for_second = "{0}{1}{2}{3}{4}{5}".format(year, month, day, hour, minute, second)
        return time_for_second

    # 随机生日 1930-2021 YYYYMMDD
    @staticmethod
    def random_birthday():
        year = "%02d" % random.randint(1930, 2021)
        month = "%02d" % random.randint(1, 8)
        day = "%02d" % (random.randint(1, 13))
        birthday = year + month + day
        return birthday

    @staticmethod
    def random_item():
        pass

    @staticmethod
    def random_gender():
        genders = ['F', 'M']
        random.shuffle(genders)
        return genders[0]
