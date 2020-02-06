from captcha2upload import CaptchaUpload
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

#to open firefox
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.maximize_window()

#Enter the url on which captcha is implemented..for now paste url here
print ("Navigating to https://example.com")
driver.get("https:example.com")

print ("Finding the captcha image")

#finding the captcha image on the page by its xpath..for now hardcode the xpath here
captcha_img = driver.find_element_by_xpath("paste xpath here")

#downloading the captcha from the source
src = captcha_img.get_attribute('src')
print (src)

#saving the captcha image as captchanew.png
urllib.urlretrieve(src, "captchanew.png")
print("Identifying captcha characters")

#close firefox
driver.quit()

#invoke the az captcha api
captcha = CaptchaUpload("yourapikey") #api key of your azcaptcha account
print captcha.solve("/path/to/save/image/captchanew.png")
print ("Captcha characters identified")
