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
		self.assertEqual('https://community.historypin.org/c/uncategorized', self.e('.category h3 a').get_attribute('href'))
		self.go('http://v75-beta-2.historypin-hrd.appspot.com')		# add to repair invalid cookie domain