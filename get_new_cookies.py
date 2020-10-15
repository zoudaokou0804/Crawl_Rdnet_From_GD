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
import os

# 反复刷新并移动滑块操作
def refresh_slide(driver):
    refresh_btn = driver.find_element_by_css_selector("#nocaptcha > div > span > a")
    refresh_btn.click()
    sour = driver.find_element_by_css_selector("#nc_1_n1z")
    ele = driver.find_element_by_css_selector("#nc_1__scale_text > span")
    ActionChains(driver).click_and_hold(sour).perform()
    ActionChains(driver).drag_and_drop_by_offset(sour, 500, 0).perform()  

# 判断是否需要重复滑块操作
def juge_slide(driver):
    try:
        search_btn = driver.find_element_by_css_selector("#searchbtn > i")
        search_btn.click()
        return 0
    except:
        return 1
# 将新获得的cookie字符串写入txt文件中
def update_cookies(cookies):
    with open('cookies.txt', 'w', encoding='utf-8') as f:
        f.write(cookies)


def verify_and_get_new_cookies():
    print('自动化测试开始.......')

    options = webdriver.ChromeOptions()
    options.add_argument('start-maximized') # 默认最大化打开，替代driver.maximize_window()
    options.add_argument('verify=False')
    options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    options.add_argument('window-size=1920x1080')  # 指定浏览器分辨率
    options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    # options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    cur_dir_pth = os.path.dirname(os.path.abspath(__file__))
    driver = webdriver.Chrome(options=options,
                              executable_path=cur_dir_pth + '\\chromedriver')
    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument", {
            "source":
            """
      Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
      })
    """
        })

    # driver.get('https://www.amap.com')
    # sleep(1)
    driver.get('https://www.amap.com/place/BZ9IQZ00DZ')

    # driver.maximize_window()  # 最大化浏览器窗口，必须要加这句话，不然在缩放窗口下自动拖拽滑块后依然无法通过
    try:
        # sleep(1)
        # 获取滑块位置
        driver.switch_to.frame(
            driver.find_element_by_xpath(
                "//iframe[contains(@id,'sufei-dialog-content')]"))
        sour = driver.find_element_by_css_selector("#nc_1_n1z")
        ele = driver.find_element_by_css_selector("#nc_1__scale_text > span")
        # print(sour)
        # print(ele)
        # 拖动滑块
        # sleep(1)
        ActionChains(driver).click_and_hold(sour).perform()
        # ActionChains(driver).drag_and_drop_by_offset(sour,ele.size['width'],-sour.size['height']).perform()
        ActionChains(driver).drag_and_drop_by_offset(sour, 500, 0).perform()
        # 点击一次搜索按钮
        sleep(2)
        result=juge_slide(driver)
        while result==1:
            refresh_slide(driver)
            result=juge_slide(driver)
        
        # try:
        #     search_btn = driver.find_element_by_css_selector("#searchbtn > i")
        #     search_btn.click()
        # except:
        #     # driver.quit()
        #     # driver.switch_to.frame(driver.find_element_by_xpath("//*[@id='themap']/iframe"))

    except:
        print('无需验证......')
    # 点击一次搜索按钮
    sleep(1)
    driver.refresh()
    search_btn = driver.find_element_by_css_selector("#searchbtn > i")
    search_btn.click()
    cookies_list = driver.get_cookies()
    cookies_str = ''
    # 以下打印cookie列表中每一项的名称和值
    item_num = len(cookies_list)
    for i in range(item_num):
        name = cookies_list[i]['name']
        value = cookies_list[i]['value']
        name_vaule = name + '=' + value + ';'
        # print(name_vaule)
        cookies_str += name_vaule
    print(cookies_str)
    print('自动化测试结束......')
    update_cookies(cookies_str)
    sleep(1)
    driver.quit()
    # return cookies_str


if __name__ == "__main__":
    verify_and_get_new_cookies()
    print('...................................')