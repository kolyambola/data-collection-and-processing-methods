from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import TimeoutException

s = Service('./msedgedriver.exe')

edge_options = Options()
edge_options.add_argument('start-maximized')

driver = webdriver.Edge(service=s, options=edge_options)
driver.implicitly_wait(15)
driver.get("https://5ka.ru/special_offers")

button_location = driver.find_element(By.XPATH, "//button[contains(@class, 'location-confirm__button')]")
button_location.click()

button_cookie = driver.find_element(By.XPATH, "//div[@class='cookie-message page-container']//button")
button_cookie.click()

i = 0
while i < 3:
    wait = WebDriverWait(driver, 15)
    try:
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-more-btn']")))
        next_button.click()
        i += 1
    except TimeoutException:
        print("Scroll finished")
        break

goods = driver.find_elements(By.XPATH, "//div[@class='product-card item']")
for good in goods:
    name = good.find_element(By.XPATH, "//div[@class='item-name']").text
    price = good.find_element(By.XPATH, "//span[@data-v-2d064667]").text
