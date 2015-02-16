# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_View(HPTestCase):
	
	PROJECT_URL = '/en/explore/oreo'
	
	@url('{0}/'.format(PROJECT_URL))
	def test_navigation_not_logged_in(self):
		
		self.assertTitle('Historypin | Project for Quality Assurance')
		self.assertTrue(self.e('.breadcrumbs').is_displayed())
		
		self.e('.sign-in').click()
		sleep(2)
		self.assertEqual('Sign in to Historypin', self.e('#ui-id-1>h2').text)
		
		self.e('#ui-id-1 .close-btn-wrapp a').click()
		self.assertFalse(self.e('#ui-id-1').is_displayed())
	
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_navigation_logged_in(self):
		
		self.e('.user-actions-triger').click()
		sleep(3)
		
		user_actions = self.e('.actions-list')
		
		self.assertEqual('{0}/channels/view/{1}/'.format(URL_BASE, ID_USER), user_actions.e('.my_profile').get_attribute('href'))
		self.assertEqual('{0}/user/logout/'.format(URL_BASE), user_actions.e('.logout').get_attribute('href'))
		
		self.assertIsInstance(self.e('#button_edit'), WebElement)
	
	@url('{0}/'.format(PROJECT_URL))
	def test_map(self):
		
		project_info = self.e('.project-meta')
		self.assertEqual('Project for Quality Assurance', project_info.e('h3').text)
		self.assertEqual('About the Project', project_info.e('.about a').text)
		
		self.assertIsInstance(self.e('#map'), WebElement)
		self.assertIsInstance(self.e('#timeline'), WebElement)
	
	@url('{0}/'.format(PROJECT_URL))
	def test_main_project_section(self):
		# TODO
		# check add a project card link
		# check add a pin card
		# check about card
		# check child project
		# check pin card
		# check if there is 3 cards per row
		pass
	
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_project_card_logged_in(self):
		# TODO
		# click add project card
		# check if the login dialog opens
		pass
	
	@url('{0}/'.format(PROJECT_URL))
	def test_add_project_card_not_logged_in(self):
		# TODO
		# click add project card
		# check if the user is sent on the correct url for adding a project
		# go back to oreo project
		pass
	
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_pin_card_logged_in(self):
		# TODO
		# click add a pin card
		# check if the user is sent to the pinning process
		# go back to the projedt
		pass
	
	@url('{0}/'.format(PROJECT_URL))
	def test_add_pin_card_not_logged_in(self):
		# TODO
		# click add a pin card
		# check if the login dialog opens
		pass
	
	@url('{0}/'.format(PROJECT_URL))
	def test_favourite_from_card(self):
		
		pass
	
	@url('{0}/'.format(PROJECT_URL))
	def test_paging(self):
		
		pass
	
	