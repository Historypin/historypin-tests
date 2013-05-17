# -*- coding: utf-8 -*-

from base import *

class Channels(HPTestCase):
	
	@url('/channels/')
	def test_index(self):
		self.assertTitle('Historypin | Featured Channels')
		
		main_img = self.e('.main-image')
		self.assertEqual(URL_BASE + '/channels/#'								, main_img.get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/channels/channels.jpg'	, main_img.e('img').get_attribute('src'))
		
		self.assertEqual('Historypin Channels', self.e('.info h1').text)
		
		paragraph = self.es('.info p')
		self.assertEqual("Channels hold everything someone has added to Historypin, including any Tours and Collections they've created, stories other people have added to their content and any Historypin Repeats of their images.", paragraph[0].text)
		self.assertEqual("Remember: Channels are personalisable so can be re-designed to look just how you want them!", paragraph[1].text)
		
		self.assertEqual("Search Channel Names"		, self.e('.search-channels h2').text)
		self.assertEqual("Some Featured Channels"	, self.e('.search h2').text)
		
		channel = self.e('.channels-list li')
		self.assertIsInstance(channel.e('img')		, WebElement)
		self.assertIsInstance(channel.e('a.logo')	, WebElement)
		self.assertIsInstance(channel.e('a.name')	, WebElement)
	
	@url('/channels/')
	def test_search(self):
		
		# TODO
		# search:
		# - type a channel
		# - click go
		# - assert that typed channel is equal to channel name
		# test search e-mail - expected failure
		# return to featured channels link and text
		pass
		
	@unittest.expectedFailure
	@url('/channels/')
	def test_search_email(self):
		
		
		pass