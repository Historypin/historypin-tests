from base import *
import os, sys

class Add_Pin(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_pin(self):
		# sleep(2)
		self.e_wait('#pins .icon-add-pin')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('#pins .icon-add-pin').click()
		# sleep(3)
		self.e_wait('.hp-editor-map-cnt')
		
		self.assertIsInstance(self.e('[name="pin-media"]'), WebElement)						# pin video
		self.assertIsInstance(self.e('[name="pin-text"]'), WebElement)						# pin text
		self.assertTrue(self.e('.add-img-pin-area .button').is_displayed())					# add file button
		self.e('.add-input-wrapper .add-input').send_keys('http://pre15.deviantart.net/5108/th/pre/i/2010/332/f/b/power_symbol_wallpapers_by_dodgydavec-d33slvo.png')	# add link to an image
		self.e('.add-input-wrapper .add-button').click()									# add link image button
		self.assertTrue(self.e('.uploaded-img .white-bg').is_displayed)						# replace image button
		self.e('#title').send_keys('Selenium pin')
		self.e('#description').send_keys('Selenium pin')
		self.e('.select2-input').send_keys('Selenium pin,', '3.14!@#$%^&*()_+=-?/;[]:,')	# add tags
		self.e('#date_taken').send_keys('2012-12-12')										# add date for pin
		self.e('.cf p:nth-of-type(4)').click()												# exact location radio button
		self.e('.location-search').send_keys('santorini')
		sleep(1)
		
		self.e('.location-search').send_keys(Keys.ENTER)
		self.assertTrue(self.e('.hp-editor-map-cnt').is_displayed())						# location map
		self.e('.pin-location-map-section p:nth-of-type(1)').click()						# street view checkbox
		sleep(1)
		
		self.assertTrue(self.e('.ui-slider-handle').is_displayed())							# fade bar
		self.assertTrue(self.e('.add-pin-to .checkbox-tick').is_displayed())				# create new collection checkbox
		# self.assertTrue(self.e('#managed_filter').is_displayed())							# your collections and tours filter
		self.e('.checkbox-list .ng-binding').click()										# first of own collections
		self.assertTrue(self.e('#license').is_displayed())
		self.assertTrue(self.e('#right_statement').is_displayed())
		self.assertTrue(self.e('#creator').is_displayed())
		self.assertTrue(self.e('#link_source').is_displayed())
		self.assertTrue(self.e('#indentifier').is_displayed())
		self.assertTrue(self.e('.button-center-wrapp .white-bg').is_displayed())			# cancel button
		self.e('.button-center-wrapp a:last-child').click()									# save button
		# sleep(8)
		self.e_wait('.pin-content h1')
		
		self.assertEqual('Selenium pin', self.e('.pin-content h1').text)
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_delete_pin(self):
		# sleep(2)
		self.e_wait('.pin-item .icon-trash')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)
		self.e('.pin-item .icon-trash').click()												# delete pin
		sleep(2)
		
		self.accept_alert()																	# submit popup window