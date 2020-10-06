#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:get_detail_of_poi.py
@Time:2020/09/29 14:04:13
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:根据获取的兴趣点唯一标识id，获取兴趣点的详细信息，道路也是一种兴趣点
'''

# 获取代理头的方法
from fake_useragent import UserAgent
import requests
from get_proxyi_ip_one import get_proxyip, getheaders
from get_new_cookies import verify_and_get_new_cookies
import json
def get_detail_json(id):
    # proxy = get_proxyip()
    # head = getheaders()
    head={}
    # head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'
    head['User-Agent']=getheaders()['User-Agent']
    head['authority']='ditu.amap.com'
    head['method']='GET'
    head['path']='/place/%s'%id
    head['scheme']='https'
    head['accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    head['accept-encoding']='gzip, deflate, br'
    head['accept-language']='zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
    head['cookie']='guid=860a-7ec7-5acf-ad24;UM_distinctid=174fbb35be02dc-039d6dcc552166-25c1b2a-1fa400-174fbb35be14ca;CNZZDATA1255626299=238811083-1601945840-%7C1601945840;cna=z8ECGGND3kwCAYviHSwckJIb;xlly_s=1;x5sec=7b22617365727665723b32223a223461326334376365373362613132303336616532386135386264646666663933434d2b6e372f7346454f3374345a2f4e6937374747673d3d227d;l=eBME8J7POc00CqhFBO5Cnurza779oIObzsPzaNbMiInca6G5sFgXShQ4SM5k-dtjgt5DpeEr55812R39So4_WxOiCcP8TwE6QTvwRe1..;tfstk=cxGFBuXZtBdUTZNYtWNPNCZM9g6daQ3nr1zbKYAJCdFH7pVQ0sbc2PcGDPz7DC2h.;isg=BP__hXhfnE2IYphRUjIYRF4zjtOJ5FOGKUuB6ZHNn671oB0imLek1Hj24nBe-Cv-;_uab_collina=160195127604843234580833;'
    head['sec-fetch-dest']='document'
    head['sec-fetch-mode']='navigate'
    head['sec-fetch-site']='none'
    head['upgrade-insecure-requests']='1'
    # 下面这个是隐藏的api接口提取兴趣点详细信息，官网未公布，自己摸索
    url='https://ditu.amap.com/detail/get/detail?id=%s'%id
    p = requests.get(url, headers=head)
    # print(p.text)
    json_data=json.loads(p.text)
    try:
        name=json_data['data']['base']['name']
        print(name)
        return name
    except:
        print('需要重新设置cookies，才能继续爬取数据')
        head['cookie']=verify_and_get_new_cookies()
        url='https://ditu.amap.com/detail/get/detail?id=%s'%id
        p = requests.get(url, headers=head)
        # print(p.text)
        json_data=json.loads(p.text)
        name=json_data['data']['base']['name']
        print(name)
        return name
if __name__ == "__main__":
    id='B0FFGQ81BR'
    get_detail_json(id)