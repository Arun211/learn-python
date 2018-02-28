from selenium import webdriver

driver = webdriver.Firefox(executable_path='[Browser Driver Path]');
driver.get('[URL to Open]');

driver.find_element_by_id('username').send_keys('admin');
driver.find_element_by_id('password').send_keys('admin');
driver.find_element_by_id('login').click();

#/usr/local/lib/python2.7/dist-packages/selenium/webdriver/remote/webdriver.py:907: UserWarning: name used for saved screenshot does not match file type. It should end with a `.png` extension
# "type. It should end with a `.png` extension", UserWarning)

driver.save_screenshot('/data/WorkArea/sample_screenshot_1.png');

driver.get_screenshot_as_file('/data/WorkArea/sample_screenshot_2.png');

# Webdriver offers others API like get_screenshot_as_png() which return a binary.
# This will create an image in memory and can be useful if we want to manipulate before saving it.
driver.get_screenshot_as_png();

