# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_View(HPTestCase):
	
	PROJECT_URL = '/en/explore/oreo'
	
	def __test_breadcrumbs(self):
		
		breadcrumbs_items = [
			['/explore/hlf/oreo/'	, 'Explore'],
			['/people'				, 'People'],
			['/projects'			, 'Projects'],
			['/places'				, 'Places'],
			['/explore/hlf/'		, 'Heritage Lottery Funded Projects'],
			['/explore/hlf%2Foreo/'	, 'Project for Quality Assurance'],
		]
		
		site_header = self.e('#site-header')
		breadcrumbs = site_header.es('li a')
		
		for n in range(len(breadcrumbs_items)):
			i = breadcrumbs_items[n]
			self.assertEqual('{0}/en{1}'.format(URL_BASE, i[0]), breadcrumbs[n].get_attribute('href'))
			self.assertEqual(i[1], breadcrumbs[n].text)
		
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_navigation_not_logged_in(self):
		
		self.__test_breadcrumbs()
		self.assertTitle('Historypin | Project for Quality Assurance')
		self.assertTrue(self.e('.breadcrumbs').is_displayed())
		
		self.e('.sign-in').click()
		sleep(2)
		self.assertEqual('Sign in to Historypin', self.e('#ui-id-1>h2').text)
		
		self.e('#ui-id-1 .close-btn-wrapp a').click()
		self.assertFalse(self.e('#ui-id-1').is_displayed())
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
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
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_map(self):
		
		project_info = self.e('.project-meta')
		self.assertEqual('Project for Quality Assurance', project_info.e('h3').text)
		self.assertEqual('About the Project', project_info.e('.about a').text)
		
		self.assertIsInstance(self.e('#map'), WebElement)
		self.assertIsInstance(self.e('#timeline'), WebElement)
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_gallery_view(self):
		
		gallery_section	= self.e('.gallery-listing')
		project_about	= gallery_section.e('.project-about-item')
		
		self.assertEqual('About the project', project_about.e('h3').text)
		self.assertEqual('+ Read more', project_about.e('.read-more').text)
		self.assertIsInstance(project_about.e('.users'), WebElement)
		
		self.assertIsInstance(gallery_section.es('.project-item')[0], WebElement)
		
		self.assertIsInstance(gallery_section.es('.pin-item')[0], WebElement)
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_project_card_logged_in(self):
		# TODO
		# click add project card
		# check if the login dialog opens
		pass
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_add_project_card_not_logged_in(self):
		# TODO
		# click add project card
		# check if the user is sent on the correct url for adding a project
		# go back to oreo project
		pass
	
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_pin_card_logged_in(self):
		# TODO
		# click add a pin card
		# check if the user is sent to the pinning process
		# go back to the projedt
		pass
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_add_pin_card_not_logged_in(self):
		# TODO
		# click add a pin card
		# check if the login dialog opens
		pass
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_favourite_from_card(self):
		
		pass
	
	@unittest.skipUnless(VERSION == 'v622-beta-1', 'Do not run on 6.17')
	@url('{0}/'.format(PROJECT_URL))
	def test_paging(self):
		
		pass
	
	