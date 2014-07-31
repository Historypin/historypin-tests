# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_DigitalWarMemorial(HPTestCase):
	
	PROJECT_URL = '/en/explore/the-digital-war-memorial'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		pass
