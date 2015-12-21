from base import *
import os, sys

class Add_Image_Pin(HPTestCase):
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_image_pin(self):
		self.e_wait('#pins .icon-add-pin')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('#pins .icon-add-pin').click()
		self.e_wait('.hp-editor-map-cnt')
		
		self.exists('[name="pin-media"]')														# pin video
		self.exists('[name="pin-text"]')														# pin text
		self.assertTrue(self.e('.add-img-pin-area .button').is_displayed())						# add file button
		self.e('[type="file"]').send_keys('/Users/kris/Downloads/images.png')					# upload image
		sleep(2)
		
		self.assertTrue(self.e('.uploaded-img .white-bg').is_displayed())						# replace image button
		self.e('#title').send_keys('Selenium image pin')
		self.e('#description').send_keys('Selenium image pin')
		self.assertTrue(self.e('#license').is_displayed())
		self.e('#date_taken').send_keys('1000-01-01')											# add date for pin
		self.e('.field-wrapper.required:nth-of-type(4) label').click()							# exact location radio button
		
		self.e('.location-search').send_keys('sofia')
		sleep(1)
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		self.assertTrue(self.e('.hp-editor-map-cnt').is_displayed())							# location map
		self.e('.pin-location-map-section .icon-tick').click()									# street view checkbox
		sleep(1)
		
		self.assertTrue(self.e('.ui-slider-handle').is_displayed())								# fade bar
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+=-?/;[]:,', 'Selenium image pin,')	# add tags
		self.assertTrue(self.e('[name="new_project"]').is_displayed())							# create new collection
		# self.assertTrue(self.e('#managed_filter').is_displayed())								# your collections and tours filter
		self.e('.checkbox-list .ng-binding').click()											# first of own collections
		self.e('#pinner h2:nth-of-type(4)').click()												# expand other info
		sleep(1)
		
		self.assertTrue(self.e('#right_statement').is_displayed())
		self.assertTrue(self.e('#creator').is_displayed())
		self.assertTrue(self.e('#link_source').is_displayed())
		self.assertTrue(self.e('#indentifier').is_displayed())
		self.assertTrue(self.e('.button-center-wrapp .white-bg').is_displayed())				# cancel button
		self.e('.button-center-wrapp a:last-child').click()										# save button
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium image pin')
		
		self.delete_image_pin()
	
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def delete_image_pin(self):
		self.e_wait('.pin-item .icon-trash')
		
		self.assertEqual('now', self.e('.activity li:first-of-type .time').text)
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.assertEqual('Selenium image pin', self.e('.pin-item h3').text)
		self.e('.pin-item .icon-trash').click()													# delete pin
		sleep(3)
		
		self.accept_alert()																		# submit popup window
		self.e_wait('.pin-item .icon-trash')
		
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)


