from captcha2upload import CaptchaUpload
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

#to open firefox
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

#Enter the url on which captcha is implemented
print ("Navigating to https://www.bandhanbank.com/recruitment.aspx")
driver.get("https://www.bandhanbank.com/recruitment.aspx")

print ("Finding the captcha image")

#finding the captcha image on the page by its xpath
captcha_img = driver.find_element_by_xpath("//html//body//form//div[4]//div[2]//div[2]//div//div//div[2]//div//ul//li[14]//div//div//img")

#downloading the captcha from the source
src = captcha_img.get_attribute('src')
print (src)

#saving the captcha image as captchanew.png
urllib.urlretrieve(src, "captchanew.png")
print("Identifying captcha characters")

#close firefox
driver.quit()

#invoke the az captcha api
captcha = CaptchaUpload("hxvgz3627mwjjf4mytqcxkdtrqgclzbp") #api key of your azcaptcha account
print captcha.solve("/home/aman/Desktop/Temp_OCR/POC/captchanew.png")
print ("Captcha characters identified")
