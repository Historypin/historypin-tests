from base import *
import os, sys

class Add_Tour(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_add_premium_tour(self):
		# sleep(4)
		self.e_wait('.create-tour-card')
		
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		self.e('.create-tour-card').click()
		# sleep(4)
		self.e_wait('.project-title')
		
		self.e('.project-title').send_keys('Premium Automated Tour')
		self.e('#short-description').send_keys('Premium Automated Tour')
		self.e('#mce_0').send_keys('Premium Automated Tour')							# long description
		self.e('#location-search').send_keys('Sydney')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.assertIsInstance(self.e('#map'), WebElement)								# left side map
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)					# location map
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')			# video landing screen
		self.e('[for="explore-view-gallery"]').click()
		self.e('[for="show-navigation-tags"] .switch').click()
		self.e('#s2id_autogen1').send_keys('3.14!@#$%^&*()_+?><|}{:;~,' , 'automated,')	# add tags
		self.e('#sort-select').click()													# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(2)').click()									# recently added gallery sorting
		self.assertTrue(self.e('.map-overlay-col .button').is_displayed())				# send a request button
		self.assertTrue(self.e('.map-overlay-preview').is_displayed())
		self.assertTrue(self.e('#blog-feed').is_displayed())
		self.assertTrue(self.e('.white-bg').is_displayed())								# cancel button
		self.e('#button_save').click()
		# sleep(6)
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated Tour')
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_delete_tour(self):
		# sleep(4)
		self.e_wait('.tour-item .icon-trash')
		
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		self.assertEqual('Premium Automated Tour', self.e('.tour-item h3').text)
		self.e(".tour-item .icon-trash").click()										# delete project
		sleep(2)
		
		self.accept_alert()																# submit popup window