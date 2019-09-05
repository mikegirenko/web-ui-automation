from selenium.webdriver import Chrome

""""
A simple way to count the number of rows in an HTML table
"""

URL = 'https://www.w3schools.com/html/html_tables.asp'

driver = Chrome()

driver.get(URL)


def get_table():
    table = driver.find_element_by_id('customers')
    return table


def get_rows():
    table = get_table()
    rows = table.find_elements_by_tag_name('tr')
    return rows


def count_rows():
    return len(get_rows())


print("There are", count_rows(), "rows in this table")

driver.quit()
