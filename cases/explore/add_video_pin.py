from base import *
import os, sys

class Add_Video_Pin(HPTestCase):
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_video_pin(self):
		self.e_wait('#pins .icon-add-pin')
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('#pins .icon-add-pin').click()
		self.e_wait('.hp-editor-map-cnt')
		
		self.e('.pin-type span:nth-of-type(2)').click()														# video pin button
		sleep(1)
		
		self.e('.video-or-sound-pin .add-input').send_keys('https://www.youtube.com/watch?v=FdT3eKdto4w')
		self.e('.video-or-sound-pin .add-button').click()
		displayed(self, '.uploaded-video-or-sound-pin .white-bg')											# replace video button
		self.e('#title').send_keys('Selenium video pin')
		self.e('#description').send_keys('Selenium video pin')
		self.e('#date_taken').send_keys('2012-12-12')														# add date for pin
		self.e('.field-wrapper.required:nth-of-type(4) label').click()										# exact location radio button
		self.e('.location-search').send_keys('moscow')
		sleep(1)
		
		self.e('.location-search').send_keys(Keys.ENTER)
		displayed(self, '.hp-editor-map-cnt')																# location map
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+=-?/;[]:,', 'Selenium pin,')					# add tags
		self.e('.checkbox-list .ng-binding').click()														# first of own collections
		self.e('#pinner h2:nth-of-type(4)').click()															# expand other info
		sleep(1)
		
		self.e('.button-center-wrapp a:last-child').click()													# save button
		self.e_wait('.streetview-img-wrapper')
		
		self.assertTitle('Historypin | kris.test00 | Selenium video pin')
		
		self.delete_video_pin()
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def delete_video_pin(self):
		self.e_wait('.pin-item .icon-trash')
		sleep(1)
		
		self.assertEqual('now', self.e('.activity li:first-of-type .time').text)
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.assertEqual('Selenium video pin', self.e('.pin-item h3').text)
		self.e('.pin-item .icon-trash').click()																# delete pin
		sleep(2)
		
		self.accept_alert()																					# submit popup window
		sleep(2)
		
		self.go('/en/person/{0}/'.format(ID_USER))
		sleep(3)
		
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)


