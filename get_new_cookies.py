#!/user/bin/env python
# -*- encoding:utf-8 -*_
'''
@File:test_selenium.py
@Time:2020/09/30 14:20:32
@Author:zoudaokou
@Version:1.0
@Contact:wangchao0804@163.com
@desc:反反爬，自动滑块验证,并返回验证通过后的cookies，用于get_detail_of_poi中设置新的cookie，绕过反扒
参考博客： https://www.cnblogs.com/qsmyjz/p/12067623.html
https://blog.csdn.net/kzl_knight/article/details/106613495?utm_medium=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-BlogCommendFromMachineLearnPai2-1.edu_weight

'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def verify_and_get_new_cookies():
  print('自动化测试开始.......')
  options = webdriver.ChromeOptions()

  options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
  options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
  options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
  # options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
  # options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
  # options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
  options.add_argument(
      "user-agent=Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  options.add_experimental_option('useAutomationExtension', False)
  driver = webdriver.Chrome(options=options, executable_path='./chromedriver')
  driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
      Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
      })
    """
  })


  # driver.get('https://www.amap.com')
  # sleep(1)
  driver.get('https://www.amap.com/place/BZ9IQZ00DZ')

  driver.maximize_window()  # 最大化浏览器窗口，必须要加这句话，不然在缩放窗口下自动拖拽滑块后依然无法通过

  sleep(0.5)
  # 获取滑块位置
  driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'sufei-dialog-content')]"))
  sour=driver.find_element_by_css_selector("#nc_1_n1z")
  ele=driver.find_element_by_css_selector("#nc_1__scale_text > span")
  # print(sour)
  # print(ele)
  # 拖动滑块
  ActionChains(driver).drag_and_drop_by_offset(sour,ele.size['width'],-sour.size['height']).perform()

  cookies_list=driver.get_cookies()
  cookies_str=''
  # 以下打印cookie列表中每一项的名称和值
  item_num=len(cookies_list)
  for i in range(item_num):
    name=cookies_list[i]['name']
    value=cookies_list[i]['value']
    name_vaule=name+'='+value+';'
    # print(name_vaule)
    cookies_str+=name_vaule
  print(cookies_str)
  print('自动化测试结束......')
  return cookies_str
  # 停留1s后自动关闭浏览器
  # sleep(1)
  # driver.close()

if __name__ == "__main__":
    verify_and_get_new_cookies()