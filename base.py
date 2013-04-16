from conf import *

import unittest

from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException

# from selenium.webdriver.common.keys import Keys


class Browser(webdriver.Chrome):
	def _e(self, selector):
		return self.find_elements_by_css_selector(selector)
	
	def _t(self, selector):
		return self._e(selector)[0].text
	
	def _a(self, selector, attr):
		return self._e(selector)[0].get_attribute(attr)

class TestCase(unittest.TestCase):
	browser = Browser(PATH_CRHOME_DRIVER)
	browser.maximize_window()
	_e, _t, _a = [getattr(browser, '_' + i) for i in ['e', 't', 'a']]
	
	
	@classmethod
	def browser_close(cls):
		cls.browser.close()
	
	def assert_title(self, title):
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
	
	unittest.TextTestRunner().run(suite)
	
	
	TestCase.browser_close()


class HPTestCase(TestCase):
	def login(self):
		pass
	
	def logout(self):
		pass


