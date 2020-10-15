#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:write_to_txt.py
@Time:2020/10/09 09:31:55
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:将获取到的道路的数据列表写入到txt文件中，一条道路一个txt文件
'''
from get_detail_info_of_poi import get_detail_info
import os

def data_write_to_txt(id):
    road_data=get_detail_info(id)
    try:
        records_list=[]
        records_list3=[]
        in_road_index=1
        for link in road_data:
            linkid=link[0]
            road_name=link[1]
            road_level=link[3]
            roadwidth=link[4]
            coord_list=link[2].split(';')
            for coord in coord_list:
                point_id=str(coord_list.index(coord)+1)
                records_list.append(str(linkid)+','+road_name+','+coord+','+road_level+','+roadwidth+','+point_id)
        
        records_list2=list(set(records_list)) # 去除列表中的重复原始
        records_list2.sort(key=records_list.index) # 去重后的列表按原来列表元素的顺序（索引）排列
        filename=road_data[0][1]+'-'+id+'.txt'
        path=os.path.dirname(os.path.abspath(__file__))+'\\data'
        path_filename=path+'\\'+filename
        with open(path_filename,'w',encoding='gb2312') as f:
            f.write('link_id,road_name,lon,lat,road_level,road_width,in_link_id,in_road_index'+'\n')
            for record in records_list2:
                record+=','+str(in_road_index)
                f.writelines(record+'\n')
                in_road_index+=1
                records_list3.append(record)
        print(filename)
    except:
        data_write_to_txt(id)
if __name__ == "__main__":
    id='BZAHR100GZ'
    data_write_to_txt(id) 