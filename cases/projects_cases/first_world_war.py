# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_FirstWorldWar(HPTestCase):
	
	PROJECT_URL = '/en/explore/first-world-war-centenary'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		header = self.e('#header')
		
		self.assertEqual('%s%s/' % (URL_BASE, self.PROJECT_URL), header.e('.breadcrumbs a').get_attribute('href'))
		self.assertEqual('First World War Centenary', header.e('.breadcrumbs a').text)
		
		banner		= self.e('#banner')
		project_nav	= banner.e('#project-nav')
		project_items = project_nav.es('li a')
		
		nav_items = [
			['%s%s/#about' % (URL_BASE, self.PROJECT_URL)	, 'ABOUT'],
			['%s%s/#cymraeg' % (URL_BASE, self.PROJECT_URL)	, 'CYMRAEG'],
			['https://s3-eu-west-1.amazonaws.com/wawwd-resources/First+World+War+Centenary_Get+Started+Guide.pdf', 'GET STARTED GUIDE'],
		]
		
		for n in range(len(nav_items)):
			i = nav_items[n]
			self.assertEqual(i[0], project_items[n].get_attribute('href'))
			self.assertEqual(i[1], project_items[n].text)
		
		self.assertIn('You can use the Historypin First World War Centenary hub to explore and contribute to these projects and add your own.', banner.e('.tab-cnt p').text)
		
		project_items[0].click()
		
		self.assertIn('The First World War Centenary hub provides a digital home for these projects', banner.e('#about').text)
		
		project_items[1].click()
		
		self.assertFalse(banner.e('#about').is_displayed())
		self.assertIn('Mae canolbwynt Canmlwyddiannol y Rhyfel Byd Cyntaf', banner.e('#cymraeg').text)
		
		sub_proj_h3s	= banner.es('.sub-projects-highlights .sub-project-item h3')
		sub_proj_desc	= banner.es('.sub-projects-highlights .sub-project-item p')
		sub_proj_links	= banner.es('.sub-projects-highlights .sub-project-item a')
		
		self.assertEqual('DIGITAL WAR MEMORIAL', sub_proj_h3s[0].text)
		self.assertEqual('Explore unique creative responses to the First World War made by local communities collaborating with artists.', sub_proj_desc[0].text)
		self.assertEqual('%s/en/explore/the-digital-war-memorial/' % URL_BASE, sub_proj_links[0].get_attribute('href'))
		
		self.assertEqual('%s%s/project/create/' % (URL_BASE, self.PROJECT_URL)	, banner.e('.add-project-btn').get_attribute('href'))
		self.assertEqual('ADD YOUR OWN PROJECT'									, banner.e('.add-project-btn').text)
		
		self.assertEqual('HLF PROJECTS', sub_proj_h3s[1].text)
		self.assertEqual('Explore projects supported by the Heritage Lottery Fund.', sub_proj_desc[1].text)
		self.assertEqual('%s/en/explore/hlf/' % URL_BASE, sub_proj_links[2].get_attribute('href'))
		
		self.assertIsInstance(self.e('.partnership'), WebElement)
	
	def test_project_button_not_logged_in(self):
		self.go(self.PROJECT_URL)
		
		banner			= self.e('#banner')
		add_proj_button	= banner.e('.add-project-btn')
		
		add_proj_button.click()
		
		self.assertIsInstance(self.e('#ui-id-1'), WebElement)
	
	@logged_in
	def test_project_button_logged_in(self):
		self.go(self.PROJECT_URL)
		
		banner			= self.e('#banner')
		add_proj_button	= banner.e('.add-project-btn')
		
		add_proj_button.click()
		
		self.assertEqual('%s%s/project/create/' % (URL_BASE, self.PROJECT_URL), self.browser.current_url)
		
		self.assertIsInstance(self.e('#banner-form'), WebElement)
		
