import hashlib
import random
import string
from datetime import datetime, time, timedelta
import pandas as pd
import nameGen


class rowData:
    # 可选年级列表
    grade = ["小一", "小二", "小三", "小四", "小五", "小六", "初一", "初二", "初三", "高一", "高二", "高三"]

    # 可选科目列表
    subject = ["英语", "数学", "语文", "物理", "化学"]

    # 我不知道数据库是不是主键就先让用户名不可重复了
    usernameSet = set()

    # 用户ID
    dataid = 0

    # 初始化
    def __init__(self, idbegin):
        '''
        这里是构造函数，id值自增
        介绍部分暂未完成,暂时用0填充
        :param idbegin: 开启的id，之后的id以1的间隔序列递增
        '''
        self.dataid = idbegin + 1
        self.created_time = self._creatTime(2018, 4, 1)
        self.birth = self._genbirth(1970, 1, 1)
        self.grade = self._randGrade()
        self.introduction = '0'
        self.name = nameGen.gen_full_name()
        self.password = self._genranPassSHA256()
        self.phone = self._get_phone_number()
        self.price = self._genRanPrice(100)
        self.subject = self._randSubject()
        self.username = self._genUsername()

    # 列出所有属性值
    def list_all(self):
        out = []
        for name, value in vars(self).items():
            out.append(value)
        return out

    # 生成随机年级
    def _randGrade(self):
        return "".join(random.sample(self.grade, 1))

    # 生成随机科目
    def _randSubject(self):
        return "".join(random.sample(self.subject, 1))

    # 生成随机中国电话号码
    def _get_phone_number(self):
        pre_lst = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150",
                   "151", "152", "153", "155", "156", "157", "158", "159", "186", "187", "188"]

        return random.choice(pre_lst) + ''.join(random.sample("0123456789", 8))

    # 生成随机日期
    def _datelist(self, beginDate, endDate):
        # beginDate, endDate是形如‘20160601’的字符串或datetime格式
        date_l = [datetime.strftime(x, '%Y/%m/%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
        return date_l

    # 生成随机时间 12小时制
    def _randTime(self):
        hours = random.choice(range(0, 24))
        minutes = random.choice(range(0, 60))
        seconds = random.choice(range(0, 60))
        return time(hours, minutes, seconds).strftime("%I:%M:%S %p")

    # 生成 创建时间
    def _creatTime(self, year, month, day):
        return "".join(
            random.sample(self._datelist(datetime(year, month, day), datetime.now()), 1)) + " " + self._randTime()

    # 生成老师生日 因为是老师 默认设置大于18岁
    def _genbirth(self, year, month, day):
        end = datetime.now() - timedelta(days=365 * 18)
        return "".join(random.sample(self._datelist(datetime(year, month, day), end), 1))

    '''
    生成随机密码，默认长度16位，并通过SHA256
    :param len 密码长度
    '''

    def _genranPassSHA256(self, len=16):
        random.seed()
        chars = string.ascii_letters + string.digits
        return hashlib.sha256(''.join([random.choice(chars) for i in range(len)]).encode()).hexdigest()

    '''
    生成价位区间，默认间距100，最大值5000
    :param start 起始位置
    :param end 终止位置
    :param step 间隔
    '''

    def _genRanPrice(self, start, end=5000, step=100):
        return random.choice(range(start, end + step, step))

    # 生成用户名，不可重复
    def _genUsername(self, len=8):
        random.seed()
        chars = string.ascii_letters + string.digits
        newusername = ''.join(random.sample(chars, len))
        if newusername in self.usernameSet:
            self._genUsername()
        else:
            self.usernameSet.add(newusername)
        return newusername
