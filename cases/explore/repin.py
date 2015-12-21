from base import *
import os, sys

class Repin(HPTestCase):
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/en/place/united-states/california/list/pins')
	def test_repin(self):
		self.e_wait('.pin-item')
		
		self.assertEqual('California', self.e('.breadcrumbs-item:nth-of-type(3) a').text)
		self.e('.pin-item').click()															# open first new pin
		self.e_wait('.photo')
		
		self.e('.site-toolbar .icon-repin').click()
		sleep(2)
		
		self.e('.listing-checkbox-styling').click()											# first of own projects
		self.e('.site-toolbar .icon-repin').click()
		sleep(2)
		
		self.unpin()
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def unpin(self):
		self.e_wait('.activity li:first-of-type .time')
		
		self.assertEqual('now', self.e('.activity li:first-of-type .time').text)
		self.e('.type-of-activity a:nth-of-type(2)').click() 								# open last active pin
		self.e_wait('.photo')
		
		self.e('.site-toolbar .icon-repin').click()
		sleep(2)
		
		self.e('.listing-checkbox-styling').click()											# first of own projects unpin
		self.e('.site-toolbar .icon-repin').click()
		sleep(2)
		
		self.go('/en/person/{0}/'.format(ID_USER))
		self.e_wait('.activity li:first-of-type .time')
		
		activity_check = (self.e('.activity li:first-of-type .time').text) 					# last activity time
		self.assertFalse('now' == activity_check)