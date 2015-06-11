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
	
	@unittest.expectedFailure
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_change_description(self):
		
		# TODO fix this when there are user controls (edit and save project)
		
		sleep(1)
		banner			= self.e('#banner')
		project_desc	= banner.e('p').text
		
		self.assertEqual('DO NOT PIN!!!', project_desc)
		
		self.go('{0}{1}/project/edit'.format(URL_BASE, self.PROJECT_URL))
		sleep(1)
		
		project_edit = self.e('#project-form')
		
		self.assertEqual(project_desc, project_edit.e('p textarea').get_attribute('value'))
		
		# edit the desc
		# save the project
		# check if the edited desc is equal to the new one
		# click edit again
		# set back the previous value
	
	@unittest.expectedFailure
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_add_admin(self):
		
		# TODO fix this when there are user controls (edit and save project)
		
		sleep(1)
		banner			= self.e('#banner')
		
		# TODO
		# assert admin
		# click edit project
		# remove existing admin
		# assert that it's not in the list anymore
		# add him again
		# check if it is added
		# save project
		# 
		# 
		# 
		# 
		
		pass
		
	
