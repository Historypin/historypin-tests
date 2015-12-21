from base import *
import os, sys

class Edit_Project(HPTestCase):
	
	@logged_in
	@url('/en/premium-automated-collection/collection/edit')
	def test_edit_premium_collection(self):
		self.e_wait('.ui-autocomplete-input')
		self.assertEqual('Premium Automated Collection', self.e('.breadcrumbs-item a').text)
		
		self.e('.ss-delete').click()														# delete manager
		self.e('.project-title').send_keys(' Changes')
		self.e('#short-description').send_keys('Changes')
		self.e('#mce_0').send_keys('Changes')												# long description
		self.e('#get-in-touch').send_keys('Changes')
		self.e('#location-search').clear()
		self.e('#location-search').send_keys('Berlin')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.exists('#map')																	# left side map
		self.exists('.hp-editor-map-cnt')													# location map
		self.e('.add-input').clear()														# delete video landing screen
		self.e('[type="file"]').send_keys('/Users/kris/Downloads/landingscreen.jpg')		# upload image
		sleep(1)
		
		self.assertTrue(self.e('.icon-trash').is_displayed()) 								# delete landing screen button
		self.assertTrue(self.e('.landing-screen-type .input-file-wrapp').is_displayed()) 	# change landing screen image button
		self.e('[for="explore-view-map"]').click()
		self.e('[name="add_pin_text"]').clear()
		self.e('[for="open-collection-pins"] .switch').click()								# close
		self.e('[for="open-collection"] .switch').click()									# close
		self.e('.select2-search-choice-close').click()										# delete tag
		self.e('[for="show-navigation-tags"] .switch').click()								# close tag
		self.e('#sort-select').click()														# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(3)').click()										# newest first gallery sorting
		self.assertTrue(self.e('.map-overlay-col .button').is_displayed())					# send a request button
		self.assertTrue(self.e('.map-overlay-preview').is_displayed())
		self.assertTrue(self.e('#blog-feed').is_displayed())
		self.assertTrue(self.e('.white-bg').is_displayed())									# cancel button
		self.e('#button_save').click()
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated Collection')
		
		self.edit_premium_collection_clear()
		
	@logged_in
	@url('/en/premium-automated-collection')
	def edit_premium_collection_clear(self):
		self.e_wait('.site-toolbar .icon-edit')
		
		self.e('.icon-arrow-down').click()
		sleep(1)
		
		self.assertEqual('Premium Automated Collection Changes', self.e('.breadcrumbs-item a').text)
		self.e('.site-toolbar .icon-edit').click()
		self.e_wait('.ui-autocomplete-input')
		
		self.e('.ui-autocomplete-input').send_keys('KrisTestTwitter')						# add manager
		sleep(2)
		
		self.e('.ui-autocomplete li:nth-of-type(1)').click()								# collection manager drop menu
		self.e('.project-title').clear()
		self.e('.project-title').send_keys('Premium Automated Collection')
		self.e('#short-description').clear()
		self.e('#short-description').send_keys('Premium Automated Collection')
		self.e('#mce_0').clear()
		self.e('#mce_0').send_keys('Premium Automated Collection')							# long description
		self.e('#get-in-touch').clear()
		self.e('#get-in-touch').send_keys('@automation awesome')
		self.e('.landing-screen-type .icon-trash').click()									# delete image landing screen
		self.e('#location-search').clear()
		self.e('#location-search').send_keys('Santorini')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)						# location map
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')				# add video landing screen
		self.e('[for="explore-view-hybrid"]').click()
		self.e('[for="open-collection-pins"] .switch').click()								# open
		self.e('[for="open-collection"] .switch').click()									# open
		self.e('[for="custom-add-pin"] .switch').click()
		self.e('[name="add_pin_text"]').send_keys('Selenium field')							# add custom name
		self.e('[for="show-navigation-tags"] .switch').click()
		self.e('.select2-input').send_keys('3.14!@#$%^&*()_+?><|}{:;~,')					# add tags
		self.e('#sort-select').click()														# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(1)').click()										# most popular gallery sorting
		self.e('#button_save').click()
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated Collection')
		
		
		