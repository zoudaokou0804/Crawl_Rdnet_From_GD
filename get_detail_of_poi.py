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
    head['cookie']='guid=132c-26ee-3b02-ea79; UM_distinctid=174dcb58dd7c16-06357c9002c746-333376b-1fa400-174dcb58dd8c51; cna=wNL6F5gPNRQCAd5GxBZJVe2R; xlly_s=1; CNZZDATA1255626299=485837329-1601428281-%7C1601449885; x5sec=7b22617365727665723b32223a223537366134373165343335393965653439613864313065623166383862616361434d4872305073464549372b344d7a6531752f4663413d3d227d; isg=BEdHrSLN1Kpf51Ah7aRwYYSx1vsRTBsuzfa4Ohk0Llb9iGZKIB-3fzGOKkjWYPOm; tfstk=ctOhB3wvqpWCxxBMhX1BlRphFsdhZTPPmQR6_CVfqZeGH6RNi1ya3fE-SMxHw81..; l=eBLehBdnO1W5XFLMBOfwnurza77OtIRfguPzaNbMiOCPOo1w5h6GWZz8TV8eCnGVnsU9J3RSn5QgBoYg3yz3lCDsb7FFJl9aCdTh.'
    head['sec-fetch-dest']='document'
    head['sec-fetch-mode']='navigate'
    head['sec-fetch-site']='none'
    head['upgrade-insecure-requests']='1'
    # 下面这个是隐藏的api接口提取兴趣点详细信息，官网未公布，自己摸索
    url='https://ditu.amap.com/detail/get/detail?id=%s'%id
    p = requests.get(url, headers=head)
    # print(p.text)
    json_data=json.loads(p.text)
    name=json_data['data']['base']['name']
    print(name)
    return name
if __name__ == "__main__":
    id='B0FFGWKQJR'
    get_detail_json(id)