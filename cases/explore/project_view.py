# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_View(HPTestCase):
	
	PROJECT_URL = '/en/hlf/oreo/new-project-qa'
	
	def __test_breadcrumbs(self):
		
		breadcrumbs_items = [
			['/hlf%2Foreo/'						, 'Explore'],
			['/people'							, 'People'],
			['/projects'						, 'Projects'],
			['/places'							, 'Places'],
			['/hlf/'							, 'Heritage Lottery Funded Projects'],
			['/hlf%2Foreo/'						, 'Project for Quality Assurance'],
			['/hlf%2Foreo%2Fnew-project-qa/'	, 'New project for QA'],
		]
		
		site_header = self.e('#site-header')
		breadcrumbs = site_header.es('li a')
		
		for n in range(len(breadcrumbs_items)):
			i = breadcrumbs_items[n]
			self.assertEqual('{0}/en{1}'.format(URL_BASE, i[0]), breadcrumbs[n].get_attribute('href'))
			self.assertEqual(i[1], breadcrumbs[n].text)
		
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_navigation_not_logged_in(self):
		
		self.__test_breadcrumbs()
		self.assertTitle('Historypin | New project for QA')
		
		self.assertTrue(self.e('.breadcrumbs').is_displayed())
		
		self.e('.sign-in').click()
		sleep(2)
		self.assertEqual('Sign in to Historypin', self.e('#ui-id-1>h2').text)
		
		self.e('#ui-id-1 .close-btn-wrapp a').click()
		self.assertFalse(self.e('#ui-id-1').is_displayed())
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_navigation_logged_in(self):
		
		self.__test_breadcrumbs()
		
		self.e('.user-actions-triger').click()
		sleep(3)
		
		user_actions = self.e('.actions-list')
		
		self.assertEqual('{0}/en/person/{1}'.format(URL_BASE, ID_USER), user_actions.e('.my_profile').get_attribute('href'))
		self.assertEqual('{0}/user/logout/'.format(URL_BASE), user_actions.e('.logout').get_attribute('href'))
		
		self.assertIsInstance(self.e('#button_edit'), WebElement)
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_map(self):
		
		project_info = self.e('.project-meta')
		self.assertIsInstance(self.e('#timeline'), WebElement)
		
		self.assertEqual('PROJECT FOR QUALITY ASSURANCE', self.e('h2 a').text)
		
		self.assertEqual('About the Project', project_info.e('.about a').text)
		
		self.assertIsInstance(self.e('#map'), WebElement)
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_gallery_view(self):
		
		self.assertIsInstance(self.e('#search'), WebElement)
		
		gallery_section	= self.e('.gallery-listing')
		project_about	= gallery_section.e('.project-about-item')
		
		self.assertEqual('About the project', project_about.e('h3').text)
		self.assertEqual('+ Read more', project_about.e('.read-more').text)
		self.assertIsInstance(project_about.e('.users'), WebElement)
		
		# self.assertIsInstance(gallery_section.es('.project-item')[0], WebElement) there is no child project
		self.assertIsInstance(gallery_section.es('.pin-item')[0], WebElement)
		
		user_card = gallery_section.e('.user-item')
		self.assertEqual('TOP PINNER', user_card.e('h4').text)
		
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_project_card_logged_in(self):
		
		add_project_card = self.e('.add-project')
		add_project_card.click()
		
		self.assertEqual('{0}{1}/project/create'.format(URL_BASE, self.PROJECT_URL), self.browser.current_url)
		self.go(self.PROJECT_URL)
		
		self.assertEqual('New project for QA', self.e('#banner h3').text)
		
		#TODO should start the test after the google login is fixed
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_add_project_card_not_logged_in(self):
		
		add_project_card = self.e('.add-project')
		add_project_card.click()
		self.assertEqual('Sign in to Historypin', self.e('#ui-id-1 h2').text)
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_pin_card_logged_in(self):
		
		add_pin_card = self.e('.add-pin-item')
		add_pin_card.click()
		# TODO complete the test when path for pinning is fixed
		# check if the user is sent to the pinning process
		# go back to the projedt
		pass
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_add_pin_card_not_logged_in(self):
		
		add_pin_card = self.e('.add-pin-item')
		add_pin_card.click()
		self.assertEqual('Sign in to Historypin', self.e('#ui-id-1 h2').text)
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_favourite_from_card(self):
		
		pass
	
	@unittest.skipUnless(VERSION == 'v623-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_paging(self):
		
		pass
	
	