from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import itertools

BASE_URL = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase'
PASSWORD = 'myPassword!'

with open('english.txt') as f:
    WORDLIST = f.read().splitlines()


def login():

    ## HEADLESS MODE SELECTION
    headless_mode = False

    if headless_mode:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # DISABLE CHROME NOTIFICATIONS
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)
        try:
            #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver_86.bck", chrome_options=options)
            driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)
        except:
            driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver_88.bck")
            #driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    else:
        
        try:
            # DISABLE CHROME NOTIFICATIONS
            options = webdriver.ChromeOptions()
            prefs = {"profile.default_content_setting_values.notifications" : 2}
            options.add_experimental_option("prefs",prefs)
            options.add_extension("nkbihfbeogaeaoehlefnkodbefgpgknn.crx")
            driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver_88.bck", chrome_options=options)

        except:
            driver = webdriver.Chrome("chromedriver")
            

    driver.get(BASE_URL)

    ## ALL COMBINATIONS (to much for one pc)
    #print(len(list(itertools.permutations(WORDLIST,12))))

    #for x in list(itertools.permutations(WORDLIST,12)):
    for x in list(itertools.permutations(WORDLIST,2)):
        seed = ''
        for word in x:
            seed+=word+' '
        print(seed)   
        driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input').send_keys(seed)
        driver.find_element_by_xpath('//*[@id="password"]').send_keys(PASSWORD)
        driver.find_element_by_xpath('//*[@id="confirm-password"]').send_keys(PASSWORD)
        source_code = driver.page_source

        if 'Frase semilla no válida.' not in source_code:
            print(seed)
        

    
    return driver


login()
