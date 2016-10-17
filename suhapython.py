# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os


class Suha(unittest.TestCase):
    def setUp(self):
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(1)
        self.base_url = "https://scholarshipuniverse.arizona.edu/suha"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_suha(self):
        driver = self.driver
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import os


class Suha(unittest.TestCase):
    def setUp(self):
        chromedriver = "chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(1)
        self.base_url = "https://scholarshipuniverse.arizona.edu/suha"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_suha(self):
        driver = self.driver
        driver.get(self.base_url + "/home/index")
        driver.find_element_by_css_selector("a.dropdown-toggle").click()
        driver.find_element_by_css_selector("ul.dropdown-menu > li > a").click()
        driver.find_element_by_id("team").click()
        driver.find_element_by_css_selector("img.img-responsive").click()
        driver.find_element_by_link_text("Next").click()
        try: self.assertEqual("Joined: 2009", driver.find_element_by_css_selector("div.h3.black > p.h3.black").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
def is_element_present(self, how, what):
    try:
        self.driver.find_element(by=how, value=what)
    except NoSuchElementException as e:
        return False
    return True


def is_alert_present(self):
    try:
        self.driver.switch_to_alert()
    except NoAlertPresentException as e:
        return False
    return True


def close_alert_and_get_its_text(self):
    try:
        alert = self.driver.switch_to_alert()
        alert_text = alert.text
        if self.accept_next_alert:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text
    finally:
        self.accept_next_alert = True


def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
