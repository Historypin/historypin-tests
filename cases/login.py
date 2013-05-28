# -*- coding: utf-8 -*-

from base import *

class Login(HPTestCase):
	
	@url('/user/')
	def test_join(self):
		
		self.assertEqual('Historypin uses Google Accounts to keep your login details safe and secure.', self.e('.centered p').text)
		
		col_left = self.e('.col.w2:nth-of-type(1)')
		self.assertEqual('I already have a Google Account'	, col_left.e('h4').text)
		self.assertIsInstance(col_left.e('a')				, WebElement)
		self.assertEqual('Login'							, col_left.e('a').text)
		
		col_right = self.e('.col.w2:nth-of-type(2)')
		self.assertEqual("I don't have a Google Account"				, col_right.e('h4').text)
		self.assertEqual('https://www.google.com/accounts/NewAccount'	, col_right.e('a').get_attribute('href'))
		self.assertEqual('Register now'									, col_right.e('a').text)
	
	@url('/user/')
	def test_login_logout(self):
		
		login = self.e('.col.w2:nth-of-type(1) .next-button')
		login.click()
		
		self.assertIn('https://accounts', 'https://accounts.google.com/ServiceLogin?service=ah&passive=true&continue=https://appengine.google.com/')
		self.e('.email-div input').send_keys('gabriela.ananieva@wearewhatwedo.org')
		self.e('#Passwd').send_keys('tristania1010')
		self.e('#signIn').click()
		
		self.assertIn('11675544', URL_BASE + '/channels/view/11675544/#|photos/list/cache/0/')
		
		logout = self.e('.nav li a[class=logout]')
		logout.click()
		
		self.assertEqual('Login'				, self.e('.nav li a[href^=https]').text)
		self.assertIn('https://www.google.com/'	, self.e('.nav li a[href^=https]').get_attribute('href'))
		



