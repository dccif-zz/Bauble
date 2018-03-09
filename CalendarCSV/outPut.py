import datetime
import re
from datetime import time

from bs4 import BeautifulSoup
from bs4 import SoupStrainer


# 从文件读取课表
def readLessonTable(infile):
    only_td_tags = SoupStrainer("td", {"align": "Center"})
    with open(infile) as CalendarFile:
        read_data = CalendarFile.read()

    bsStr = BeautifulSoup(read_data, "html.parser", parse_only=only_td_tags).prettify()

    # 去除空<td>
    patternTd = re.compile(r'<td align="Center">&nbsp;</td>')
    firstClass = re.compile(r'<td align="Center" rowspan="\d"', flags=re.DOTALL)
    afterStr = re.sub(patternTd, "", bsStr)

    # 找到第一门课位置
    startpos = firstClass.search(afterStr).start()
    classstart = afterStr[startpos:]

    # 提取课表<td>
    patternEle = re.compile(r'<td align="Center" rowspan="\d".*?</td>', flags=re.DOTALL)
    allclass = patternEle.findall(classstart)
    return allclass


# 获取tag中文本
def tdText(tdList):
    soup = BeautifulSoup(tdList, "html.parser")
    return soup.get_text()


# 添加Less类
def LessObjList(tdList):
    LessList = []
    length = tdList.__len__()
    for obj in tdList:
        LessList.append(wraplesson(obj))
    return LessList


# 移除多余符号
def removeLine(tdListEle):
    temp = tdText(tdListEle).split("\n \n")
    afterList = []
    for str in temp:
        if str != "":
            afterList.append(str.strip())
    return afterList


# 计算课程时间
def getSpan(List):
    out = []
    if List.__len__() >= 3:
        alltime = List[1].split('{')
        classtime = alltime[0]
        classspan = classtime[3:][:-1]
        spanweek = alltime[1]
        out.append(classtime[1])
        out.append(classspan)
        out.append(countWeek(spanweek))
    return out


# 计算持续周
def countWeek(str):
    temp = str.split('-')
    endweek = temp[1][:-2]
    startweek = temp[0][1:]
    count = int(endweek) - int(startweek) + 1
    return count


# 包装课程
def wraplesson(lesslist):
    onelesson = removeLine(lesslist)
    lessontime = getSpan(onelesson)
    lessonListLength = onelesson.__len__()
    # 标准课程
    if lessonListLength > 3:
        return Lesson(onelesson[0], lessontime[0], lessontime[1], lessontime[2], onelesson[2], onelesson[3])
    # 实验课程
    if lessonListLength == 3:
        return Lesson(onelesson[0], lessontime[0], lessontime[1], lessontime[2], onelesson[2], '')


# 写文件
def writefile(filename, instr):
    with open(filename, 'w') as outFile:
        outFile.write(instr)


# 字符拼接
def str_join(LessonList, addExp="Y"):
    title_start = r'"主题","开始日期**","开始时间","结束日期","结束时间","全天事件","提醒开/关","提醒日期","提醒时间","会议组织者","必需的与会者","可选的与会者","会议资源",' \
                  r'"地点**","记帐信息","类别","里程","忙闲状态","敏感度","说明","私有","优先级" '
    newLine = '\n'
    LessonStr = title_start + newLine
    strlesson = ""
    for lesson in LessonList:
        if lesson != None:
            strlesson = strlesson + "".join(lesson.classStr())
        else:
            continue
    if addExp.upper() == "Y":
        return LessonStr + strlesson
    else:
        strNoExp = ""
        strlesson = strlesson.splitlines()
        for line in strlesson:
            if "实验" in line:
                continue
            strNoExp = strNoExp + line + "\n"
        return LessonStr + strNoExp


class Lesson(object):
    term_begin = datetime.date(2018, 3, 5)

    def __init__(self, name, weekday, span, count, teacher, loc):
        self.name = name
        self.weekday = weekday
        self.span = span
        self.count = count
        self.teacher = teacher
        self.loc = loc

    # 处理开始日期
    def __startPro(self):
        startday = self.weekday
        if startday == "一":
            # delta = datetime.timedelta(days=1)
            startday = self.term_begin
        elif startday == "二":
            delta = datetime.timedelta(days=1)
            startday = self.term_begin + delta
        elif startday == "三":
            delta = datetime.timedelta(days=2)
            startday = self.term_begin + delta
        elif startday == "四":
            delta = datetime.timedelta(days=3)
            startday = self.term_begin + delta
        elif startday == "五":
            delta = datetime.timedelta(days=4)
            startday = self.term_begin + delta
        return startday

    def __dayStrList(self):
        outList = []
        startday = self.__startPro()
        delta = datetime.timedelta(days=7)
        # print(self.term_begin.strftime('%Y/%m/%d'))
        outList.append(startday)
        for count in range(1, self.count):
            startday = startday + delta
            outList.append(startday)
        # print(outList)
        return outList

    # 处理课程时间间隔
    def __timeStrList(self):
        timeList = []
        twoclasstimedelta = datetime.timedelta(minutes=45 * 2 + 5)
        threeclasstimedelta = datetime.timedelta(minutes=45 * 3 + 2 * 5)
        Lessontime = self.span
        if Lessontime == '1,2':
            timeStart = time(hour=8, minute=0, second=0)
            timeList.append(timeStart)
            timeEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), timeStart) + twoclasstimedelta).time()
            timeList.append(timeEnd)
        elif Lessontime == '3,4':
            timeStart = time(hour=9, minute=55, second=0)
            timeList.append(timeStart)
            timeEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), timeStart) + twoclasstimedelta).time()
            timeList.append(timeEnd)
        elif Lessontime == '3,4,5':
            timeStart = time(hour=9, minute=55, second=0)
            timeList.append(timeStart)
            timeEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), timeStart) + threeclasstimedelta).time()
            timeList.append(timeEnd)
        elif Lessontime == '6,7':
            timeStart = time(hour=13, minute=15, second=0)
            timeList.append(timeStart)
            timeEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), timeStart) + twoclasstimedelta).time()
            timeList.append(timeEnd)
        elif Lessontime == '8,9':
            timeStart = time(hour=15, minute=5, second=0)
            timeList.append(timeStart)
            timeEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), timeStart) + twoclasstimedelta).time()
            timeList.append(timeEnd)
        elif Lessontime == '10,11,12':
            timeStart = time(hour=18, minute=00, second=0)
            timeList.append(timeStart)
            timeEnd = (datetime.datetime.combine(datetime.date(1, 1, 1), timeStart) + threeclasstimedelta).time()
            timeList.append(timeEnd)
        # print(timeList)
        return timeList

    # 处理课程
    def classStr(self):
        outList = []
        dayList = self.__dayStrList()
        timeList = self.__timeStrList()
        emptSign = re.compile(r'"x"')
        for count in range(self.count):
            oneRow = []
            oneRow.append(self.name)
            oneRow.append(dayList[count].strftime('%Y/%m/%d'))
            oneRow.append(timeList[0].strftime("%X"))
            oneRow.append(dayList[count].strftime('%Y/%m/%d'))
            oneRow.append(timeList[1].strftime("%X"))
            oneRow.append("False\",\"False")
            oneRow.append(dayList[count].strftime('%Y/%m/%d'))
            oneRow.append(timeList[0].strftime("%X"))
            oneRow.append(r'x","x","x","x')
            oneRow.append(self.loc)
            oneRow.append(r'x","x","x')
            oneRow.append("2\",\"普通")
            oneRow.append("")
            oneRow.append("False\",\"中")
            oneRow = "\"" + "\",\"".join(oneRow) + "\"\n"
            oneRow = re.sub(emptSign, "", oneRow)
            outList.append(oneRow)
        # print(outList)
        return outList


if __name__ == "__main__":
    allClass = readLessonTable("downCalendar.html")

    allLesson = LessObjList(allClass[1:allClass.__len__() - 1])
    str_join(allLesson, "n")
    # b = allLesson[9].classStr()
    # writefile("out.csv", str_join(allLesson))
