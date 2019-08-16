from selenium.webdriver import ActionChains
from selenium.webdriver import Chrome
from time import sleep

"""
Automating a manual scenario when a user hovers over an element (for 
example, a question mark), and additional popup displayed
"""


# Function:
def hover_over_element(web_element):
    actions = ActionChains(driver)
    actions.move_to_element(web_element)
    actions.perform()


# Usage
URL = "https://medium.com/"
driver = Chrome()
driver.get(URL)

first_author_link = driver.find_elements_by_xpath(
    "//a[contains(@class, '--author')]")[0]


hover_over_element(first_author_link)

# Here you can look at the browser and see the popup
sleep(5)

driver.quit()
