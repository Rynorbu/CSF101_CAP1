from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


option = Options()
option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

driver.get("https://www.facebook.com/")


login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'login')))

username_field = driver.find_element(By.XPATH, '//*[@id="email"]')
username_field.send_keys("******")
password_field = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_field.send_keys("*****")
login_button.click()
driver.maximize_window()

# Wait for login to complete
time.sleep(5)

# Navigate to the Facebook group
driver.get("https://www.facebook.com/groups/4088646741264659")

# Scroll through the posts
for i in range(10):  # Adjust this number based on the number of posts you want to like
    # scroll down to the buttom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)  # Wait for the page to load

driver.quit()


