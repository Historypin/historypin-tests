# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_FirstWorldWar(HPTestCase):
	
	PROJECT_URL = '/en/explore/first-world-war-centenary'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		pass
