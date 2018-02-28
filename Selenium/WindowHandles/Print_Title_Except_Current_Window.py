from selenium import webdriver

driver = webdriver.Firefox(executable_path="/data/Softwares/BrowserDrivers/geckodriver");
driver.get("file:///data/WorkArea/Python_Test.html");

driver.find_element_by_id("link").click();

handles = driver.window_handles;
size = len(handles);
for x in range(size):
	if handles[x] != driver.current_window_handle:
		driver.switch_to.window(handles[x]);
		print driver.title;

driver.quit();