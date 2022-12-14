from selenium import webdriver
from selenium.webdriver import Keys, DesiredCapabilities
#
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.options import Options as InternetExplorerOptions
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
ieoptions = InternetExplorerOptions()
ieoptions.ignore_protected_mode_settings = True



def func_1():

    print('##### func 1  - start #####')

    walla_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    ynet_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    walla_driver.get("http://www.walla.co.il")
    ynet_driver.get("http://www.ynet.co.il")
    ynet_driver.close()
    walla_driver.close()

    print('##### func 1  - complete #####\n')



def func_2():

    print('##### func 2 #####')
    ynet_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    ynet_driver.get("http://www.ynet.co.il")
    ynet_title = ynet_driver.title
    print(f' ynet title is - {ynet_title}')
    ynet_driver.refresh()
    if ynet_driver.title == ynet_title:
        print('title after refresh equals to ynet_title variable')
    ynet_driver.close()

    print('##### func 2  - complete #####\n')

#3
def func_3():

    print('##### func 3 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    firefox_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    edge_driver = webdriver.Edge()

    chrome_driver.get("http://www.google.com")
    firefox_driver.get("http://www.google.com")
    edge_driver.get("http://www.google.com")

    one = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    two = firefox_driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    three = edge_driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    print(f'one - {one}')
    print(f'two - {two}')
    print(f'three - {three}')

    print('location will be the same because xpath are the same - however every session will generate different hash')

    firefox_driver.close()
    edge_driver.close()
    chrome_driver.close()

    print('##### func 3  - complete #####\n')
#4
def func_4():

    print('##### func 4 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://translate.google.com")
    chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea').send_keys('מה שלומך אין בכלל כפתור')

    x = input("please enter to continue to the next solution \n")
    chrome_driver.close()

    print('##### func 4  - complete #####\n')
#5
def func_5():

    print('##### func 5 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://www.youtube.com")
    chrome_driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys("stairway to heaven")
    chrome_driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]').click()

    x = input("please enter to continue to the next solution \n")

    chrome_driver.close()
    print('##### func 5  - complete #####\n')

def func_6():

    print('##### func 6 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://translate.google.com")
    a = chrome_driver.find_element(By.CSS_SELECTOR, '[aria-label="Source text"]')
    b = chrome_driver.find_element(By.CLASS_NAME, 'er8xn')
    c = chrome_driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea')
    print(f'css_selector "a = {a} \n class_name "b" = {b}  \n  xpath "c" = {c}')


    chrome_driver.close()
    print('##### func 6  - complete #####\n')

def func_7():

    print('##### func 7 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://www.facebook.com")
    chrome_driver.find_element(By.NAME, "email").send_keys("idonthavefacebook")
    chrome_driver.find_element(By.NAME, "pass").send_keys("nonono")
    chrome_driver.find_element(By.NAME, "login").click()

    x = input("please enter to continue to the next solution ")

    chrome_driver.close()
    print('##### func 7  - complete #####\n')
def func_8():

    print('##### func 8 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://www.stackoverflow.com")
    cookie = chrome_driver.get_cookies()
    print(f'Here are Cookies that are on right now :  {cookie}')
    chrome_driver.delete_all_cookies()
    cookie = chrome_driver.get_cookies()
    print(f'Here are Cookies after deletion :  {cookie}')

    x = input("please enter to continue to the next solution ")

    chrome_driver.close()
    print('##### func 8  - complete #####\n')
def func_9():

    print('##### func 9 #####')
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))

    chrome_driver.get("https://github.com")
    chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[1]/div[2]/button').click()    # enter = input("Please enter for search")
    search = chrome_driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label')
    ent = "Selenium"
    search.send_keys(ent)

    # enter = input("Please enter for search")
    # print(enter)
    # while enter != "":
    #     enter = input("wrong key entered, Please enter for search\n")
    search.send_keys(Keys.ENTER)
    print(f'You have searched for "{ent}" , \nhere is the link for results - {chrome_driver.current_url}, browser will open in few seconds\n')
    # just to get it focused again :

    close = input("Please enter any key to close the Browser")
    chrome_driver.close()
    print('##### func 9  - complete #####\n')
def func_10():

    print('##### func 10 #####')
    chrome_options.add_argument("--disable-extensions")
    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://www.github.com")
    # # firefox_capabilities = DesiredCapabilities.FIREFOX
    # firefox_profile = Options()
    # print(firefox_profile)
    # firefox_driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), firefox_profile = firefox_profile)
    #edge_driver = webdriver.Edge()
    # ie_options = InternetExplorerOptions()
    # ie_driver = webdriver.Ie(options=ie_options, service=IEService(IEDriverManager().install()))
    # ie_driver.get("https://www.google.co.il")

    close = input("Please enter any key to close the Browser")

    ## did it just for chrome other methods cant be found unless we do new profiling
    chrome_driver.close()
    # ie_driver.close()
    print('##### func 10  - complete #####\n')
def func_11():

    print('##### func 11 #####')
    # loading with gecko is without extensions

    chrome_driver = webdriver.Chrome(options=chrome_options, service=Service(ChromeDriverManager().install()))
    chrome_driver.get("https://github.com")
    close = input("Please enter any key to close the Browser")


    chrome_driver.close()
    print('##### func 11  - complete #####\n')


#####################################################
###          Questions - and - Solutions          ###
#####################################################

    # 1. Write a script which will open the following:
    # a. Chrome – http://www.walla.co.il
    # b. Firefox – http://www.ynet.co.il

# func_1()
#
#     # 2. In one of the browsers you have open, do the following:
#     # a. Create a variable with the website’s title
#     # b. Refresh website
#     # c. Get website name and compare it to the variable you created in clause 1
#
# func_2()
#
#     # 3. Open a few browsers, locate any element, does the element has the same locator in
#     # the other browser?
#
# func_3()
#
#     # 4. Create a test with the following:
#     # a. Open Google Translate web page
#     # b. Write anything in Hebrew in the text area
#
# func_4()
#
#     # 5. Open Youtube web page
#     # a. Type a name of a song
#     # b. Click on search.
#
# func_5()
#
#     # 6. Open Chrome browser on Google Translate website: https://translate.google.com/
#     # a. Find translation text field (the one you send keys to) with 3 different locators and
#     # print the WebElement you created.
#
# func_6()
#
#     # 7. Open Chrome browser on Facebook website https://www.facebook.com/
#     # a. Login into Facebook (No need to send me credentials).
#
# func_7()
#
#     # Challenges:
#     # 8. Open Chrome browser on any webpage:
#     # a. Delete all cookies from browser.
#     # b. Make sure all cookies are deleted by printing all cookies stored in the browser.
#
# func_8()
#
#     # 9. Open any browser on "Github" website https://github.com/
#     # a. Enter “Selenium” keyword in search textfield
#     # b. Press Enter to search (through code - of course).
#
# func_9()

    # 10.Find a way to disable all extensions in
    # a. Chrome

    # b. Firefox
    # - didnt find a way

    # c. Explorer
    # -  didnt find a way

func_10()

    # 11.Find a way to start a browser without extensions.
    # loading with gecko is without extensions

func_11()


