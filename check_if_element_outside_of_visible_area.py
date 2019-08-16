from selenium.webdriver import Chrome

"""
Automating the below manual scenario:
1. A page has several input fields, all of them required
2. User populated all but one input field and clicked Submit
3. The page scrolls up. User can see input fields but cannot see Submit button

Note that automation of these type of test may not be super reliable.  
Different screen resolution or different size of monitor may cause this 
automated test to fail
"""


# Function
def is_element_visible(element):

    scroll_position_script = """
        var pageY;
        if (typeof(window.pageYOffset) == 'number') {
            pageY = window.pageYOffset;
        } else {
            pageY = document.documentElement.scrollTop;
        }
        return pageY;
    """

    y_offset = driver.execute_script(scroll_position_script)

    js_client_height = "return document.documentElement.clientHeight;"
    browser_height = driver.execute_script(js_client_height)

    elem_yloc = int(element.location['y'])
    return bool(y_offset <= elem_yloc <= y_offset + browser_height)


# Usage
URL = 'https://stackoverflow.com/'

driver = Chrome()

driver.get(URL)

for_businesses_button = driver.find_element_by_xpath(
    "//a[contains(text(), 'For businesses')]")

# Confirm button element is visible
assert is_element_visible(for_businesses_button)

# Scroll the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Confirm button element is not visible
assert not is_element_visible(for_businesses_button)

driver.quit()
