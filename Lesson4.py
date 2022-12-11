from selenium import webdriver
#
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

def func_1():
    walla_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    ynet_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    walla_driver.get("http://www.walla.co.il")
    ynet_driver.get("http://www.ynet.co.il")
    ynet_driver.close()
    walla_driver.close()

def func_2():
    ynet_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    ynet_driver.get("http://www.ynet.co.il")
    ynet_title = ynet_driver.title
    print(f' ynet title is - {ynet_title}')
    ynet_driver.refresh()
    if ynet_driver.title == ynet_title:
        print('title after refresh equals to ynet_title variable')
    ynet_driver.close()

#3
def func_3():
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    firefox_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    edge_driver = webdriver.Edge()

    chrome_driver.get("http://google.com")
    firefox_driver.get("http://google.com")
    edge_driver.get("http://google.com")

    one = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/img')
    two = firefox_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/img')
    three = edge_driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/img')
    print(f'one - {one}')
    print(f'two - {two}')
    print(f'three - {three}')

    print('location will be the same because xpath are the same - however every session will generate different hash')

    firefox_driver.close()
    edge_driver.close()
    chrome_driver.close()


#4
def func_4():
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://translate.google.com")
    chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys('מה שלומך אין בכלל כפתור')
    chrome_driver.close()
#5
def func_5():
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://www.youtube.com")
    chrome_driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("stairway to heaven")
    chrome_driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()
    chrome_driver.close()


def func_6():
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://translate.google.com")
    a = chrome_driver.find_element(By.CSS_SELECTOR, '[aria-label="Source text"]')
    b = chrome_driver.find_element(By.CLASS_NAME, 'er8xn')
    c = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
    print(f'css_selector "a = {a} \n class_name "b" = {b}  \n  xpath "c" = {c}')
    chrome_driver.close()

def func_7():
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://www.facebook.com")
    chrome_driver.find_element(By.NAME, "email").send_keys("idonthavefacebook")
    chrome_driver.find_element(By.NAME, "pass").send_keys("nonono")
    chrome_driver.find_element(By.NAME, "login").click()


func_7()