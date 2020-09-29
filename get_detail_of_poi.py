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
    head['cookie']='guid=6f6c-9e1d-9302-25b4; UM_distinctid=174d9ae6fddda0-0d7c0de175d45-293e1d4e-1fa400-174d9ae6fdfd99; cna=mXAMF4PZzmICAd5C7SQ6bLCt; isg=BOrqT3YYQdawL806ukGJtcPOM1CMW261UrVkT3ShAD3Ip4xhXOiixBcZN1G7TOZN; l=eBPaXM27O18mD2eABO5Zourza77t3QR1hkPzaNbMiInca6NViF1ulNQ4o-xBrdtfMt5cpetzt0ss5REDSSa38O9-NuHk3YLEVwvwSe1..; tfstk=clslBbqNBa8SUuU2Xut5C4vNBF6haOiesMSf0imUWyHXulIBKsKKR8wbhpFGYM5..; xlly_s=1; CNZZDATA1255626299=1182552343-1601379807-%7C1601379807; x5sec=7b22617365727665723b32223a223032343338323065653238666665633034333834306239633136663730616231434c48417a507346454f374d787358516a4c71394b773d3d227d'
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
    id='B00155P5PX'
    get_detail_json(id)