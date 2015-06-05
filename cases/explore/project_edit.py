# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_Edit(HPTestCase):
	
	PROJECT_URL = '/en/hlf/oreo/new-project-qa'
	
	@logged_in
	@url('{0}/project/edit'.format(self.PROJECT_URL))
	def test_change_image(self):
		# TODO
		# discuss with Sasho how we're going to assert the image
		pass
	
	@logged_in
	@url('{0}/project/edit'.format(self.PROJECT_URL))
	def test_change_title(self):
		sleep(1)
		
		# TODO
		# discuss with Sasho how we're going to get the current title
		
		pass
	
	@logged_in
	@url('{0}/project/edit'.format(self.PROJECT_URL))
	def test_change_description(self):
		pass
	