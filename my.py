    #导入包
import datetime
from zhdate import ZhDate

import requests
import json

import requests
import json
import time

today = datetime.datetime.now()
today2 = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
y = (datetime.datetime(2024,1,1) - today)
a = (datetime.datetime(2024,2,10) - today)
b = (datetime.datetime(2024,2,9) - today) 
c = (datetime.datetime(2024,4,4) - today)
d = (datetime.datetime(2024,4,1) - today)
e = (datetime.datetime(2024,6,10) - today)
f = (datetime.datetime(2023,9,29) - today)
g = (datetime.datetime(2023,10,1) - today)



def gz(payrollDate):  # 发工资日期
    x  = today.month
    while  int((datetime.datetime(today.year,x,payrollDate) - today).days) < 0:
        x += 1
    return (datetime.datetime(today.year,x,payrollDate) - today)
    
def offDutyTime(hour,minute): #下班时间差
    timeDifference = datetime.datetime(today.year,today.month,today.day,hour,minute) -today
    timeDifference = timeDifference
    return time.strftime('%H:%M:%S',time.gmtime(timeDifference.total_seconds()))

def hftq(): #和风天气
    key='##################'   #我自己的和风天气key，你最好自己注册一个，免费的
    location='CN101040100'            #城市代码
    url="https://devapi.qweather.com/v7/weather/3d?"
    params = {'location': location,'key': key,'lang': 'zh'}
    res=requests.get(url=url,params=params)
    jsondata=res.json()['daily']
    todaydata=jsondata[0]
    tomdata=jsondata[1]
    readweather1='今日天气:'+todaydata['textDay']+todaydata["moonPhase"]+todaydata['windDirDay']+todaydata['windScaleDay']+'级。最高温度'+todaydata['tempMax']+'度，最低温度'+todaydata['tempMin']+'度。\n'
    readweather2='明日天气:'+tomdata['textDay']+tomdata["moonPhase"]+tomdata['windDirDay']+tomdata['windScaleDay']+'级。最高温度'+tomdata['tempMax']+'度，最低温度'+tomdata['tempMin']+'度。'
    readweather=readweather1+readweather2
    return readweather

def API(types):   #api很多都来自https://api.aa1.cn/ 这个网站
    if types == "名人名言":
        res = requests.get("https://v.api.aa1.cn/api/api-wenan-mingrenmingyan/index.php?aa1=json",verify=False)
        return f'{res.json()[0]["mingrenmingyan"]}'
    elif types == "安慰":
        res = requests.get("https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=json",verify=False)
        return f'{res.json()["anwei"]}'
    elif types == "网易云热评":
        wyy = requests.get("https://v1.hitokoto.cn/?c=j")
        return f'{wyy.json()["hitokoto"]}  来自{wyy.json()["from_who"]}的《{wyy.json()["from"]}》'
    elif types == "一言分享":
        res = requests.get("https://v1.hitokoto.cn/")
        return  f'{res.json()["hitokoto"]}  来自{res.json()["from"]}'
    elif types == '爱情文案':
        res =requests.get("https://v.api.aa1.cn/api/api-wenan-aiqing/index.php?type=json",verify=False) 
        return f'{res.json()["text"]}'
    elif types == 'emo':
        res =requests.get("http://api.sc1.fun/API/emo.php",verify=False) 
        res = res.text.replace("emo自愈文案","")
        res= res.replace("————ScAPI————","")
        res = res.replace("\n","")
        res = res.replace(" ","")
        return res

sayHello = lambda x : "早上好" if x < 12 else("下午好" if 12 < x < 18 else "晚上好")

X  = f"现在是{today2}，\n {ZhDate.from_datetime(today).chinese()},\n{sayHello(today.hour)} 打工人！工作再累，一定不要忘记照顾自己哦！有事没事喝杯茶，舒展一下身体，去廊道走走别老在工位上坐着，钱是老板的,但命是自己的\n距离下班还有{offDutyTime(18,30)}的时间了\n距离下次充值大概还有{int(gz(15).days)}天\n距离元旦节还有{int(y.days) -1}天\n距离春节还有{int(a.days) -1}天\n距离清明节还有{int(b.days) -1}天\n距离劳动节还有{int(d.days)}天\n距离端午节还有{int(e.days) }天\n距离中秋节还有{int(f.days) }天\n距离国庆节还有{int(g.days) -1}天\n距离年假还有{int(a.days) -1}天\n距离除夕还有{int(b.days) -1}天\n上班是帮老板赚钱，但是身体是革命的本钱！\n最后，祝愿天下所有打工人，都能愉快的渡过每一天\n{hftq()}\n今日励志：\n{API(types='名人名言')}\n今日安慰：\n{API(types='安慰')}\n 今日网易云：\n{API('网易云热评')}\n 今日爱情：\n{API('爱情文案')}\n 今日emo:\n{API('emo')}"

def ding():  #这里发送到钉钉 群聊消息
    headers={'Content-Type': 'application/json'}
    
    data1 ={"at": {"atMobiles":[""],"atUserIds":["user123"],"isAtAll": False},"text": {
            "content":f"{X}"},"msgtype":"text"}
    robot= requests.post(url = robot_url,data=json.dumps(data1),headers=headers,verify=False)
    # robot= requests.post(url = robot_url4,data=json.dumps(data1),headers=headers)
    #robot= requests.post(url = robot_url3,data=json.dumps(data1),headers=headers)
    print(robot)

if __name__ == '__main__':
    if 9 <today.hour < 19:
        ding()
