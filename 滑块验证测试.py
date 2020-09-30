from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('https://passport.ctrip.com/user/reg/home')
driver.find_element_by_css_selector("#agr_pop>div.pop_footer>a.reg_btn.reg_agree").click()
sleep(5)
# 获取滑块位置
sour=driver.find_element_by_css_selector("#slideCode>div.cpt-drop-box>div.cpt-drop-btn")
ele=driver.find_element_by_css_selector("#slideCode>div.cpt-drop-box>div.cpt-bg-bar")
# 拖动滑块
ActionChains(driver).drag_and_drop_by_offset(sour,ele.size['width'],-sour.size['height']).perform()