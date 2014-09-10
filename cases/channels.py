# -*- coding: utf-8 -*-

from base import *

class Channels(HPTestCase):
	
	@url('/channels/')
	def test_index(self):
		self.assertTitle('Historypin | Featured Profiles')
		
		main_img = self.e('.main-image')
		self.assertEqual('%s/channels/#'							 % URL_BASE, main_img.get_attribute('href'))
		self.assertEqual('%s/resources/images/channels/channels.jpg' % URL_BASE, main_img.e('img').get_attribute('src'))
		
		self.assertEqual('Historypin Profiles', self.e('.info h1').text)
		
		paragraph = self.es('.info p')
		self.assertEqual("Profiles hold everything someone has added to Historypin, including any Tours and Collections they've created, stories other people have added to their content and any Historypin Repeats of their images.", paragraph[0].text)
		self.assertEqual("Remember: Profiles are personalisable so can be re-designed to look just how you want them!", paragraph[1].text)
		
		self.assertEqual("Search Profiles"		, self.e('.search-channels h2').text)
		self.assertEqual("Some Featured Profiles"	, self.e('.search h2').text)
		
		channel = self.e('.channels-list li')
		self.assertIsInstance(channel.e('img')		, WebElement)
		self.assertIsInstance(channel.e('a.logo')	, WebElement)
		self.assertIsInstance(channel.e('a.name')	, WebElement)
	
	def __test_channel_assertion(self):
		self.assertEqual('Search Results for "Gabss":', self.e('.search > h2').text)
		channel = self.e('.channels-list li')
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW)							, channel.e('a.logo').get_attribute('href'))
		self.assertEqual('%s/channels/img/%d/logo/1/dim/70x70/crop/1/' % (URL_BASE, ID_USER_VIEW)	, channel.e('a.logo img').get_attribute('src'))
		self.assertEqual('Gabss'																	, channel.e('a.name').text)
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW)							, channel.e('a.name').get_attribute('href'))
		
		h2 = self.e('.search-channels .right a')
		self.assertEqual('Return to Featured Profiles'	, h2.text)
		self.assertEqual('%s/channels/'	% URL_BASE		, h2.get_attribute('href'))
	
	@url('/channels/')
	def test_search(self):
		
		input_search = self.e('.input-container input')
		input_search.click()
		sleep(1)
		input_search.send_keys("Gabss")
		sleep(1)
		self.e('.button.left').click()
		
		self.__test_channel_assertion()
	
	@url('/channels/')
	def test_search_email(self):
		
		input_search = self.e('.input-container input')
		
		input_search.click()
		sleep(1)
		input_search.send_keys("g.ananieva@avalith.bg")
		sleep(1)
		self.e('.button.left').click()
		
		self.assertEqual('Search Results for "g.ananieva@avalith.bg":', self.e('.search > h2').text)
		
		channel = self.e('.channels-list li:nth-of-type(1)')
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW)							, channel.e('a.logo').get_attribute('href'))
		self.assertEqual('%s/channels/img/%d/logo/1/dim/70x70/crop/1/' % (URL_BASE, ID_USER_VIEW)	, channel.e('a.logo img').get_attribute('src'))
		self.assertEqual('Gabss'																	, channel.e('a.name').text)
		self.assertEqual('%s/channels/view/%d/' % (URL_BASE, ID_USER_VIEW)							, channel.e('a.name').get_attribute('href'))
		
		h2 = self.e('.search-channels .right a')
		self.assertEqual('Return to Featured Profiles'	, h2.text)
		self.assertEqual('%s/channels/'	% URL_BASE, h2.get_attribute('href'))

