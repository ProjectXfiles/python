from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = 'https://github.com/ProjectXfiles/python.git'

chrome_driver = ChromeDriverManager().install()
driver = Chrome(service = Service(chrome_driver))
driver.maximize_window()
driver.get(link)



input()