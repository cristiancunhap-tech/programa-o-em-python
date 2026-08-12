from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal")
    driver.fullscreen_window()
    time.sleep(5)

    search = driver.find_element(By.NAME, "search")
    search.send_keys("SENAC")
    time.sleep(20)

    driver.find_element(By.CSS_SELECTOR, ".cdx-menu__listbox li:first-child a").click()
    time.sleep(5)

    elemento_texto = driver.find_element(By.ID,"mwEQ").text

    time.sleep(20)
    

finally:
    driver.quit()