# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_VictorianLondon(HPTestCase):
	
	PROJECT_URL = '/en/explore/victorian-london/'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		# TODO
		# assert title
		# assert in text
		# assert link
		# assert headings, links and texts for projects
		# assert logo
		pass
	
	def test_about(self):
		self.go(self.PROJECT_URL)
		# TODO
		# click link find out more
		# see if about title is on the page
		# click go back
		# see if find out more is on the page
		pass
	