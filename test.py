path='cookies.txt'
with open(path,'r',encoding='utf-8') as f:
    cookies=f.read()
    print(cookies)
path2='cookies2.txt'
with open(path2,'w',encoding='utf-8') as f:
        f.write('测试测试2')