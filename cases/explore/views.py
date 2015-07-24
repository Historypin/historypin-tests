# -*- coding: utf-8 -*-

from base import *
import os, sys

class Pages_View(HPTestCase):
	
	# TODO put in order test later to be in seperate files
	# TODO These later could be extended to fully check the content and/or functionality.
	
	@url('{0}/en/'.format(URL_BASE))
	def test_homepage_view(self):
		
		self.assertTitle('Historypin | Home')
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		
		page_intro = self.e('.page-intro')
		self.assertEqual('{0}/resources/explore/images/homepage-intro-image.jpg'.format(URL_BASE), page_intro.e('img').get_attribute('src'))
		self.assertEqual('Working Together To\nRemember Our History', page_intro.e('h1').text)
		
		self.assertIsInstance(self.e('.partners'), WebElement)
		
		# TODO assert all sections in the future when the test is extended and it is the seperate test suite
	
	@url('{0}/en/collections/'.format(URL_BASE))
	def test_collections_view(self):
		
		self.assertTitle('Historypin | Collections')
		
		all_collections_cnt = self.e('.container.projects-all')
		self.assertEqual('Collections', all_collections_cnt.e('h1').text)
		
		self.assertIsInstance(self.e('#search'), WebElement)
		
		pass

