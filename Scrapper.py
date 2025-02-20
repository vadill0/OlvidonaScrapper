from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# basic setup
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
driver.get("https://www.youtube.com/@TheWildProject")

time.sleep(1.5)

# accept cookies
cookiesButton = driver.find_element(By.XPATH, '//*[contains(@aria-label, "Accept all")]')
cookiesButton.click()
time.sleep(1.5)

# scroll into view to THE WILD PROJECT PODCAST
podcastTitle = driver.find_element(By.XPATH, '//*[contains(@title, "THE WILD PROJECT PODCAST")]')
driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'start'})", podcastTitle)

# collect items from video container && write to file
with open("WILD PROJECT PODCASTS.txt", "w") as file:
    file.write("Latest WILD PROJECT PODCAST videos:\n")
    for it in range(1,6):
        link = driver.find_element(By.XPATH,f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer[2]/div[3]/ytd-shelf-renderer/div[1]/div[2]/yt-horizontal-list-renderer/div[2]/div/div/ytd-grid-video-renderer[{it}]/div[1]/ytd-thumbnail/a').get_attribute("href")
        file.write(f"\t{it}. {link}\n")
   