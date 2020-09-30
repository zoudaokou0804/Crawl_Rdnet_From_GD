# 获取代理头的方法
from fake_useragent import UserAgent
import requests,json
from get_proxyi_ip_one import get_proxyip, getheaders


head = getheaders()

response = requests.get('https://www.amap.com/search?query=三环路&city=330600&geoobj=120.858034%7C29.993051%7C120.898681%7C30.031841&zoom=14.02')
# print(response.text)
print(response.headers)

cookie = requests.utils.dict_from_cookiejar(response.cookies)
cookies_str = json.dumps(cookie)
print(cookies_str)