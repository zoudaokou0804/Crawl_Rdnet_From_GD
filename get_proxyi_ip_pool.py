#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:get_proxy_ip.py
@Time:2020/02/16 00:41:37
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:动态获取"免费代理"网站的代理ip
获取多个ip
'''

import requests
import random
import json
from fake_useragent import UserAgent # 获取代理头

def getheaders():
    # user_agent_list = [
    #     "Mozilla/5.0 (Windows; U; Windows NT 5.01) AppleWebKit/535.15.5 (KHTML, like Gecko) Version/5.0 Safari/535.15.5",
    #     "Mozilla/5.0 (Android 1.6; Mobile; rv:49.0) Gecko/49.0 Firefox/49.0",
    #     "Mozilla/5.0 (compatible; MSIE 7.0; Windows 95; Trident/5.1)",
    #     "Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_7 rv:4.0; bn-IN) AppleWebKit/533.33.6 (KHTML, like Gecko) Version/4.0.1 Safari/533.33.6",
    #     "Mozilla/5.0 (iPhone; CPU iPhone OS 5_1_1 like Mac OS X) AppleWebKit/531.2 (KHTML, like Gecko) CriOS/30.0.806.0 Mobile/47E619 Safari/531.2",
    #     "Opera/8.37.(X11; Linux i686; zh-SG) Presto/2.9.175 Version/11.00",
    #     "Opera/8.43.(Windows NT 5.2; fy-NL) Presto/2.9.179 Version/12.00",
    #     "Opera/9.29.(X11; Linux i686; ca-FR) Presto/2.9.161 Version/11.00",
    #     "Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.0; Trident/4.0)",
    #     "Mozilla/5.0 (Android 2.0.1; Mobile; rv:66.0) Gecko/66.0 Firefox/66.0"
    # ]
    # useragent = random.choice(user_agent_list)
    useragent = UserAgent().random
    headers = {"User-Agent": useragent}
    return headers

"""
获取单个代理ip方法
参见网上开源项目：https://github.com/jiangxianli/ProxyIpLib#%E5%85%8D%E8%B4%B9%E4%BB%A3%E7%90%86ip%E5%BA%93
https://www.freeip.top/?page=1
"""
def get_proxyips(url='https://ip.jiangxianli.com/api/proxy_ips'):
    rep=requests.get(url, headers=getheaders())
    rep.encoding=rep.apparent_encoding
    html=rep.text
    data=json.loads(html)
    proxies=[]
    for i in range(len(data['data']['data'])):
        ip=data['data']['data'][i]['ip']
        port=data['data']['data'][i]['port']
        htp_type=data['data']['data'][i]['protocol']
        #因为爬取的是高德，用的https，所以http暂不添加
        # ip_port1='http://'+ip+':'+port
        # proxies.append(ip_port1)
        ip_port2='https://'+ip+':'+port
        proxies.append(ip_port2)
    print(proxies)
    return proxies

if __name__ == "__main__":
    result=get_proxyips()