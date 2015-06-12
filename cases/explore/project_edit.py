# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_Edit(HPTestCase):
	
	PROJECT_URL = '/en/hlf/oreo/new-project-qa'
	
	@logged_in
	@url('{0}/project/edit'.format(PROJECT_URL))
	def test_change_image(self):
		
		
		# TODO
		# discuss with Sasho how we're going to assert the image
		pass
	
	# @unittest.expectedFailure
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_change_title(self):
		
		sleep(1)
		
		banner			= self.e('#banner')
		project_title	= banner.e('h3').text
		
		self.assertEqual('New project for QA', project_title)
		
		user_controls	= self.e('#main-header .temp')
		editing_project	= user_controls.es('li a')[0]
		saving_project	= user_controls.es('li a')[1]
		
		editing_project.click()
		sleep(1)
		
		project_edit_title = self.e('#project-form h3 textarea')
		
		self.assertEqual(project_title, project_edit_title.get_attribute('value'))
		
		project_edit_title.send_keys(' was being edited')
		
		saving_project.click()
		sleep(1)
		
		editing_project	= user_controls.es('li a')[0]
		editing_project.click()
		sleep(1)
		
		project_edit_title = self.e('#project-form h3 textarea')
		project_edit_title.clear()
		
		project_edit_title.send_keys('New project for QA')
		saving_project.click()
		sleep(1)
		
		self.assertEqual('New project for QA', project_title)
	
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_change_description(self):
		
		sleep(1)
		banner			= self.e('#banner')
		project_desc	= banner.e('p').text
		
		self.assertEqual('DO NOT PIN!!!', project_desc)
		
		user_controls	= self.e('#main-header .temp')
		editing_project	= user_controls.es('li a')[0]
		saving_project	= user_controls.es('li a')[1]
		
		editing_project.click()
		sleep(1)
		
		project_edit_desc = self.e('#project-form .short-desc-wrap textarea')
		
		self.assertEqual(project_desc, project_edit_desc.get_attribute('value'))
		
		project_edit_desc.send_keys(' The description was being edited')
		
		saving_project.click()
		sleep(1)
		
		editing_project	= user_controls.es('li a')[0]
		editing_project.click()
		sleep(1)
		
		project_edit_desc = self.e('#project-form .short-desc-wrap textarea')
		project_edit_desc.clear()
		
		project_edit_desc.send_keys('DO NOT PIN!!!')
		saving_project.click()
		sleep(1)
		
		self.assertEqual('DO NOT PIN!!!', project_desc)
	
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_admin(self):
		
		# TODO fix this when there are user controls (edit and save project)
		
		banner			= self.e('#banner')
		sleep(3)
		project_admin	= banner.es('.user-img')[2]
		
		self.assertEqual('/en/person/{0}'.format(ID_USER_EXPLORE), project_admin.get_attribute('href'))
		
		user_controls	= self.e('#main-header .temp')
		editing_project	= user_controls.es('li a')[0]
		saving_project	= user_controls.es('li a')[1]
		
		editing_project.click()
		sleep(1)
		
		banner			= self.e('#banner')
		
		project_edit_admin_delete = banner.e('.user-img:nth-of-type(3) .user-remove .ss-delete')
		project_edit_admin_delete.click()
		
		saving_project.click()
		sleep(3)
		
		
		# self.assertIsNotInstance(banner.es('.user-img')[2], WebElement)
		self.assertFalse(self.e('#banner').exists('.user-img:nth-of-type(3)'))
		
		editing_project	= user_controls.es('li a')[0]
		saving_project	= user_controls.es('li a')[1]
		
		editing_project.click()
		sleep(2)
		
		self.e('#banner .ui-autocomplete-input').send_keys('gabriela1')
		sleep(2)
		self.e('.ui-autocomplete li').click()
		sleep(2)
		self.assertTrue(self.e('#banner').exists('.user-img:nth-of-type(3) .user-remove .ss-delete'))
		
		saving_project.click()
		sleep(3)
		
		banner			= self.e('#banner')
		project_admin	= banner.es('.user-img')[2]
		
		self.assertEqual('/en/person/{0}'.format(ID_USER_EXPLORE), project_admin.get_attribute('href'))
	