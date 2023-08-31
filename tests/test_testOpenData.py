# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestOpenData():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_testOpenData(self):
    self.driver.get("https://www.flashscore.pl/?gclid=EAIaIQobChMIqp26naWGgQMVRYZoCR1-yw3REAAYASAAEgIId_D_BwE")
    self.driver.set_window_size(550, 691)
    element = self.driver.find_element(By.CSS_SELECTOR, ".header__item:nth-child(2)")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".menuTop__myfs")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.ID, "onetrust-reject-all-handler").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, "#g_1_zowUjY1D > .event__participant--away").click()
    self.vars["win5251"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win5251"])
    element = self.driver.find_element(By.CSS_SELECTOR, ".header__logo")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(3) .tab__text").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.CSS_SELECTOR, ".h2h__section:nth-child(2) .h2h__row:nth-child(1) > .h2h__awayParticipant").click()
    self.vars["win1359"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win1359"])
    self.driver.close()
  
