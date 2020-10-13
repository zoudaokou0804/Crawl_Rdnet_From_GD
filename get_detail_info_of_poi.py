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
import os
requests.packages.urllib3.disable_warnings()
# 获取txt文件中的cookies字符串
def load_cookies():
    cur_dir_pth=os.path.dirname(os.path.abspath(__file__))
    with open(cur_dir_pth+'\\cookies.txt','r',encoding='utf-8') as f:
        cookies=f.read()
        # print(cookies)
    return cookies

# 将新获得的cookie字符串写入txt文件中
def update_cookies(cookies):
    with open('cookies.txt','w',encoding='utf-8') as f:
        f.write(cookies)
    # print(cookies)

# 获取兴趣点详细信息
def get_detail_info(id):
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
    head['cookie']=load_cookies()
    head['sec-fetch-dest']='document'
    head['sec-fetch-mode']='navigate'
    head['sec-fetch-site']='none'
    head['upgrade-insecure-requests']='1'
    # 下面这个是隐藏的api接口提取兴趣点详细信息，官网未公布，自己摸索
    
    url='https://ditu.amap.com/detail/get/detail?id=%s'%id
    p = requests.get(url, headers=head,verify=False)
    # print(p.text)
    json_data=json.loads(p.text)
    road_data=[] #一条道路的数据集合，包含道路上所有路段的数据集合
    try:
        name=json_data['data']['base']['name']
        try:
            route_list=json_data['data']['spec']['mining_shape']['shape'].split('|') # 单条道路所有分段集合
        except:
            route_list=[json_data['data']['spec']['mining_shape']['shape']]
        # print(name)
        # print(route_list)
        
        i=1 # 路段编号
        for path in route_list:
            path_data=[]
            lat_lon_list=path.split(';')
            longitude_x=lat_lon_list[0].split(',')[0]
            latitude_y=lat_lon_list[0].split(',')[1]
            # 根据路径起点坐标构建新的url获取道路的等级及宽度等信息
            url='https://www.amap.com/service/regeo?longitude=%s&latitude=%s'%(longitude_x,latitude_y)
            rego = requests.get(url, headers=head,verify=False)
            jd=json.loads(rego.text)    
            roadlist=jd['data']['road_list']
            for road in roadlist:
                if road['name']==name:
                    road_level=road['level']  # 道路等级
                    road_width=road['width']  # 道路宽度
                    break # 跳出循环
            path_data=[i,name,path,road_level,road_width] # 道路上一条路段的数据集合，包含路径坐标。道路等级，道路宽度
            i=i+1
            road_data.append(path_data)
            # print(path_data)
    except:
        print('需要重新设置cookies，才能继续爬取数据')
        verify_and_get_new_cookies()
        # update_cookies(new_cookies)
        get_detail_info(id)
    print('路段数：'+str(len(road_data)))
    return road_data
    
if __name__ == "__main__":
    id='BZAHR100GZ'
    get_detail_info(id)