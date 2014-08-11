# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_DigitalWarMemorial(HPTestCase):
	
	PROJECT_URL = '/en/explore/the-digital-war-memorial'
	PROJECT_FWW = '/en/explore/first-world-war-centenary'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertIn(self.PROJECT_FWW, self.browser.current_url)
		
		sleep(3)
		breadcrumbs_items = self.es('.breadcrumbs li a')
		
		self.assertEqual('First World War Centenary', breadcrumbs_items[0].text)
		self.assertEqual('%s%s/' % (URL_BASE, self.PROJECT_FWW), breadcrumbs_items[0].get_attribute('href'))
		
		self.assertEqual('The Digital War Memorial', breadcrumbs_items[1].text)
		self.assertEqual('%s%s/the-digital-war-memorial/' % (URL_BASE, self.PROJECT_FWW), breadcrumbs_items[1].get_attribute('href'))
		
		banner = self.e('#banner')
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		self.assertIn('The Digital War Memorial brings together communities and artists', banner.e('.description').text)
		
		sub_projects_section	= banner.e('.sub-projects')
		projects				= sub_projects_section.es('a')
		
		self.assertIsInstance(projects[0], WebElement)
		self.assertIsInstance(projects[0].e('img'), WebElement)
		self.assertEqual(9, len(projects))
		
		partners = banner.e('.partnership')
		
		#TODO - add partner links when they are provided
		
		
	
