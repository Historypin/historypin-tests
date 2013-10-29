# -*- coding: utf-8 -*-

from base import *

class Project_PTQH(HPTestCase):
	@url('/project/5-DiamondJubilee')
	def test_homepage(self):
		# TODO
		# check the title
		# verify the current nav and title, and image in the header
		# check the h3 and the main text
		# check the background
		# check the photo
		# check the two buttons - links and texts
		# check the three touts - images, text, links
		# check the section with pins
		# check the tours and collections text links and images
		# check the custom footer links and text, and the logo
		pass
	
	@url('/project/5-DiamondJubilee/visits/')
	def test_visits(self):
		# TODO
		# check the title
		# check the video element present
		# check title
		# check text
		# check at least one visit
		pass
	
	@url('/project/5-DiamondJubilee/map/')
	def test_map(self):
		# TODO
		# title
		# check text
		# check the input
		# check year slider
		# check if there is a map
		pass
	
	@url('/project/5-DiamondJubilee/pin/')
	def test_pin_page(self):
		# TODO
		# check the title
		# check the button link and text
		# check the image
		# check share text and icons
		pass
	
	@url('/project/5-DiamondJubilee/about/')
	def test_about(self):
		# check the title
		# check the titles
		# check the images
		# check the texts
		pass
