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
			['Login'				, URL_BASE + '/user/'],
			['Join'					, URL_BASE + '/user/'],
			['Pin'					, URL_BASE + '/upload/'],
		]
		
		for n in range(len(header_items)):
			i = header_items[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
	
	@url('/en/explore/')
	def test_index(self):
		
		self.assertTitle('Historypin')
		
		header	= self.e('#header')
		self.assertEqual('%s/' % URL_BASE, header.e('h1 a').get_attribute('href'))
		
		self.assertEqual('Historypin', self.e('h3').text)
		self.assertIsInstance(self.e('.home-anchor'), WebElement)
		
		timeline = self.e('#timeline')
		self.assertEqual('1800', timeline.e('.start').text)
		self.assertEqual('1800', timeline.e('.ui-slider-handle-left').text)
		
		
		self.assertEqual('2029', timeline.e('.end').text)
		self.assertEqual('2029', timeline.e('.ui-slider-handle-right').text)
		
		self.assertIsInstance(timeline.e('.ui-slider-range'), WebElement)
		
		self.assertIsInstance(self.e('#map'), WebElement)
	
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
		
		self.assertTitle('Historypin')
		
		footer	= self.e('#footer')
		links	= footer.es('li a')
		
		footer_items = [
			['Terms and Conditions'	, URL_BASE + '/terms-and-conditions/'],
			['Privacy Policy'		, URL_BASE + '/privacy-policy/'],
			['Cookies'				, URL_BASE + '/cookies/'],
			['Facebook'				, 'http://www.facebook.com/pages/Historypin/192291707448024/'],
			['Twitter'				, 'http://twitter.com/Historypin/'],
			['Google +'				, 'https://plus.google.com/116628462065893538180/posts/'],
			['Blog'					, 'http://blog.historypin.com/'],
			[u'© We Are What We Do'	, 'http://wearewhatwedo.org/'],
		]
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
	
