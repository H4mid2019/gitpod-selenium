from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
# Important Arguments, won't run without them in Gitpod
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("--headless")  

# Setup ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()
