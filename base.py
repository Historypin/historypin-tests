import unittest

from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


from conf import *

WebElement.e	= WebElement.find_element_by_css_selector
WebElement.es	= WebElement.find_elements_by_css_selector
WebElement.css	= WebElement.value_of_css_property
WebElement.parent_node = lambda self: self.find_element_by_xpath('./parent::node()')

def url(url):
	def wrapper(fn):
		def wrapped(*args, **kwargs):
			args[0].go(url)
			fn(*args, **kwargs)
		return wrapped
	return wrapper


def logged_in(fn):
	def wrapped(*args, **kwargs):
		args[0].login_cookie_set()
		fn(*args, **kwargs)
		args[0].login_cookie_del()
	return wrapped


# class Browser(webdriver.Firefox):
class Browser(webdriver.Chrome):
	def go(self, url):
		self.get('' if url.startswith('http') else URL_BASE + url)
		# self.pageload_wait()
	
	# TODO get rid of this it is exactly the same
	def goBack(self, url):
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
	
	# def pageload_wait(self, timeout = 30):
	# 	try:
	# 		w = WebDriverWait(self, timeout)
	# 		return w.until(lambda driver: driver.execute_script("return document.readyState;") == "complete")
	# 	except:
	# 		raise Exception('Page could not load')  # NoSuchElementException('The element could not be found')
	
	def hover(self, elem):
		webdriver.common.action_chains.ActionChains(self).move_to_element(elem).perform()
		sleep(.5)
	
	def double_click(self, elem):
		webdriver.common.action_chains.ActionChains(self).double_click(elem).perform()
		sleep(.5)  # TODO is this necessary



class TestCase(unittest.TestCase):
	@classmethod
	def browser_start(cls, browser):
		cls.browser = browser
		cls.browser.maximize_window()
		
		cls.go				= cls.browser.go
		cls.goBack			= cls.browser.goBack  # TODO remove this
		cls.refresh			= cls.browser.refresh
		cls.es				= cls.browser.es
		cls.e				= cls.browser.e
		cls.e_wait			= cls.browser.e_wait
		# cls.pageload_wait	= cls.browser.pageload_wait
		cls.hover			= cls.browser.hover
		cls.double_click	= cls.browser.double_click
	
	@classmethod
	def browser_close(cls):
		cls.browser.close()
	
	def assertTitle(self, title):
		self.assertIn(title, self.browser.title)


LOGIN_COOKIES = []

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
	
	TestCase.browser_start(Browser(PATH_CRHOME_DRIVER))
	HPTestCase.login()
	
	unittest.TextTestRunner(verbosity = 1).run(suite)
	TestCase.browser_close()


class HPTestCase(TestCase):
	@classmethod
	def login(cls):
		cls.go('/user/')
		
		login = cls.e('#site-content .login .buttons li:nth-of-type(1) a')
		login.click()
		sleep(3)
		
		cls.e('#Email').send_keys('gabriela.ananieva@wearewhatwedo.org')
		cls.e('#Passwd').send_keys('tristania1010')
		cls.e('#signIn').click()
		sleep(3)
		
		try:
			cls.e('#submit_approve_access').click()
			sleep(3)
		except:
			pass
		
		LOGIN_COOKIES.append(cls.browser.get_cookie('hpsid'))
		
		cls.login_cookie_del()
		
		cls.browser.execute_script('window.stop();')
		sleep(1)
	
	@classmethod
	def login_cookie_set(cls):
		for i in LOGIN_COOKIES:
			if i: cls.browser.add_cookie(i)
	
	@classmethod
	def login_cookie_del(cls):
		for i in LOGIN_COOKIES:
			if i: cls.browser.delete_cookie(i['name'])
	
	# def logout(self):
	# 	self.go(URL_BASE + '/user/logout/')
	# 	self.pageload_wait()


