# Alicja Wiacek s22749
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import requests

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.pap.pl/')
#a zaakceptuje pliki cookies
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cookies .ok'))).click()
#b zwiekszy okno przegladarki na caly ekran
driver.maximize_window()
#c zmieni jezyk strony na angielski
driver.get('https://www.pap.pl/en')
# d Wejdzie w sekcję Business
driver.get('https://www.pap.pl/en/Business')
# e Z sekcji business ściągnie wszystkie tytuły do listy titles
titles = []
elem1 = driver.find_elements(By.CSS_SELECTOR, '.title')
for p in elem1:
    titles.append(p.text)
print(titles)

# f Ściągnie wszystkie zdjęcia z tej sekcji na dysk lokalny
elem2 = driver.find_elements(By.CSS_SELECTOR, 'img')
i = 0
for p in elem2:
    img_data = requests.get(p.get_attribute("src")).content
    with open(str(i)+'.jpg', 'wb') as handler:
        handler.write(img_data)
        i += 1

# g Zjedzie na dół strony
button_id = '/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[6]/a/span[2]'
button = driver.find_element(By.XPATH, '/html/body/div/div[2]/section[2]/div/div[2]/div[1]/div[2]/div/nav/ul/li[6]/a/span[2]')

actions = ActionChains(driver)
actions.move_to_element(button).perform()

# h Przejdzie na ostatnią stronę i zwróci printem jej numer (atrybut text)
button.click()

time.sleep(10)
driver.close()