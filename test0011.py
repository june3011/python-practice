import calendar     # 캘린더 모듈 사용
import datetime     # date / time 에 대한 모듈
d=datetime.datetime.now()
print(calendar.month(d.year, d.month))