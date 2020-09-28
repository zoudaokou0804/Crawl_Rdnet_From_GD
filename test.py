# 获取代理头的方法
from fake_useragent import UserAgent
import requests
from get_proxyi_ip_one import get_proxyip, getheaders

'''代理IP地址（高匿）'''
proxy = get_proxyip()
head = getheaders()
'''http://icanhazip.com会返回当前的IP地址'''
p = requests.get('https://ditu.amap.com/detail/get/detail?id=B0FFGQ7PQK', headers=head, proxies=proxy)
# p = requests.get('https://ditu.amap.com/detail/get/detail?id=B0FFGQ7PQK', headers=head)
print(p.text)
# AG=UserAgent().random
# print(AG)