from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
# options.headless = True
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.youtube.com/")