# -*- coding: utf-8 -*-

from base import *
import os, sys

class Homepage_V6(HPTestCase):
	
	@url('/en/explore/')
	def test_header(self):
		
		self.assertTitle('Historypin')
		
		
		header	= self.e('#header')
		links	= header.es('li a')
		
		header_items = [
			['Home'					, URL_BASE + '/'],
			['Map'					, URL_BASE + '/map/'],
			['Projects'				, URL_BASE + '/projects/'],
			['Channels'				, URL_BASE + '/channels/'],
			['Tours and Collections', URL_BASE + '/curated/'],
			['Get Involved'			, URL_BASE + '/community/'],
			['Blog'					, 'http://blog.historypin.com/'],
			['Pin'					, URL_BASE + '/upload/'],
			['Join'					, URL_BASE + '/user/'],
			['Login'				, URL_BASE + '/user/'],
		]
		
		for n in range(len(header_items)):
			i = header_items[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
	
	@url('/en/explore/')
	def test_index(self):
		self.assertEqual('%s/' % URL_BASE, header.e('h1 a').get_attribute('href'))
		# assert HP logo and link
		# assert HP text and i-icon, also text by
		# assert year slider
		# assert map
		
		pass
	
	
	@url('/en/explore/')
	def test_pin(self):
		# click on the pin on the map
		# assert title views and link to the channel
		# assert image
		# assert description and infor
		# assert the tooltip on the map
		# assert year slider
		# close the sidebar
		# assert that it's closed
		pass
	
	@url('/en/explore/1989')
	def test_project(self):
		# TODO
		# check text
		# check the exact years
		# check the text when it is expanded
		# check explore the map
		# check share icons on hover the icon
		# click explore the map
		# check if it is hidden
		pass
	
	@url('/en/explore/')
	def test_footer(self):
		# assert footer links
		pass
	
