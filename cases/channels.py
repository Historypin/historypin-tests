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
	
	def __test_channel_assertion(self):
		channel = self.e('.channels-list li')
		self.assertEqual(URL_BASE + '/channels/view/id/10649049/'						, channel.e('a.logo').get_attribute('href'))
		self.assertEqual(URL_BASE + '/channels/img/10649049/logo/1/dim/70x70/crop/1/'	, channel.e('a.logo img').get_attribute('src'))
		self.assertEqual('Gabss'														, channel.e('a.name').text)
		self.assertEqual(URL_BASE + '/channels/view/id/10649049/'						, channel.e('a.name').get_attribute('href'))
		
		h2 = self.e('.search-channels .right a')
		self.assertEqual('Return to Featured Channels'									, h2.text)
		self.assertEqual(URL_BASE + '/channels/'										, h2.get_attribute('href'))
	
	@url('/channels/')
	def test_search(self):
		self.e('.input-container input').click()
		sleep(1)
		self.e('.input-container input').send_keys("Gabss")
		sleep(1)
		self.e('.button.left').click()
		
		self.__test_channel_assertion()
	
	@url('/channels/')
	def test_search_email(self):
		self.e('.input-container input').click()
		sleep(1)
		self.e('.input-container input').send_keys("g.ananieva@avalith.bg")
		sleep(1)
		self.e('.button.left').click()
		
		h2 = self.e('.search-channels .right a')
		channel = self.e('.channels-list li')
		info = ['/channels/view/id/16857003/', '/resources/avatars/100x100/avatar_1.png', 'gabriela.ananieva', 'Return to Featured Channels', '/channels/']
		for n in range(len(info)):
			self.assertEqual(URL_BASE + info[0]	, channel[n].e('a.logo').get_attribute('href'))
			self.assertEqual(URL_BASE + info[0]	, channel[n].e('a.name').get_attribute('href'))
			self.assertEqual(URL_BASE + info[1]	, channel[n].e('a.logo img').get_attribute('src'))
			self.assertEqual(info[2]			, channel[n].e('a.name').text)
			self.assertEqual(info[3]			, h2[n].text)
			self.assertEqual(URL_BASE + info[4]	, h2[n].get_attribute('href'))
			
		# channel = self.e('.channels-list li')
		# self.assertEqual(URL_BASE + '/channels/view/id/16857003/'				, channel.e('a.logo').get_attribute('href'))
		# self.assertEqual(URL_BASE + '/resources/avatars/100x100/avatar_1.png'	, channel.e('a.logo img').get_attribute('src'))
		# self.assertEqual('gabriela.ananieva'									, channel.e('a.name').text)
		# self.assertEqual(URL_BASE + '/channels/view/id/16857003/'				, channel.e('a.name').get_attribute('href'))
		# 
		# h2 = self.e('.search-channels .right a')
		# self.assertEqual('Return to Featured Channels'									, h2.text)
		# self.assertEqual(URL_BASE + '/channels/'										, h2.get_attribute('href'))
	