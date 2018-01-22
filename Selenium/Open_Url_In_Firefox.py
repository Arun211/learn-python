#import selenium webdriver module 
from selenium import webdriver

#Create Firefox browser driver object, and assigns it to a local object
driver = webdriver.Firefox();

#get('url') method opens given url in Firebox browser launched in previous step
driver.get("http://www.google.com");