from selenium import webdriver

#To import selenium.webdriver.firefox.firefox_binary.FirefoxBinary module
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#Create FirefoxBinary object by passing Firefox binary file as an argument and assign it to a local variable
binary = FirefoxBinary('path/to/binary')

#Create Firefox browser driver object, and assigns it to a local variable;
#Pass FirefoxBinary object created in previous step as follows, 'binary' in our example
driver = webdriver.Firefox(firefox_binary=binary)