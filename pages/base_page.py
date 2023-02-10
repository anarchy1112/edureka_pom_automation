from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from utilities.confreader import confread
import allure

class BasePage:

    def __init__(self, driver):
        self.driver=driver

    def click(self, locator):
        self.driver.find_element(By.XPATH, confread('locators', locator)).click()

    def type(self, locator, value):
        self.driver.find_element(By.XPATH, confread('locators', locator)).send_keys(value)

    def erase(self, locator):
        self.driver.find_element(By.XPATH, confread('locators', locator)).clear()

    def wait_visible(self, section, locator):
        wait=WebDriverWait(self.driver,10)
        wait.until(EC.visibility_of_element_located((By.XPATH, confread(section, locator))))

    def wait_clickable(self, section, locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, confread(section, locator))))

    def right_click(self, locator):
        action=ActionChains(self.driver)
        element=self.driver.find_element(By.XPATH, confread('locators', locator))
        action.context_click(element).perform()

    def mouse_hover(self, locator):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, confread('locators', locator))
        action.move_to_element(element)

    def double_click(self, locator):
        action=ActionChains(self.driver)
        element=self.driver.find_element(By.XPATH, confread('locators', locator))
        action.double_click(element).perform()

    def enable_check(self, locator):
        return self.driver.find_element(By.XPATH, confread('locators', locator)).is_enabled()

    def text_extract(self, section, locator):
        return self.driver.find_element(By.XPATH, confread(section, locator)).text

    def elem(self, locator):
        self.driver.find_element(By.XPATH, confread('locators', locator))

    def elems(self, locator):
        self.driver.find_elements(By.XPATH, confread('locators', locator))

    def drag_and_drop(self, locatordrag, locatordrop):
        action = ActionChains(self.driver)
        dragable = self.driver.find_element(By.XPATH, confread('locators', locatordrag))
        droppable = self.driver.find_element(By.XPATH, confread('locators', locatordrop))
        action.drag_and_drop(dragable, droppable).perform()


    def drag(self, locator, x, y):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, confread('locators', locator))
        action.drag_and_drop_by_offset(element, x, y).perform()

    def click_hold(self, locator):
        action = ActionChains(self.driver)
        element = self.driver.find_element(By.XPATH, confread('locators', locator))
        action.click_and_hold(element).perform()

    def key_enter(self, locator, key_name):   #bit experimental, try it out
        key=getattr(Keys,key_name)
        self.driver.find_element(By.XPATH, confread('locators', locator)).send_keys(key)



    def dropdown_by_value(self, locator, value):
        element = self.driver.find_element(By.XPATH, confread('locators', locator))
        select = Select(element)
        select.select_by_value(value)

    def scrolldown(self, x,y):
        self.driver.execute_script(f"window.scrollTo(0,{y})")

    def attributes(self, locator, value):
        self.driver.find_element(By.XPATH, confread('locators', locator)).get_attribute(value)

    def element_present(self, locator):
        try:
            self.driver.find_element(By.XPATH, confread('locators', locator))
        except NoSuchElementException:
            return False
        return True

    def screenshot(self):
        self.driver.get_screenshot_as_png()

    def alluress(self, name):
        allure.attach(self.driver.get_screenshot_as_png(), name=name, attachment_type=AttachmentType.PNG)