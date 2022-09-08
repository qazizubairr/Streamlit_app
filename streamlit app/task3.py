from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import psycopg2
import psycopg2.extras
import time
from decouple import config
from railway_db import connect, execute


options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--disable-gpu')  # applicable to windows os only
options.add_argument('--log-level=1')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\Program Files (x86)\chromedriver')


page=1
url='https://www.airbnb.com/s/United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&search_type=autocomplete_click&price_min=1500&query=United%20States&place_id=ChIJCzYy5IS16lQRQrfeQ5K5Oxw&date_picker_type=calendar&source=structured_search_input_header&price_filter_input_type=0&federated_search_session_id=a35c0b45-1e0a-4458-849c-7709a8e414bb&pagination_search=true'
try:
    while page==1:
        driver.get(url)
        time.sleep(10)
        new_places = driver.find_elements(By.XPATH,"//div[@class='gh7uyir g1xypvzw g14v8520 dir dir-ltr']/div[@class='c4mnd7m dir dir-ltr']/div[@class='c1l1h97y dir dir-ltr']/div[@itemprop='itemListElement']/div/div/div[@class='cy5jw6o  dir dir-ltr']/div[@class='g1tup9az cb4nyux dir dir-ltr']")
        for place in new_places:
            if 'New' in place.text:
                
                homes=place.find_elements(By.XPATH,"div[@class='t1jojoys dir dir-ltr']")
                address = place.find_elements(By.XPATH,"div[@class='n1v28t5c s1cjsi4j dir dir-ltr']")
                rooms = place.find_elements(By.XPATH,"div[@class='f15liw5s s1cjsi4j dir dir-ltr']/span[contains(@aria-label,'beds')]/span")
                dates = place.find_elements(By.XPATH,"div[@class='f15liw5s s1cjsi4j dir dir-ltr']/span[contains(@aria-label,'–')]/span")
                Rent = place.find_elements(By.XPATH,"div[@class='pquyp1l dir dir-ltr']/div/div/span/span")
                
                for i in range(len(homes)):
                    record_to_insert = (homes[i].text,address[i].text,rooms[i].text,dates[i].text,Rent[i].text)
                    execute(connect(),record_to_insert)
        page+=1
        # try:
        #     linkss= driver.find_element(By.XPATH,"//a[@aria-label='Next']")
        #     url =linkss.get_attribute("href")
        # except NoSuchElementException as e:
        #     print(e)
        #     break
except Exception as e:
    print(e)
finally:
    driver.quit()