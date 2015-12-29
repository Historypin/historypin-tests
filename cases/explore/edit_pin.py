from base import *
import os, sys

class Edit_Pin(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_edit_pin(self):
		
		self.e_wait('.pin-item h3')
		
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('.pin-item .icon-pen').click()
		self.e_wait('#title')
		
		self.e('#title').send_keys(' Changes')
		self.e('#description').send_keys('Changes ')
		displayed(self, '#license')
		self.e('#date_taken').clear()
		self.e('#date_taken').send_keys('1000-2015')										# change date
		self.e('.location-search').clear()
		self.e('.location-search').send_keys('Tokyo')										# change location
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		displayed(self, '.hp-editor-map-cnt')												# location map
		displayed(self, '.ui-slider-handle')												# fade bar
		self.e('.select2-search-choice-close').click()										# delete tag
		displayed(self, '[name="new_project"]')												# create new collection
		displayed(self, '.checkbox-list')													# own collections
		self.e('#pinner h2:nth-of-type(4)').click()											# expand other info
		sleep(1)
		
		displayed(self, '#right_statement')
		displayed(self, '#creator')
		displayed(self, '#link_source')
		displayed(self, '#indentifier')
		displayed(self, '.button-center-wrapp .white-bg')									# cancel button
		self.e('.button-center-wrapp a:last-child').click()									# save button
		# sleep(8)
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium pin Changes')
		
		self.edit_pin_clear()
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def edit_pin_clear(self):
		
		self.e_wait('.pin-item .icon-pen')
		
		self.assertEqual('Selenium pin Changes', self.e('.pin-item h3').text)
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('.pin-item .icon-pen').click()
		self.e_wait('#title')
		
		self.e('#title').clear()
		self.e('#title').send_keys('Selenium pin')
		self.e('#description').clear()
		self.e('#description').send_keys('Selenium pin')
		self.e('#date_taken').clear()
		self.e('#date_taken').send_keys('2012-12-12')										# add date for pin
		self.e('.location-search').clear()
		self.e('.location-search').send_keys('rio de janeiro')								# change location
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		self.e('.select2-input').send_keys('selenium pin,', '3.14!@#$%^&*()_+=-?/;[]:,')	# add tags
		self.e('#pinner h2:nth-of-type(4)').click()											# expand other info
		sleep(1)
		
		self.e('.button-center-wrapp a:last-child').click()									# save button
		# sleep(8)
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium pin')
		
		
		