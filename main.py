from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random

today = datetime.now()
city = os.environ['CITY']
#province = os.environ['PROVINCE']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

user_id = os.environ["USER_ID"]
template_id = os.environ["TEMPLATE_ID"]


# def get_weather():
#   url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
#   res = requests.get(url).json()
#   weather = res['data']['list'][0]
#   return weather['weather'], math.floor(weather['temp'])

# def get_birthday():
#   next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#   if next < datetime.now():
#     next = next.replace(year=next.year + 1)
#   return (next - today).days

# def get_words():
#   words = requests.get("https://api.shadiao.pro/chp")
#   if words.status_code != 200:
#     return get_words()
#   return words.json()['data']['text']

# def get_random_color():
#   return "#%06x" % random.randint(0, 0xFFFFFF)


# client = WeChatClient(app_id, app_secret)

# wm = WeChatMessage(client)
# wea, temperature = get_weather()
# data = {"weather":{"value":wea},"temperature":{"value":temperature},"birthday_left":{"value":get_birthday()},"words":{"value":get_words(), "color":get_random_color()}}
# res = wm.send_template(user_id, template_id, data)
# print(res)

def get_color():
  # 获取随机颜色
  get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
  color_list = get_colors(100)
  return random.choice(color_list)

# def get_weather(province, city):
#   # 城市id
#   try:
#       city_id = cityinfo.cityInfo[province][city]["AREAID"]
#   except KeyError:
#       print("推送消息失败，请检查省份或城市是否正确")
#       os.system("pause")
#       sys.exit(1)
#   # city_id = 101280101
#   # 毫秒级时间戳
#   t = (int(round(time() * 1000)))
#   headers = {
#       "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
#       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#   }
#   url = "http://d1.weather.com.cn/dingzhi/{}.html?_={}".format(city_id, t)
#   response = get(url, headers=headers)
#   response.encoding = "utf-8"
#   response_data = response.text.split(";")[0].split("=")[-1]
#   response_json = eval(response_data)
#   # print(response_json)
#   weatherinfo = response_json["weatherinfo"]
#   # 天气
#   weather = weatherinfo["weather"]
#   # 最高气温
#   temp = weatherinfo["temp"]
#   # 最低气温
#   tempn = weatherinfo["tempn"]
#   return weather, temp, tempn


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
  return pop,tips

#推送信息
# def send_message(to_user, access_token, city_name, weather, max_temperature, min_temperature, pipi, zaoan, pop, tip):
#   url = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}".format(access_token)
#   week_list = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"]
#   year = localtime().tm_year
#   month = localtime().tm_mon
#   day = localtime().tm_mday
#   today = datetime.date(datetime(year=year, month=month, day=day))
#   week = week_list[today.isoweekday() % 7]
#   # 获取在一起的日子的日期格式
#   love_year = int(config["love_date"].split("-")[0])
#   love_month = int(config["love_date"].split("-")[1])
#   love_day = int(config["love_date"].split("-")[2])
#   love_date = date(love_year, love_month, love_day)
#   # 获取在一起的日期差
#   love_days = str(today.__sub__(love_date)).split(" ")[0]
#   # 获取所有生日数据
#   birthdays = {}
#   for k, v in config.items():
#       if k[0:5] == "birth":
#           birthdays[k] = v
#   data = {
#       "touser": to_user,
#       "template_id": template_id,
#       "url": "http://weixin.qq.com/download",
#       "topcolor": "#FF0000",
#       "data": {
#           "date": {
#               "value": "{} {}".format(today, week),
#               "color": get_color()
#           },
#           "city": {
#               "value": city_name,
#               "color": get_color()
#           },
#           "weather": {
#               "value": weather,
#               "color": get_color()
#           },
#           "min_temperature": {
#               "value": min_temperature,
#               "color": get_color()
#           },
#           "max_temperature": {
#               "value": max_temperature,
#               "color": get_color()
#           },
#           "love_day": {
#               "value": love_days,
#               "color": get_color()
#           },
#           "pipi": {
#               "value": pipi,
#               "color": get_color()
#           },
#           "lizhi": {
#               "value": lizhi,
#               "color": get_color()
#           },
#           "zaoan": {
#               "value": zaoan,
#               "color": get_color()
#           },
#           "pop": {
#               "value": pop,
#               "color": get_color()
#           },
#           "tips": {
#               "value": tips,
#               "color": get_color()
#           }
#       }
#   }
#   for key, value in birthdays.items():
#     # 获取距离下次生日的时间
#     birth_day = get_birthday(value, year, today)
#     # 将生日数据插入data
#     data["data"][key] = {"value": birth_day, "color": get_color()}
#     headers = {
#       'Content-Type': 'application/json',
#       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
#     }
#     response = post(url, headers=headers, json=data).json()
#     if response["errcode"] == 40037:
#       print("推送消息失败，请检查模板id是否正确")
#     elif response["errcode"] == 40036:
#       print("推送消息失败，请检查模板id是否为空")
#     elif response["errcode"] == 40003:
#       print("推送消息失败，请检查微信号是否正确")
#     elif response["errcode"] == 0:
#       print("推送消息成功")
#     else:
#       print(response)


if __name__ == "__main__":
  # 传入省份和市获取天气信息
  #weather, max_temperature, min_temperature = get_weather(province, city)
  # 彩虹屁
  pipi = caihongpi()
  #下雨概率和建议
  pop,tips = tip()
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
              "value": city_name,
              "color": get_color()
          },
#           "weather": {
#               "value": weather,
#               "color": get_color()
#           },
#           "min_temperature": {
#               "value": min_temperature,
#               "color": get_color()
#           },
#           "max_temperature": {
#               "value": max_temperature,
#               "color": get_color()
#           },
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















