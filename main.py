import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (presence_of_element_located)

########################################################################################################################
# -------------------------------------------------Chromme Driver Config-----------------------------------------------#
########################################################################################################################

chrome_options = Options()
chrome_options.page_load_strategy = 'eager'
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_experimental_option("prefs", {
    'safebrowsing.enabled': True,
    "credentials_enable_service": False,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True,
    "profile": {"password_manager_enabled": False}})
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
# service = Service(r'Z:\#Pasta Publica\Diretorio Publico\Lucas Lucena\workspace\chromedriver.exe')
service = Service('chromedriver.exe')
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {
    "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'
                 '537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})

download_path = rf'F:\Musicas evangelho'
driver.execute_cdp_cmd('Page.setDownloadBehavior', {'behavior': 'allow', 'downloadPath': download_path})
main_page = 'https://x2download.app/pt41/download-youtube-to-mp3'

yt_links = [
    'https://youtu.be/Q_34yVWOlvg',
    'https://youtu.be/ej3h6WxEKJs',
    'https://youtu.be/3R4AfxziJ40',
    'https://youtu.be/nN7wuf2e6Cc',
    'https://youtu.be/nPffL3cNGrs',
    'https://youtu.be/TqyLnMa3DJw',
    'https://youtu.be/fcSdCXoQzGI',
    'https://youtu.be/duhTLY6aTF4',
    'https://youtu.be/uGKtc9gz3Gs',
    'https://youtu.be/dJqwOvuV7A8',
    'https://youtu.be/F9LLcipqXro',
    'https://youtu.be/F9LLcipqXro',
    'https://youtu.be/F9LLcipqXro',
    'https://youtu.be/F9LLcipqXro',
    'https://youtu.be/3R4AfxziJ4',
    'https://youtu.be/7sIm18KQv4o',
    'https://youtu.be/Y0plyNaxy30',
    'https://youtu.be/hlWiI4xVXKY',
    'https://youtu.be/Lp6XlsBm_Lw',
    'https://youtu.be/FMrtSHAAPhM'
]

errors = []
for i in yt_links:

    driver.get(main_page)
    try:
        driver.find_element(By.XPATH, '//*[@id="s_input"]').send_keys(i)  # Insert yt link
        sleep(5)
        button = driver.find_element(By.XPATH, '//*[@id="search-form"]/button')
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, '//*[@id="search-form"]/button').click()  # Search link
        sleep(5)
        button = driver.find_element(By.XPATH, '//*[@id="btn-action"]')
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, '//*[@id="btn-action"]').click()  # Get link
        sleep(5)
        button = driver.find_element(By.XPATH, '//*[@id="asuccess"]')
        driver.execute_script("arguments[0].click();", button)
        # driver.find_element(By.XPATH, '//*[@id="asuccess"]').click()  # Download mp3
        sleep(5)
        while any(['.crdownload' in i for i in os.listdir(download_path)]):
            sleep(1)
    except:
        errors.append(i)
        print('ops')
print(errors)
