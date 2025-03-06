from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://chromereleases.googleblog.com/search?updated-max=2025-02-19T07:28:00-08:00&max-results=7')
string_to_search = "Stable Channel Update for Desktop"
# Find all elements containing the string (for example, in paragraph tags)
elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{string_to_search}')]")
# Print out the text of each element found
for element in elements:
    print(element.text)
# If elements were found, take a screenshot
if elements:
    for index, element in enumerate(elements):
        # Get the location and size of the element
        location = element.location
        size = element.size
        screenshot_path_chromerelease= 'C:\\Users\\DELL\\OneDrive\\Pictures\\Selenium_Screenshot\chromerelease_screenshot.png'
        # Take a screenshot of the entire page
        driver.save_screenshot(screenshot_path_chromerelease)
        # Crop the screenshot to the size of the element
# Close the driver
driver.quit()