from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome

"""
Count number of elements which have the same locator
"""

URL = 'https://www.google.com/'

driver = Chrome()

driver.get(URL)


def count_elements_on_page(name):
    elements = driver.find_elements_by_name(name)
    if not elements:
        raise NoSuchElementException('Nothing matched')
    count = len(elements)
    return count


print(count_elements_on_page('btnK'))

driver.quit()
