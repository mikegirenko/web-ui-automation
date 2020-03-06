from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

"""
Several methods to remove test from an input field. As I was  working, I found that usual .clear() method no
longer works (because our FE team started using Design Language to build UI). So, I had to find workaround.
"""

URL = 'https://www.google.com/'
driver = Chrome()
driver.get(URL)
text_input_field = driver.find_element_by_name('q')


def remove_text_using_clear_method():
    text_input_field.send_keys('remove using clear() method')
    text_input_field.clear()
    assert text_input_field.text == '', 'Text was not removed'


def remove_text_using_my_workaround():
    text_input_field.send_keys('remove using my workaround')
    text_input_field.send_keys(Keys.CONTROL, "a")
    length = len(text_input_field.get_attribute('value'))
    text_input_field.send_keys(length * Keys.BACKSPACE)
    assert text_input_field.text == '', 'Text was not removed'


def remove_using_keys_delete():
    text_input_field.send_keys('remove using Keys.DELETE')
    text_input_field.send_keys(Keys.CONTROL, "a")
    text_input_field.send_keys(Keys.DELETE)
    assert text_input_field.text == '', 'Text was not removed'


remove_text_using_clear_method()
remove_text_using_my_workaround()
remove_using_keys_delete()

driver.quit()
