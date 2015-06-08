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
	
	@logged_in
	@url('{0}/'.format(PROJECT_URL))
	def test_change_title(self):
		
		sleep(1)
		
		# TODO fix this when there are user controls (edit and save project)
		
		banner			= self.e('#banner')
		project_title	= banner.e('h3').text
		
		self.assertEqual('New project for QA', project_title)
		
		self.go('{0}{1}/project/edit'.format(URL_BASE, self.PROJECT_URL))
		sleep(1)
		
		# project_title	= banner.e('h3')
		project_edit = self.e('#project-form')
		
		self.assertEqual(project_title, project_edit.e('h3 textarea').get_attribute('value'))
		
		
	
	@logged_in
	@url('{0}/project/edit'.format(PROJECT_URL))
	def test_change_description(self):
		pass
	