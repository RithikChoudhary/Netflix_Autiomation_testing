
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path=r'c:\Users\rchoudhary.CORP\Downloads\geckodriver-v0.31.0-win64\geckodriver')  

#Accessing the netflix trailer page
driver.get("https://www.netflix.com/in/browse/genre/839338")
driver.find_element(By.XPATH,"//*[@id='appMountPoint']/div/div[2]/main/section[2]/div/ul/li[1]/a/img").click()

#Star cast 
Star_cast = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/span[2]").text
print("Star Case of the movie = "+Star_cast)

#description of the movie
description = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/section[1]/div[1]/div[1]/div[2]/div/div[2]/div[1]").text
print("Description - "+ description)

#play trailer 
driver.find_element(By.CSS_SELECTOR,"li.nm-content-horizontal-row-item:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1) > svg:nth-child(2) > g:nth-child(1) > path:nth-child(2)").click()
time.sleep(10)

print("End of the Show")


driver.quit()



