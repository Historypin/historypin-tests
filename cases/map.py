# -*- coding: utf-8 -*-

from base import *

class Map(HPTestCase):
	
	@url('/map/')
	def test_index(self):
		# TODO
		# asssert title
		# assert main panel:
		# - assert search by place text
		# - assert assert input text field
		# - assert Go button link and text
		# - assert Narrow down text
		# - assert by date and by subject text
		# - assert show  thumbnails 
		# - assert fullscreen text and icon
		# asset if map is visible(assertIsInstance)
		pass
	
	@url('/map/')
	def test_search(self):
		
		
		
		pass
	
	@url('/map/')
	def test_search_by_date(self):
		
		
		pass
	
	@url('/map/')
	def test_search_by_place(self):
		
		
		pass
	
	@url('/map/')
	def test_fullscreen_map(self):
		
		
		pass
	
	@url('/map/')
	def test_photo_cluster(self):
		#test photo cluster gallery
		
		pass
	
	@url('/map/')
	def test_hp_marker(self):
		#to test dialogue
		
		pass
	
	@url('/map/')
	def test_footer(self):
		
		footer = [
			[URL_BASE + '/'						, 'Home'],
			[URL_BASE + '/about-us'				, 'About'],
			[URL_BASE + '/faq'					, 'FAQs'],
			[URL_BASE + '/presscentre'			, 'Press Centre'],
			[URL_BASE + '/donate'				, 'Support us'],
			[URL_BASE + '/app'					, 'Mobile App'],
			[URL_BASE + '/terms-and-conditions'	, 'Terms and Conditions'],
			[URL_BASE + '/privacy-policy'		, 'Privacy Policy'],
			[URL_BASE + '/cookies'				, 'Cookies'],
			[URL_BASE + '/contact'				, 'Contact'],
			['http://wearewhatwedo.org/'		, u'© 2012 We Are What We Do'],
		]
		
		lists = self.es('.nav.cf li a')
		
		for n in range(len(footer)):
			i = footer[n]
			self.assertEqual(i[0]			, lists[n].get_attribute('href'))
			self.assertEqual(i[1]			, lists[n].text)
	
