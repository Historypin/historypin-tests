from base import *
import os, sys

class Edit_Project(HPTestCase):
	
	@logged_in
	@url('/en/premium-automated-collection/collection/edit')
	def test_edit_premium_collection(self):
		# sleep(4)
		# self.e_wait('.banner-cnt h3')
		
		# self.e('.hp-icon.icon-edit').click()
		# sleep(4)
		self.e_wait('.ui-autocomplete-input')
		self.assertEqual('Premium Automated Collection', self.e('.breadcrumbs-item a').text)
		
		self.e('.ss-delete').click()													#  delete manager
		self.e('.project-title').send_keys(' Changes')
		self.e('#short-description').send_keys(' Changes')
		self.e('#mce_0').send_keys(' Changes')											# long description
		self.e('#get-in-touch').send_keys(' Changes')
		self.e('#location-search').clear()
		self.e('#location-search').send_keys('Berlin')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.assertIsInstance(self.e('#map'), WebElement)								# left side map
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)					# location map
		
		# self.e('.landing-screen-type .button').click() 								# add landingscreen image
		
		self.e('.add-input').clear()													# delete video landing screen
		self.e('[for="explore-view-map"]').click()
		self.e('[name="add_pin_text"]').clear()
		self.e('[for="open-collection-pins"] .switch').click()							# close
		self.e('[for="open-collection"] .switch').click()								# close
		self.e('.select2-search-choice-close').click()									# delete tag
		self.e('[for="show-navigation-tags"] .switch').click()							# close tag
		self.e('#sort-select').click()													# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(3)').click()									# newest first gallery sorting
		self.assertTrue(self.e('.map-overlay-col .button').is_displayed())				# send a request button
		self.assertTrue(self.e('.map-overlay-preview').is_displayed())
		self.assertTrue(self.e('#blog-feed').is_displayed())
		self.assertTrue(self.e('.white-bg').is_displayed())								# cancel button
		self.e('#button_save').click()
		# sleep(6)
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated Collection')
		
	@logged_in
	@url('/en/premium-automated-collection')
	def test_edit_premium_collection_clear(self):
		# sleep(4)
		self.e_wait('.hp-icon.icon-edit')
		
		self.assertEqual('Premium Automated Collection Changes', self.e('.breadcrumbs-item a').text)
		self.e('.hp-icon.icon-edit').click()
		# sleep(4)
		self.e_wait('.ui-autocomplete-input')
		
		self.e('.ui-autocomplete-input').send_keys('KrisTestTwitter')					# add manager
		sleep(1)
		
		self.e('.ui-autocomplete li:nth-of-type(1)').click()							#  collection manager drop menu
		self.e('.project-title').clear()
		self.e('.project-title').send_keys('Premium Automated Collection')
		self.e('#short-description').clear()
		self.e('#short-description').send_keys('Premium Automated Collection')
		self.e('#mce_0').clear()
		self.e('#mce_0').send_keys('Premium Automated Collection')						# long description
		self.e('#get-in-touch').clear()
		self.e('#get-in-touch').send_keys('@automation awesome')
		self.e('#location-search').clear()
		self.e('#location-search').send_keys('Santorini')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.assertIsInstance(self.e('#map'), WebElement)								# left side map
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)					# location map
		
		# self.e('.landing-screen-type .button').click() # add landingscreen image
		
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')			# video landing screen
		self.e('[for="explore-view-hybrid"]').click()
		self.e('[for="open-collection-pins"] .switch').click()
		self.e('[for="open-collection"] .switch').click()
		self.e('[for="custom-add-pin"] .switch').click()
		self.e('[name="add_pin_text"]').send_keys('Selenium field')						# add custom name
		self.e('[for="show-navigation-tags"] .switch').click()
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+?><|}{:;~,')				# add tags
		self.e('#sort-select').click()													# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(1)').click()									# most popular gallery sorting
		self.assertTrue(self.e('.map-overlay-col .button').is_displayed())				# send a request button
		self.assertTrue(self.e('.map-overlay-preview').is_displayed())
		self.assertTrue(self.e('#blog-feed').is_displayed())
		self.assertTrue(self.e('.white-bg').is_displayed())								# cancel button
		self.e('#button_save').click()
		# sleep(6)
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated Collection')