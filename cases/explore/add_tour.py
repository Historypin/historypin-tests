from base import *
import os, sys

class Add_Tour(HPTestCase):
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_premium_tour(self):
		self.e_wait('.create-tour-card')
		
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		self.e('.create-tour-card').click()
		self.e_wait('.project-title')
		
		self.e('.project-title').send_keys('Automated Tour')
		self.e('#short-description').send_keys('Automated Tour')
		self.e('#mce_0').send_keys('Automated Tour')									# long description
		self.e('#location-search').send_keys('Sydney')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.exists('#map')																# left side map
		self.exists('.hp-editor-map-cnt')												# location map
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')			# video landing screen
		self.e('[for="explore-view-gallery"]').click()
		self.e('[for="show-navigation-tags"] .switch').click()
		self.e('#s2id_autogen1').send_keys('3.14!@#$%^&*()_+?><|}{:;~,' , 'automated,')	# add tags
		self.e('#sort-select').click()													# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(2)').click()									# recently added gallery sorting
		displayed(self, '.map-overlay-col .button')										# send a request button
		displayed(self, '.map-overlay-preview')
		displayed(self, '#blog-feed')
		displayed(self, '.white-bg')													# cancel button
		self.e('#button_save').click()
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Automated Tour')
		
		self.delete_tour()
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def delete_tour(self):
		self.e_wait('.tour-item .icon-trash')
		
		self.assertEqual('now', self.e('.activity li:first-of-type .time').text)
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		self.assertEqual('Automated Tour', self.e('.tour-item h3').text)
		self.e(".tour-item .icon-trash").click()										# delete project
		sleep(2)
		
		self.accept_alert()																# submit popup window
		
		self.go('/en/person/{0}/'.format(ID_USER))
		self.e_wait('.tour-item .icon-trash')
		
		self.assertEqual('Premium Automated Tour', self.e('.tour-item h3').text)
		
		
		