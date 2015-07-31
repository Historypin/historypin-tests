# -*- coding: utf-8 -*-

from base import *
import os, sys

class Discourse(HPTestCase):
	
	def test_discourse_page(self):
		self.go('https://community.historypin.org/')
		
		self.assertTitle('Historypin Community')
		
		self.assertIsInstance(self.e('#ember1184'), WebElement)  # asserting the header
		self.assertIsInstance(self.e('.list-controls'), WebElement)
	