# python3日期和时间

# 时间元组
'''
tm_year     4位数年      2017
tm_mon      月           1到12
tm_mday     日           1到31
tm_hour     小时          0到23
tm_min      分钟          0到59
tm_sec      秒           0到61（闰秒）
tm_wday     一周的第几日  0到6（0是周一）
tm_yday     一年的第几日  1到366
tm_isdst    夏令时        值有：1(夏令时)、0(不是夏令时)、-1(未知)，默认 -1

'''

# time 模块
import time

localtime = time.localtime(time.time())
print('本地市时间为:', localtime)
# time.struct_time(tm_year=2017, tm_mon=10, tm_mday=12, tm_hour=9, tm_min=10, tm_sec=34, tm_wday=3, tm_yday=285, tm_isdst=0)
localtime = time.asctime(time.localtime(time.time()))
print('本地市时间为:', localtime)
# Thu Oct 12 09:10:34 2017

# 格式化日期
print(time.strftime('%Y-%m-%d &H:%M:%S', time.localtime()))
# 2017-10-12 &H:23:26
print(time.strftime('%a %b %d %H:%M:%S %Y', time.localtime()))
# Thu Oct 12 09:23:26 2017
date = 'Sat Mar 28 22:24:24 2017'
print(time.mktime(time.strptime(date, '%a %b %d %H:%M:%S %Y')))
# 格式化为时间戳    1490711064.0


# python3中日期格式化符号
'''
%y      两位数的年份表示（00-99）
%Y      四位数的年份表示（000-9999）
%m      月（01-12）
%d      日（0-31）
%H      24小时制度（0-23）
%I      12小时制度（01-12）
%M      分钟数（00=59）
%S      秒（00-59）
%a      本地简写星期（Mon  Tue   Wed  Thu  Fri   Sat  Sun）
%A      本地完整星期
%b      本地简写月份（Jan Feb Mar Apr May June July  Aug  Sept  Oct  Nov  Dec）
%B      本地完整月份
%c      本地相应的日期表示和时间表示
%j      年内的一天(001-366)
%p      本地A.M或者P.M的等价符
%U      一年中的星期数(00-53),星期天为开始
%w       星期(0-6)
%W       一年中的星期数(00-53)，星期一为开始
%x       本地相应的日期表示
%X        本地相应的时间表示
%Z        当前时期名称

'''


def getTime(fomatStr):
    localtime = time.localtime()
    print(time.strftime(fomatStr, localtime))
    # 2017 10 12 15 24


if __name__ == '__main__':
    getTime('%y')  # 17
    getTime('%Y')  # 2017
    getTime('%m')  # 10
    getTime('%d')  # 12
    getTime('%H')  # 15
    getTime('%I')  # 03
    getTime('%M')  # 27
    getTime('%S')  # 02
    getTime('%a')  # Thu
    getTime('%A')  # Thursday
    getTime('%b')  # Oct
    getTime('%B')  # October
    getTime('%c')  # Thu Oct 12 15:46:16 2017
    getTime('%j')  # 285
    getTime('%p')  # PM
    getTime('%U')  # 41
    getTime('%w')  # 4
    getTime('%W')  # 41
    getTime('%x')  # 10/12/17
    getTime('%X')  # 15:49:07
    getTime('%Z')  # 一堆乱码(?D1¨²¡À¨º¡Á?¨º¡À??)

# time.altzone       返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值
print('time.altzoine: %d' % time.altzone)
# time.altzoine: -32400

# time.asctime([tupletime])  接受时间元组并返回字符串
t = time.localtime()
print('time.asctime(t):%s' % time.asctime(t))
# time.asctime(t):Thu Oct 12 16:04:21 2017

# time.clock()   用以浮点数计算的秒数返回当前的CPU时间

# time.ctime([secs]) 未给参数时，相当于asctime,参数为时间戳
print('time.ctime():%s' % time.ctime())
# time.ctime():Thu Oct 12 16:07:35 2017
print('time.ctime([secs]):%s' % time.ctime(time.time()))
# time.ctime([secs]):Thu Oct 12 16:12:11 2017

# time.gtime([secs]) 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t
print('tiem.gmtime([secs]):', time.gmtime(time.time()))
# tiem.gmtime([secs]): time.struct_time(tm_year=2017, tm_mon=10, tm_mday=12, tm_hour=8, tm_min=18, tm_sec=12, tm_wday=3, tm_yday=285, tm_isdst=0)

# time.localtime([secs]) 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t
print('time.localtime():', time.localtime())
# time.localtime(): time.struct_time(tm_year=2017, tm_mon=10, tm_mday=12, tm_hour=16, tm_min=24, tm_sec=14, tm_wday=3, tm_yday=285, tm_isdst=0)
print('time.loacltime([secs]):', time.localtime(time.time()))
# time.loacltime([secs]): time.struct_time(tm_year=2017, tm_mon=10, tm_mday=12, tm_hour=16, tm_min=26, tm_sec=7, tm_wday=3, tm_yday=285, tm_isdst=0)


# time.mktime(tupletime)    接受时间元组并返回时间辍
t = (2017, 10, 12, 16, 36, 38, 1, 48, 0)
secs = time.mktime(t)
print('time.mktime(t):%f' % secs)
# time.mktime(t):1507797398.000000

# time.sleep(s)   推迟调用线程的运行，s指秒数。
print('start:%d' % time.clock())  # 0
# time.sleep(3)
print('end:%d' % time.clock())  # 3

# time.strftime(fmt[,tupletime]) 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 2017-10-12 16:41:27

# time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')  根据fmt的格式把一个时间字符串解析为时间元组。
struct_time = time.strptime("12 Oct 17", "%d %b %y")
print('返回元组:', struct_time)
# 返回元组: time.struct_time(tm_year=2017, tm_mon=10, tm_mday=12, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=285, tm_isdst=-1)

# time.time()    返回当前时间的时间戳（1970纪元后经过的浮点秒数）。



# calendar 模块

import calendar

# calendar.calendar(year,w=2,l=1,c=6)    返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# print(calendar.calendar(theyear=2017))  #输出2017年日历

# calendar.firstweekday()    返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。

# calendar.isleap(year)      是闰年返回True，否则为false。
print(calendar.isleap(year=2017))  # False

# calendar.leapdays(y1.y2)   返回在Y1，Y2两年之间的闰年总数。
print(calendar.leapdays(y1=2000, y2=2017))  # 5

# calendar.month(year,month,w=2,l=1) 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
print(calendar.month(theyear=2017, themonth=10))  # 打印出2017年10月的日历

# calendar.monthcalendar(year,month)     返回一个列表，日期外的数为0
print(calendar.monthcalendar(year=2017, month=10))
# [[0, 0, 0, 0, 0, 0, 1], [2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22], [23, 24, 25, 26, 27, 28, 29], [30, 31, 0, 0, 0, 0, 0]]

# calendar.monthrange(year,month)    返回两个整数。第一个为当月的第一天的星期数，第二个当月的天数
print(calendar.monthrange(year=2017, month=10))  # (6,31)     10月1日为周日，一共有31天

#calendar.prcal(year,w=2,l=1,c=6)   相当于print(calendar.calendar(year,w,l,c))
#calendar.prcal(theyear=2017)

#calendar.prmonth(year,month,w=2,l=1)   相当于print(calendar.month(theyear, themonth)
#calendar.prmonth(theyear=2017,themonth=10)

#calendar.setfirstweekday() 设置每周的起始日期码。0（星期一）到6（星期日）。

#calendar.timegm(tupletime)     接受一个时间元组形式，返回该时刻的时间辍
print(calendar.timegm((2017,10,12,17,22,30)))     #1507828950

#calendar.weekday(year,month,day)       返回给定日期的日期码
print(calendar.weekday(2017,10,12))     #3  代表周4