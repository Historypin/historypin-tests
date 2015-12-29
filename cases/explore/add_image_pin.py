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
		displayed(self, '.add-img-pin-area .button')											# add file button
		self.e('[type="file"]').send_keys('/Users/kris/Downloads/images.png')					# upload image
		sleep(2)
		
		displayed(self, '.uploaded-img .white-bg')												# replace image button
		self.e('#title').send_keys('Selenium image pin')
		self.e('#description').send_keys('Selenium image pin')
		displayed(self, '#license')
		self.e('#date_taken').send_keys('1000-01-01')											# add date for pin
		self.e('.field-wrapper.required:nth-of-type(4) label').click()							# exact location radio button
		
		self.e('.location-search').send_keys('sofia')
		sleep(1)
		self.e('.location-search').send_keys(Keys.ENTER)
		sleep(1)
		
		displayed(self, '.hp-editor-map-cnt')													# location map
		self.e('.pin-location-map-section .icon-tick').click()									# street view checkbox
		sleep(1)
		
		displayed(self, '.ui-slider-handle')													# fade bar
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+=-?/;[]:,', 'Selenium image pin,')	# add tags
		displayed(self, '[name="new_project"]')													# create new collection
		# displayed(self, '#managed_filter')													# your collections and tours filter
		self.e('.checkbox-list .ng-binding').click()											# first of own collections
		self.e('#pinner h2:nth-of-type(4)').click()												# expand other info
		sleep(1)
		
		displayed(self, '#right_statement')
		displayed(self, '#creator')
		displayed(self, '#link_source')
		displayed(self, '#indentifier')
		displayed(self, '.button-center-wrapp .white-bg')										# cancel button
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


