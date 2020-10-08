#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:batch_get_poi_info.py
@Time:2020/09/29 19:28:29
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:批量获取数据,获取查询区域所有兴趣点的id
'''
import requests,json
import time
import math
# 读取每一页中所有兴趣点的名称
def get_poi_name(url):
    rsp=requests.get(url)
    data=json.loads(rsp.text)
    namedict={}
    for i in range(len(data['pois'])):
        namedict[data['pois'][i]['id']]=data['pois'][i]['name']
    return namedict

# 按搜索关键字和区域代码获取数据
def get_pois_id(poi_type,citycode):
    key='0662e29ae686aed5e0e3d13902aef81c' # 开发者账号
    onepage_num='20' # 每一页显示的兴趣点个数
    page_num='1' # 显示第多少页
    url='https://restapi.amap.com/v3/place/text?types=%s&city=%s&output=json&offset=%s&page=%s&key=%s&extensions=all'%(poi_type,citycode,onepage_num,page_num,key)
    rsp=requests.get(url)
    data=json.loads(rsp.text)
    num=int(data['count'])
    page_numbs=math.ceil(num/int(onepage_num)) # 计算总共多少页，后面构建每一页的url，读取每一页的数据
    print(num)
    print(page_numbs)
    namedict_all={} # 所查询区域所有兴趣点名称列表
    for i in range(1,page_numbs+1):
        url='https://restapi.amap.com/v3/place/text?types=%s&city=%s&output=json&offset=%s&page=%s&key=%s&extensions=all'%(poi_type,citycode,onepage_num,i,key)
        namedict_all.update(get_poi_name(url)) # 合并所有页的字典
    print(namedict_all)

## 后续实现周边搜索

## 后续实现多边形搜索

## 后续实现id查询

if __name__ == "__main__":
    poi_type='190301'   # 兴趣点类别，详见excel文件分类，此处代表道路
    citcode='310114'      # 城市区域代码，详见excel文件
    get_pois_id(poi_type,citcode)