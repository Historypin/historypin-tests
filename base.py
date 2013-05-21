import unittest, functools

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


from conf import *

WebElement.e = WebElement.find_element_by_css_selector
WebElement.es = WebElement.find_elements_by_css_selector
WebElement.css = WebElement.value_of_css_property

def url(url):
	def wrapper(fn):
		def wrapped(*args, **kwargs):
			args[0].go(url)
			fn(*args, **kwargs)
		return wrapped
	return wrapper


class Browser(webdriver.Chrome):
# class Browser(webdriver.Firefox):
	def go(self, url):
		self.get(URL_BASE + url)
	
	def es(self, selector):
		return self.find_elements_by_css_selector(selector)
		
	def e(self, selector):
		return self.find_element_by_css_selector(selector)
	
	def e_wait(self, selector, timeout = 30):
		try:
			w = WebDriverWait(self, timeout)
			return w.until(lambda driver: driver.e(selector))
		except:
			raise NoSuchElementException('The element could not be found')
	
	def hover(self, elem):
		webdriver.common.action_chains.ActionChains(self).move_to_element(elem).perform()
		sleep(.5)
	
	def double_click(self, elem):
		webdriver.common.action_chains.ActionChains(self).double_click(elem).perform()
		sleep(.5)



class TestCase(unittest.TestCase):
	browser = Browser(PATH_CRHOME_DRIVER) # chrome
	# browser = Browser() # FF
	browser.maximize_window()
	
	# @classmethod
	# def setUpClass(cls, browser):
	# 	cls.browser = Browser(PATH_CRHOME_DRIVER)
	# 	cls.browser.maximize_window()
	
	go				= browser.go
	refresh			= browser.refresh
	es				= browser.es
	e				= browser.e
	e_wait			= browser.e_wait
	hover			= browser.hover
	double_click	= browser.double_click
	
	@classmethod
	def browser_close(cls):
		cls.browser.close()
	
	def assertTitle(self, title):
		self.assertIn(title, self.browser.title)


def run(*tests):
	import cases
	
	suite = unittest.TestSuite()
	
	if tests:
		for i in tests:
			i = i.split('.')
			
			test_case = getattr(cases, i[0])
			if len(i) > 1:
				suite.addTest(test_case(i[1]))
			else:
				suite.addTests(unittest.TestLoader().loadTestsFromTestCase(test_case))
	else:
		suite.addTests(unittest.TestLoader().loadTestsFromModule(cases))
	
	unittest.TextTestRunner(verbosity = 1).run(suite)
	
	
	TestCase.browser_close()


class HPTestCase(TestCase):
	def login(self):
		pass
	
	def logout(self):
		pass


