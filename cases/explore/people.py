# -*- coding: utf-8 -*-

from base import *
import os, sys

class People(HPTestCase):
	
	@url('/en/people')
	def test_index(self):
		
		self.assertTitle('Historypin | People')
		# TODO
		# assert title
		# assert collections and places links
	
	
	# @url('')
	# def test_most_popular(self):
		
	# 	# assert if the option menu is ordered by most popular
	# 	# check if the first profile is most viewed
	# 	pass
	
	
	