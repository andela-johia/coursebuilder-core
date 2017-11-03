"""To test, create a virtualenv and pip install selenium
Then run python tests/integration/course_carousel_test.py to test"""

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class CarouselNavigationTest(unittest.TestCase):
    def setUp(self):
        """Assign driver to chrome driver."""
        self.driver = webdriver.Chrome()

    def test_no_carousel_movement_in_carousel_content(self):
        """Assert no carousel movement when the user clicks inside the carousel"""
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("https://johnboscoohia-dot-cfafrica-mooc-dev.appspot.com/test/unit?unit=4&lesson=12")
        driver.maximize_window()
        self.assertIn("Test - - Unit 2 - Unit 2", driver.title)
        driver.find_element_by_tag_name("body")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element = driver.find_element_by_id("7MD2r4aHrXrY").find_element_by_tag_name("input")
        element.send_keys("The react basics")
        ActionChains(driver) \
            .key_down(Keys.ARROW_LEFT) \
            .key_down(Keys.ARROW_LEFT) \
            .perform()
        self.assertTrue(driver.find_element_by_id("7MD2r4aHrXrY"))

    def test_carousel_movement_outside_carousel_content(self):
        """Assert movement of the carousel when the user clicks outside the carousel content."""
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("https://johnboscoohia-dot-cfafrica-mooc-dev.appspot.com/test/unit?unit=4&lesson=12")
        driver.maximize_window()
        ActionChains(driver) \
            .key_down(Keys.ARROW_DOWN) \
            .perform()
        carousel_nav = driver.find_element_by_class_name("owl-next")
        ActionChains(driver) \
            .click(carousel_nav) \
            .send_keys(Keys.ARROW_RIGHT) \
            .perform()
        new_element = driver.find_element_by_css_selector("div#NycYrhJOAbuy")
        self.assertTrue(new_element)
        owl_next = driver.find_element_by_class_name("owl-next")
        ActionChains(driver) \
            .click(owl_next) \
            .send_keys(Keys.ARROW_RIGHT) \
            .perform()
        element = driver.find_element_by_css_selector("div#nwdacawc64qe")
        self.assertTrue(element)
        carousel_element = driver.find_element_by_class_name('qt-check-answer-button')
        ActionChains(driver) \
            .click(carousel_element) \
            .key_down(Keys.ARROW_RIGHT) \
            .perform()
        self.assertTrue(driver.find_element_by_id("NycYrhJOAbuy"))
        ActionChains(driver) \
            .key_down(Keys.ARROW_RIGHT) \
            .perform()
        self.assertTrue(driver.find_element_by_id("nwdacawc64qe"))

    def test_multiple_carousels_movement(self):
        """Assert movement of a carousel does not affect the movement of the other carousels present."""
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("https://johnboscoohia-dot-cfafrica-mooc-dev.appspot.com/test/unit?unit=1&lesson=2")
        driver.maximize_window()
        driver.find_element_by_tag_name("body")
        first_carousel_content = driver.find_element_by_class_name("gcb-video-container")
        self.assertTrue(first_carousel_content)
        ActionChains(driver) \
            .key_down(Keys.ARROW_DOWN) \
            .perform()
        element = driver.find_element_by_class_name("owl-next")
        ActionChains(driver) \
            .click(element) \
            .send_keys(Keys.ARROW_RIGHT) \
            .key_down(Keys.ARROW_DOWN) \
            .perform()
        second_carousel_content = driver.find_element_by_css_selector("div#kuIF4OOWMh0J")
        self.assertTrue(second_carousel_content)

    def test_individual_carousel_movement(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("https://johnboscoohia-dot-cfafrica-mooc-dev.appspot.com/test/unit?unit=4&lesson=11")
        driver.maximize_window()
        first_carousel = driver.find_element_by_class_name("owl-carousel")
        ActionChains(driver).click(first_carousel)\
            .key_down(Keys.ARROW_RIGHT)\
            .key_down(Keys.ARROW_RIGHT)\
            .perform()
        self.assertTrue(driver.find_element_by_css_selector("div.owl-item"))

    def test_no_carousel_movement_with_radio_buttons(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("https://johnboscoohia-dot-cfafrica-mooc-dev.appspot.com/test/unit?unit=4&lesson=11")
        driver.maximize_window()
        first_carousel_content = driver.find_element_by_class_name("owl-carousel")
        ActionChains(driver).click(first_carousel_content).key_down(Keys.ARROW_RIGHT).perform()
        second_carousel_content = driver.find_element_by_css_selector("input#test1")
        ActionChains(driver)\
            .click(second_carousel_content)\
            .key_down(Keys.ARROW_RIGHT)\
            .key_down(Keys.ARROW_RIGHT)\
            .key_down(Keys.ARROW_LEFT)\
            .perform()
        self.assertTrue(driver.find_element_by_css_selector("input#test1"))
        self.assertTrue(driver.find_element_by_css_selector("input#test2"))
        self.assertTrue(driver.find_element_by_css_selector("input#test3"))
        self.assertTrue(driver.find_element_by_css_selector("input#test4"))

    def test_no_carousel_movement_inside_code_mirror(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get("https://johnboscoohia-dot-cfafrica-mooc-dev.appspot.com/test/unit?unit=4&lesson=17")
        driver.maximize_window()
        first_carousel_content = driver.find_element_by_class_name("owl-carousel")
        ActionChains(driver).click(first_carousel_content).key_down(Keys.ARROW_RIGHT).perform()
        second_carousel = driver.find_element_by_css_selector("span.cm-variable")
        ActionChains(driver).click(second_carousel).key_down(Keys.ARROW_RIGHT).key_down(Keys.ARROW_RIGHT).perform()
        self.assertTrue(driver.find_element_by_css_selector("span.cm-variable"))
        self.assertTrue((driver.find_element_by_tag_name("span")))

    def tearDown(self):
        """terminate driver."""
        self.driver.close()


if __name__ == '__main__':
    unittest.main()