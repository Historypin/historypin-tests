# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_FirstWorldWar(HPTestCase):
	
	PROJECT_URL = '/en/explore/first-world-war-centenary'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		# assert project banner
		header = self.e('#header')
		
		self.assertEqual('{0}{1}/'.format(URL_BASE, self.PROJECT_URL), header.e('.breadcrumbs a').get_attribute('href'))
		self.assertEqual('First World War Centenary', header.e('.breadcrumbs a').text)
		
		banner = self.e('#banner')
		self.assertEqual('First World War Centenary', banner.e('h3').text)
		self.assertIsInstance(banner.e('img'), WebElement)
		
		
		project_logos	= banner.e('.logos')
		logos_links		= project_logos.es('li a')
		logos_imgs		= project_logos.es('li img')
		
		logo_items = [
			['http://www.hlf.org.uk/', '/partnership-hlf-logo.png'],
			['http://www.jisc.ac.uk/', '/partnership-jisc-logo.png'],
			['http://www.iwm.org.uk/', '/partnership-iwm-logo.png'],
			['http://www.ahrc.ac.uk/', '/partnership-ahrc-logo.png'],
		]
		
		for n in range(len(logo_items)):
			i = logo_items[n]
			self.assertEqual(i[0], logos_links[n].get_attribute('href'))
			self.assertEqual('{0}/resources/explore/images{1}'.format(URL_BASE, i[1]), logos_imgs[n].get_attribute('src'))
		
		# self.assertIn('You can use the Historypin First World War Centenary hub to explore and contribute to these projects and add your own.', banner.e('.tab-cnt p').text)
		
		# project_items[0].click()
		
		# self.assertIn('The First World War Centenary hub provides a digital home for these projects', banner.e('#about').text)
		
		# project_items[1].click()
		
		# self.assertFalse(banner.e('#about').is_displayed())
		# self.assertIn('Mae canolbwynt Canmlwyddiannol y Rhyfel Byd Cyntaf', banner.e('#cymraeg').text)
		
		# sub_proj_h3s	= banner.es('.sub-projects-highlights .sub-project-item h3')
		# sub_proj_desc	= banner.es('.sub-projects-highlights .sub-project-item p')
		# sub_proj_links	= banner.es('.sub-projects-highlights .sub-project-item a')
		
		# self.assertEqual('DIGITAL WAR MEMORIAL', sub_proj_h3s[0].text)
		# self.assertEqual('Explore unique creative responses to the First World War made by local communities collaborating with artists.', sub_proj_desc[0].text)
		# self.assertEqual('{0}/en/explore/the-digital-war-memorial/'.format(URL_BASE), sub_proj_links[0].get_attribute('href'))
		
		# self.assertEqual('{0}{1}/project/create/'.format(URL_BASE, self.PROJECT_URL)	, banner.e('.add-project-btn').get_attribute('href'))
		# self.assertEqual('ADD YOUR OWN PROJECT'											, banner.e('.add-project-btn').text)
		
		# self.assertEqual('HLF PROJECTS', sub_proj_h3s[1].text)
		# self.assertEqual('Explore projects supported by the Heritage Lottery Fund.', sub_proj_desc[1].text)
		# self.assertEqual('{0}/en/explore/hlf/'.format(URL_BASE), sub_proj_links[2].get_attribute('href'))
		
	
	def test_project_button_not_logged_in(self):
		self.go(self.PROJECT_URL)
		
		sleep(4)
		banner			= self.e('.panel')
		add_proj_button	= banner.e('.add-project-btn')
		
		add_proj_button.click()
		
		self.assertIsInstance(self.e('#ui-id-1'), WebElement)
	
	@logged_in
	def test_project_button_logged_in(self):
		self.go(self.PROJECT_URL)
		
		sleep(3)
		banner			= self.e('#banner')
		add_proj_button	= banner.e('.add-project-btn')
		
		add_proj_button.click()
		
		self.assertEqual('{0}{1}/project/create/'.format(URL_BASE, self.PROJECT_URL), self.browser.current_url)
		
		self.assertIsInstance(self.e('.panel'), WebElement)
		
		
		# TEST CASES:
		# 1. Sorting by: all possible cases:
			# a. before changing to date added (oldest), check 1-2 items, then change order, check them again
			# b. same with date taken
		
		# 2. make test for searching all possible options:
			# a. search photo, audio, video - verify that for all of them the results are as expected
		
		# 3. search one keyword and get the results
		# 4. search project keyword
		# 5. search for two seperate words
		# 6. make test for load button - if there is no button, stop the test
		# 7. assert about section
		# 8. assert banner
