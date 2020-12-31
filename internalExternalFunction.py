
print("random 을 import 하기 전에 dir() 호출 : {}".format(dir()))

import random

print("random 을 import한 후에 dir() 호출 : {}".format(dir()))


# list of pyhon builtins

# glob : 결로 내의 폴더 / 파일 목록 조회(윈도우 dir)
import glob
print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())

import datetime
print("오늘 날짜는 ", datetime.date.today())
print(datetime.timedelta(100))
print("오늘부토 100일 후는 ", datetime.date.today() + datetime.timedelta(100))