from selenium import webdriver
import time

def testDeleteGroup():
  path = '../bin/chromedriver'
  browser = webdriver.Chrome(path)
  browser.get("https://www.fangcloud.com/auth/login")
  time.sleep(2)
  browser.find_element_by_id("login").send_keys("656032372@qq.com")
  browser.find_element_by_id("password").send_keys("pass123456")
  browser.find_element_by_id("login_btn").click()
  time.sleep(3)
  #点击企业控制台
  browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/a/i').click()
  time.sleep(2)
  browser.switch_to_window(browser.window_handles[1])
  #点击部门与成员
  browser.find_element_by_xpath('//div/div[2]/div/div[2]/ul/li[1]/a').click()
  time.sleep(5)
  for i in range(546):
    deleteElements(browser)
  # if browser.find_element_by_xpath("//div[3]/div[1]")!=None:
  #     time.sleep(1)
  #     browser.find_element_by_xpath("/html/body/div[2]/div[3]/button").click()
  #     time.sleep(1)
  #     browser.find_element_by_xpath("//*[@id='etn134529']/i").click()

def isElementExist(browser, element):
  flag = True
  try:
    browser.find_element_by_xpath(element)
    return flag
  except:
    flag = False
    return flag

def deleteElements(browser):
  time.sleep(1)
  # 明源
  browser.find_element_by_xpath("//div/ul/li/ul/li/div/i").click()
  time.sleep(1)
  browser.find_element_by_xpath("//div/ul/li/ul/li/ul/li/div/i").click()
  time.sleep(1)
  flag = isElementExist(browser, "//div/ul/li/ul/li/ul/li/ul/li")
  print(flag)
  if flag is False:
    time.sleep(1)
    browser.find_element_by_xpath("//div/ul/li/ul/li/ul/li").click()
    time.sleep(1)
    browser.find_element_by_xpath("//div[1]/div/div/div/a[contains(text(), '删除')]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//button[contains(text(), '删除部门')]").click()
    time.sleep(4)
  else:
    time.sleep(1)
    browser.find_element_by_xpath("//div/ul/li/ul/li/ul/li/ul/li").click()
    time.sleep(3)
    browser.find_element_by_xpath("//div[1]/div/div/div/a[contains(text(), '删除')]").click()
    time.sleep(1)
    browser.find_element_by_xpath("//button[contains(text(), '删除部门')]").click()
    time.sleep(2)
    reflag = isElementExist(browser,"//div/div[contains(text(),'部门无法删除')]")

    if reflag is True:
        # 知道了
        time.sleep(2)
        browser.find_element_by_xpath("//div/div/button[contains(text(),'知道了')]").click()
        time.sleep(0.5)
        browser.find_element_by_xpath("//div[2]/div/div[2]/ul/li/ul/li/ul/li/ul/li/div/i").click()
        time.sleep(2)
        browser.find_element_by_xpath("//div[2]/div/div[2]/ul/li/ul/li/ul/li/ul/li/ul").click()
        time.sleep(2)
        browser.find_element_by_xpath("//div[1]/div/div/div/a[contains(text(), '删除')]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//button[contains(text(), '删除部门')]").click()
    time.sleep(2)

