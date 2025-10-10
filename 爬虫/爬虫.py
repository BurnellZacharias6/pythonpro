import requests
url='https://www.weather.com.cn/alarm/alarm_list.shtml'
response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)

imgae=requests.get("https://www.baidu.com/img/flexible/logo/pc/peak-result.png")
with open("test.jpg","wb") as f:
    f.write(imgae.content)