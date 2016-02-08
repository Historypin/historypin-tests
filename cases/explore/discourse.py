# -*- coding: utf-8 -*-

from base import *
import os, sys

class Discourse(HPTestCase):
	
	def test_discourse_page(self):
		self.go('https://community.historypin.org/')
		
		self.e_wait('.title')
		self.assertTitle('Historypin Community')
		
		instance(self, '.ember-view .d-header')
		instance(self, '.list-controls')
		displayed(self, '.category h3 a')
		self.go('http://{0}.historypin-hrd.appspot.com'.format(VERSION))		# add to repair invalid cookie domain