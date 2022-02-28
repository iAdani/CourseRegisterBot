from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

# Time settings
sleepTime = 0.5
waitTime = 20

# Setting the driver
driver = webdriver.Chrome("chromedriver")

# Login info
ID = "208642884"
code = "Fuckyouhacker5"

# Load page
driver.get("https://inbar.biu.ac.il/live/Login.aspx")
driver.maximize_window()
time.sleep(sleepTime)

# Logging in
username = driver.find_element_by_id("edtUsername")
username.clear()
username.send_keys(ID)

password = driver.find_element_by_id("edtPassword")
password.clear()
password.send_keys(code)
time.sleep(sleepTime)

driver.find_element_by_name("btnLogin").click()
time.sleep(sleepTime)

# Going into the Course Registration System
driver.find_element_by_id("tvMainn10").click()
time.sleep(sleepTime)

# Closing annoying window
driver.find_element_by_id("ContentPlaceHolder1_btnCloseThresholdRemark").click()
time.sleep(sleepTime)

# Open list
driver.find_element_by_id("tbActions_ctl04_btnAddLessons").click()
time.sleep(sleepTime)

# Closing annoying window
driver.find_element_by_id("ContentPlaceHolder1_btnCloseThresholdRemark").click()
time.sleep(sleepTime)

# Scrolling
scrollList = driver.find_elements_by_xpath("//tr[@class='GridRow']")
scrollLimit = 5
for cell in scrollList:
    if scrollLimit % 2 == 1:
        continue
    driver.execute_script("arguments[0].scrollIntoView();", cell)
    time.sleep(1)
    if scrollLimit <= 0:
        break
    scrollLimit -= 1
driver.find_element_by_id("ContentPlaceHolder1_gvBalance_lblBalanceName_11").click()

# Refreshing
for i in range(1, 10000):
    time.sleep(waitTime)
    try:
        driver.find_element_by_id("ContentPlaceHolder1_gvLinkToLessons_btnLinkStudentToLesson_0").click()
        break
    except NoSuchElementException:
        driver.refresh()

# Closing the window
# driver.close()

