from base import *
import os, sys

class Add_Projects(HPTestCase):
	
	@logged_in
	@url('/en/Premium Automated Collection')
	def test_edit_premium_collection(self):
		# sleep(4)
		self.e_wait('.icon-edit')
		
		self.assertEqual('Premium Automated Collection', self.e('.simple-banner h2').text)
		self.e('.icon-edit').click()
		# sleep(4)
		self.e_wait('.ui-autocomplete-input')
		
		self.e('.ss-delete').click()													#  delete manager
		self.e('.project-title').send_keys('Premium Automated Collection Edited')
		self.e('#short-description').send_keys('Premium Automated Collection Edited')
		self.e('#mce_0').send_keys('Premium Automated Collection Edited')						# long description
		self.e('#get-in-touch').send_keys('@automation awesome edited')
		self.e('#location-search').send_keys('Miami')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.assertIsInstance(self.e('#map'), WebElement)								# left side map
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)					# location map
		
		# self.e('.landing-screen-type .button').click() # add landingscreen image
		
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')			# video landing screen
		self.e('[for="explore-view-gallery"]').click()
		self.e('[for="open-collection"] .switch').click()
		self.e('[for="custom-add-pin"] .switch').click()
		self.e('[name="add_pin_text"]').send_keys('Selenium field')						# add custom name
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
		
		self.assertTitle('Historypin | Premium Automated Collection')