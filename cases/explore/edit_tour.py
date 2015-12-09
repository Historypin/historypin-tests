from base import *
import os, sys

class Edit_Tour(HPTestCase):
	
	@logged_in
	@url('/en/premium-automated-tour/collection/edit')
	def test_edit_tour(self):
		
		self.e_wait('.project-title')
		
		self.assertEqual('Premium Automated Tour', self.e('.breadcrumbs-item a').text)
		self.e('.project-title').send_keys('Changes')
		self.e('#short-description').send_keys('Changes')
		self.e('#mce_0').send_keys('Changes')											# long description
		self.e('#location-search').clear()
		self.e('#location-search').send_keys('Dubai')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.assertIsInstance(self.e('#map'), WebElement)								# left side map
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)					# location map
		self.e('.add-input').clear()													# delete video landing screen
		self.e('[for="explore-view-gallery"]').click()
		self.e('.select2-search-choice-close').click()									# delete tag
		self.e('[for="show-navigation-tags"] .switch').click()							# close
		self.e('#sort-select').click()													# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(1)').click()									# most  popular gallery sorting
		self.assertTrue(self.e('.map-overlay-col .button').is_displayed())				# send a request button
		self.assertTrue(self.e('.map-overlay-preview').is_displayed())
		self.assertTrue(self.e('#blog-feed').is_displayed())
		self.assertTrue(self.e('.white-bg').is_displayed())								# cancel button
		self.e('#button_save').click()
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated TourChanges')
		
	@logged_in
	@url('/en/premium-automated-tour/collection/edit')
	def test_edit_tour_clear(self):

		self.e_wait('.project-title')
		
		self.assertEqual('Premium Automated TourChanges', self.e('.breadcrumbs-item a').text)
		self.e('.project-title').clear()
		self.e('.project-title').send_keys('Premium Automated Tour')
		self.e('#short-description').clear()
		self.e('#short-description').send_keys('Premium Automated Tour')
		self.e('#mce_0').clear()
		self.e('#mce_0').send_keys('Premium Automated Tour')							# long description
		self.e('#location-search').clear()
		self.e('#location-search').send_keys('Sydney')
		sleep(1)
		
		self.e('#location-search').send_keys(Keys.ENTER)
		
		self.assertIsInstance(self.e('#map'), WebElement)								# left side map
		self.assertIsInstance(self.e('.hp-editor-map-cnt'), WebElement)					# location map
		self.e('.add-input').send_keys('http://vjs.zencdn.net/v/oceans.mp4')			# video landing screen
		self.e('[for="explore-view-map"]').click()
		self.e('[for="show-navigation-tags"] .switch').click()							# open
		self.e('#s2id_autogen1').send_keys('3.14!@#$%^&*()_+?><|}{:;~,')				# add tags
		self.e('#sort-select').click()													# default gallery sorting
		sleep(1)
		
		self.e('#sort-select :nth-of-type(4)').click()									# oldest first gallery sorting
		self.assertTrue(self.e('.map-overlay-col .button').is_displayed())				# send a request button
		self.assertTrue(self.e('.map-overlay-preview').is_displayed())
		self.assertTrue(self.e('#blog-feed').is_displayed())
		self.assertTrue(self.e('.white-bg').is_displayed())								# cancel button
		self.e('#button_save').click()
		self.e_wait('.title')
		
		self.assertTitle('Historypin | Premium Automated Tour')
