import os
filename=road_data[0][1]+'.txt'
with open(filename,'w',encoding='utf-8') as f:
    f.write('link_id,road_name,lon,lat,road_level,road_width')
# for link in data: