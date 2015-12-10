from base import *
import os, sys

class Edit_Pin(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_edit_pin(self):
		
		self.e_wait('.pin-item .icon-pen')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('.pin-item .icon-pen').click()
		self.e_wait('#title')
		
		self.e('#title').send_keys(' Changes')
		self.e('#description').send_keys(' Changes ')
		self.assertTrue(self.e('#license').is_displayed())
		self.e('#date_taken').clear()
		self.e('#date_taken').send_keys('1000-2015')										# change date
		self.e('.location-search').clear()
		self.e('.location-search').send_keys('Tokyo')										# change location
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		self.assertTrue(self.e('.hp-editor-map-cnt').is_displayed())						# location map
		self.assertTrue(self.e('.ui-slider-handle').is_displayed())							# fade bar
		self.e('.select2-search-choice-close').click()										# delete tag
		self.assertTrue(self.e('[name="new_project"]').is_displayed())						# create new collection
		self.assertTrue(self.e('.checkbox-list').is_displayed())							# own collections
		self.e('#pinner h2:nth-of-type(4)').click()											# expand other info
		sleep(1)
		
		self.assertTrue(self.e('#right_statement').is_displayed())
		self.assertTrue(self.e('#creator').is_displayed())
		self.assertTrue(self.e('#link_source').is_displayed())
		self.assertTrue(self.e('#indentifier').is_displayed())
		self.assertTrue(self.e('.button-center-wrapp .white-bg').is_displayed())			# cancel button
		self.e('.button-center-wrapp a:last-child').click()									# save button
		# sleep(8)
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium pin Changes')
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_edit_pin_clear(self):
		
		self.e_wait('.pin-item .icon-pen')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('.pin-item .icon-pen').click()
		self.e_wait('#title')
		
		self.e('#title').clear()
		self.e('#title').send_keys('Selenium pin')
		self.e('#description').clear()
		self.e('#description').send_keys('Selenium pin')
		self.assertTrue(self.e('#license').is_displayed())
		self.e('#date_taken').clear()
		self.e('#date_taken').send_keys('2012-12-12')										# add date for pin
		self.e('.location-search').clear()
		self.e('.location-search').send_keys('rio de janeiro')								# change location
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		self.assertTrue(self.e('.hp-editor-map-cnt').is_displayed())						# location map
		self.assertTrue(self.e('.ui-slider-handle').is_displayed())							# fade bar
		self.e('.select2-input').send_keys('selenium pin,', '3.14!@#$%^&*()_+=-?/;[]:,')	# add tags
		self.assertTrue(self.e('[name="new_project"]').is_displayed())						# create new collection
		self.assertTrue(self.e('.checkbox-list').is_displayed())							# own collections
		self.e('#pinner h2:nth-of-type(4)').click()											# expand other info
		sleep(1)
		
		self.assertTrue(self.e('#right_statement').is_displayed())
		self.assertTrue(self.e('#creator').is_displayed())
		self.assertTrue(self.e('#link_source').is_displayed())
		self.assertTrue(self.e('#indentifier').is_displayed())
		self.assertTrue(self.e('.button-center-wrapp .white-bg').is_displayed())			# cancel button
		self.e('.button-center-wrapp a:last-child').click()									# save button
		# sleep(8)
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium pin')
		