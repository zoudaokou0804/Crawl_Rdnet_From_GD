#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:main.py
@Time:2020/10/14 13:46:19
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:实现大区域批量下载道路网数据主程序入口
'''
from get_batch_pois_id import get_pois_id
from Road_Data_to_txt import data_write_to_txt
import os
import time
import requests
import sys
# 重启脚本程序
def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)

def readpois():
    road_id_list=[]
    path=os.path.dirname(os.path.abspath(__file__))+'\\poi_id_list.txt'
    with open(path,'r',encoding='utf-8') as f:
        roadlist=f.readlines() # 每次只取9个道路id，因为高德限制了一次大于9个就会出错
        for line in roadlist[:9]:
            id=line.split(':')[0]
            # print(id)
            road_id_list.append(id)
        with open(path,'w',encoding='utf-8') as f:
            f.write(''.join(roadlist[9:])) # 取完前9个id后，删除文件中前9个元素
    return road_id_list

def main(poi_type,citcode):
    print('开始下载数据......')
    start_time=time.time()
    roadlist=readpois()
    print(roadlist)
    # roadsdicts=get_pois_id(poi_type,citcode)
    # ids=roadsdicts.keys()
    # ids2=[ key for key,value in roadsdicts.items() ]
    # print(ids)
    for roadid in roadlist:
        data_write_to_txt(roadid)

    print('数据下载完成......')
    end_time=time.time()
    print('总耗时：%s s'%(end_time-start_time))

    try:
        restart_program()
    except:
        print('全部取完')
if __name__ == "__main__":
    poi_type='190301'   # 兴趣点类别，详见excel文件分类，此处代表道路
    citcode='310110'      # 城市区域代码，详见excel文件
    main(poi_type,citcode)
