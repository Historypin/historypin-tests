from base import *
import os, sys

class Edit_Profile(HPTestCase):
	
	@logged_in
	@url('/en/person/65536')
	def test_edit_profile(self):
		
		self.e_wait('.icon-edit')
		
		self.e('.icon-edit').click()
		self.e_wait('#save-mah')
		
		self.assertEqual('kris.test00', self.e('.main-header-user a').text)
		self.assertEqual('http://{0}.historypin-hrd.appspot.com/en/people'.format(VERSION), self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		if not self.exists('[src="/resources/avatars/225x225/avatar_1.png"]'):
			self.e('.icon-trash').click()
			# logging.critical('test')
			sleep(1)
			self.accept_alert()
		
		self.e('#name').send_keys('edited')
		self.e('#description').send_keys('automation edit')
		self.e('#place').clear()
		self.e('#place').send_keys('santorini')
		sleep(1)
		
		self.e('#place').send_keys(Keys.ENTER)
		self.e('#birthyear').click()
		self.e('[label="2000"]').click()
		displayed(self, '#website')
		displayed(self, '#facebook')
		displayed(self, '#twitter')
		displayed(self, '#google-plus')
		displayed(self, '[for="facebook_switch"]')
		displayed(self, '[for="twitter_switch"]')
		displayed(self, '[for="google_switch"]')
		displayed(self, '[for="notification_switch"]')
		displayed(self, '[for="newsletter_switch"]')
		displayed(self, '[for="featured_user"]')
		displayed(self, '.edit-option-panel h5')
		displayed(self, '.footer-col a')
		displayed(self, '#intercom-launcher')
		instance(self, '[class="file-input"]')
		instance(self, '[label="1900"]')
		self.e('#save-mah').click()
		self.e_wait('.icon-edit')
		
		self.edit_profile_clear()
		
	@logged_in
	@url('/en/person/65536/edit')
	def edit_profile_clear(self):
		
		self.e_wait('#save-mah')
		
		self.assertEqual('kris.test00edited', self.e('.main-header-user a').text)
		self.e('[type="file"]').send_keys('/Users/kris/Downloads/wallpaper-power-symbol-green.png')
		self.e('#name').clear()
		self.e('#name').send_keys('kris.test00')
		self.e('#description').clear()
		self.e('#place').clear()
		self.e('#place').send_keys('sofia')
		sleep(1)
		
		self.e('#place').send_keys(Keys.ENTER)
		self.e('#birthyear').click()
		self.e('[label="1988"]').click()
		self.e('#save-mah').click()
		self.e_wait('.icon-edit')
		
		self.assertEqual('kris.test00', self.e('.main-header-user a').text)
		
		
		