from datetime import date, datetime
from time import time, localtime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import http.client, urllib
import json


week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
year = localtime().tm_year
month = localtime().tm_mon
day = localtime().tm_mday
today = datetime.date(datetime(year=year, month=month, day=day))
week = week_list[today.isoweekday() % 7]

city = os.environ['CITY']

birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


# def get_birthday():
#   next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#   if next < datetime.now():
#     next = next.replace(year=next.year + 1)
#   return (next - today).days


def get_color():
  # 获取随机颜色
  get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
  color_list = get_colors(100)
  return random.choice(color_list)


def get_birthday(birthday, year, today):
  # 获取生日的月和日
  birthday_month = int(birthday.split("-")[1])
  birthday_day = int(birthday.split("-")[2])
  # 今年生日
  year_date = date(year, birthday_month, birthday_day)
  # 计算生日年份，如果还没过，按当年减，如果过了需要+1
  if today > year_date:
      birth_date = date((year + 1), birthday_month, birthday_day)
      birth_day = str(birth_date.__sub__(today)).split(" ")[0]
  elif today == year_date:
      birth_day = 0
  else:
      birth_date = year_date
      birth_day = str(birth_date.__sub__(today)).split(" ")[0]
  return birth_day


#彩虹屁
def caihongpi():
  conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
  params = urllib.parse.urlencode({'key':'3b17bbea47c5a5820ba27904a77a1ebc'})
  headers = {'Content-type':'application/x-www-form-urlencoded'}
  conn.request('POST','/caihongpi/index',params,headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data)
  data = data["newslist"][0]["content"]
  if("XXX" in data):
      data.replace("XXX","宝宝")
  return data


# 早安语
def zaoan():
  conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
  params = urllib.parse.urlencode({'key':'3b17bbea47c5a5820ba27904a77a1ebc'})
  headers = {'Content-type':'application/x-www-form-urlencoded'}
  conn.request('POST','/zaoan/index',params,headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data) #转换成字典
  return data["newslist"][0]["content"]

#下雨概率和建议
def tip():
  conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
  params = urllib.parse.urlencode({'key':'3b17bbea47c5a5820ba27904a77a1ebc','city':'荆门市'})
  headers = {'Content-type':'application/x-www-form-urlencoded'}
  conn.request('POST','/tianqi/index',params,headers)
  res = conn.getresponse()
  data = res.read()
  data = json.loads(data)
  weather = data["newslist"][0]["weather"]
  max_temperature = data["newslist"][0]["highest"]
  min_temperature = data["newslist"][0]["lowest"]
  pop = data["newslist"][0]["pop"]
  tips = data["newslist"][0]["tips"]
  return pop,tips



if __name__ == "__main__":
  # 彩虹屁
  pipi = caihongpi()
  #下雨概率和建议
  weather,max_temperature,min_temperature,pop,tips = tip()
  # 早安语言
  zaoan = zaoan()
  
  
  client = WeChatClient(app_id, app_secret)
  wm = WeChatMessage(client)
  
  data = {
          "date": {
              "value": "{} {}".format(today, week),
              "color": get_color()
          },
          "city": {
              "value": city,
              "color": get_color()
          },
          "weather": {
              "value": weather,
              "color": get_color()
          },
          "min_temperature": {
              "value": min_temperature,
              "color": get_color()
          },
          "max_temperature": {
              "value": max_temperature,
              "color": get_color()
          },
          "pipi": {
              "value": pipi,
              "color": get_color()
          },
          "zaoan": {
              "value": zaoan,
              "color": get_color()
          },
          "pop": {
              "value": pop,
              "color": get_color()
          },
          "tips": {
              "value": tips,
              "color": get_color()
          }
  }
  res = wm.send_template(user_id, template_id, data)















