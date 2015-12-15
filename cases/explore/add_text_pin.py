from base import *
import os, sys

class Add_Text_Pin(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_text_pin(self):
		self.e_wait('#pins .icon-add-pin')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('#pins .icon-add-pin').click()
		self.e_wait('.hp-editor-map-cnt')
		
		self.e('.pin-type span:nth-of-type(3)').click()														# pin text button
		self.e('.cf .field-wrapper textarea').send_keys("Historypin is home to a growing community of local history lovers building up a global picture of how the world used to be using photos, old movies and sounds from the past.")
		self.e('#title').send_keys('Selenium text pin')
		self.e('#description').send_keys('Selenium text pin')
		self.assertTrue(self.e('#license').is_displayed())
		self.e('#date_taken').send_keys('2012-12-12')														# add date for pin
		self.e('.field-wrapper.required:nth-of-type(4) label').click()										# exact location radio button
		self.e('.location-search').send_keys('beijing')
		sleep(1)
		self.e('.location-search').send_keys(Keys.ENTER)
		
		self.assertTrue(self.e('.hp-editor-map-cnt').is_displayed())										# location map
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+=-?/;[]:,', 'Selenium pin,')					# add tags
		self.assertTrue(self.e('[name="new_project"]').is_displayed())										# create new collection
		# self.assertTrue(self.e('#managed_filter').is_displayed())											# your collections and tours filter
		sleep(1)
		
		self.e('.checkbox-list .ng-binding').click()														# first of own collections
		self.e('#pinner h2:nth-of-type(4)').click()															# expand other info
		sleep(1)
		
		self.assertTrue(self.e('#right_statement').is_displayed())
		self.assertTrue(self.e('#creator').is_displayed())
		self.assertTrue(self.e('#link_source').is_displayed())
		self.assertTrue(self.e('#indentifier').is_displayed())
		self.assertTrue(self.e('.button-center-wrapp .white-bg').is_displayed())							# cancel button
		self.e('.button-center-wrapp a:last-child').click()													# save button
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium text pin')
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_delete_text_pin(self):
		self.e_wait('.pin-item .icon-trash')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.assertEqual('Selenium text pin', self.e('.pin-item h3').text)
		self.e('.pin-item .icon-trash').click()																# delete pin
		sleep(2)
		
		self.accept_alert()																					# submit popup window
		sleep(2)
		
		self.go('/en/person/{0}/'.format(ID_USER))
		sleep(2)
		
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)
