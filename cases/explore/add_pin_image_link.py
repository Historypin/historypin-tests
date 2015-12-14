from base import *
import os, sys

class Add_Pin_Image_Link(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_pin_image_link(self):
		self.e_wait('#pins .icon-add-pin')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('#pins .icon-add-pin').click()
		self.e_wait('.hp-editor-map-cnt')
		
		self.assertIsInstance(self.e('[name="pin-media"]'), WebElement)						# pin video
		self.assertIsInstance(self.e('[name="pin-text"]'), WebElement)						# pin text
		self.assertTrue(self.e('.add-img-pin-area .button').is_displayed())					# add file button
		self.e('.add-input-wrapper .add-input').send_keys('http://pre15.deviantart.net/5108/th/pre/i/2010/332/f/b/power_symbol_wallpapers_by_dodgydavec-d33slvo.png')	# add link to an image
		self.e('.add-input-wrapper .add-button').click()									# add link image button
		self.assertTrue(self.e('.uploaded-img .white-bg').is_displayed())					# replace image button
		self.e('#title').send_keys('Selenium image with link pin')
		self.e('#description').send_keys('Selenium image with link pin')
		self.assertTrue(self.e('#license').is_displayed())
		self.e('#date_taken').send_keys('2012-12-12')										# add date for pin
		self.e('.field-wrapper.required:nth-of-type(4) label').click()						# exact location radio button
		self.e('.location-search').send_keys('santorini')
		sleep(1)
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		self.assertTrue(self.e('.hp-editor-map-cnt').is_displayed())						# location map
		self.e('.pin-location-map-section .icon-tick').click()								# street view checkbox
		sleep(1)
		
		self.assertTrue(self.e('.ui-slider-handle').is_displayed())							# fade bar
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+=-?/;[]:,', 'Selenium image with link pin,')	# add tags
		self.assertTrue(self.e('[name="new_project"]').is_displayed())						# create new collection
		# self.assertTrue(self.e('#managed_filter').is_displayed())							# your collections and tours filter
		self.e('.checkbox-list .ng-binding').click()										# first of own collections
		self.e('#pinner h2:nth-of-type(4)').click()											# expand other info
		sleep(1)
		
		self.assertTrue(self.e('#right_statement').is_displayed())
		self.assertTrue(self.e('#creator').is_displayed())
		self.assertTrue(self.e('#link_source').is_displayed())
		self.assertTrue(self.e('#indentifier').is_displayed())
		self.assertTrue(self.e('.button-center-wrapp .white-bg').is_displayed())			# cancel button
		self.e('.button-center-wrapp a:last-child').click()									# save button
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium image with link pin')
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_delete_pin_image_link(self):
		self.e_wait('.pin-item .icon-trash')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.assertEqual('Selenium image with link pin', self.e('.pin-item h3').text)
		self.e('.pin-item .icon-trash').click()												# delete pin
		sleep(2)
		
		self.accept_alert()																	# submit popup window
		self.e_wait('.pin-item h3')
		
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)
		