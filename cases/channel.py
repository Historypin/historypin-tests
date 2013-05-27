# -*- coding: utf-8 -*-

from base import *

class Channel(HPTestCase):
	
	@url('/channels/view/10649049/')
	def test_channel_info(self):
		self.assertTitle('Gabss | Historypin')
		
		info = self.e('.chan.info')
		self.assertEqual('Gabss'														, info.e('h2').text)
		self.assertEqual(URL_BASE + '/channels/img/10649049/logo/1/dim/200x200/crop/1/'	, info.e('img').get_attribute('src'))
		
		self.assertEqual('Find out more at: avalith.bg'					, self.e('.chan.info br~p').text)
		
		link = self.es('.chan.info br~p a')
		self.assertEqual('avalith.bg'									, link[0].text)
		self.assertEqual('http://avalith.bg/'							, link[0].get_attribute('href'))
		self.assertEqual('Find me on Facebook'							, link[1].text)
		self.assertEqual('http://www.facebook.com/gabriela.ananieva.7'	, link[1].get_attribute('href'))
		self.assertEqual('Follow me on Twitter'							, link[2].text)
		self.assertEqual('http://twitter.com/@Tristania90'				, link[2].get_attribute('href'))
		self.assertEqual('Visit my blog'								, link[3].text)
		self.assertEqual('http://test/'									, link[3].get_attribute('href'))
	
	@url('/channels/view/10649049/')
	def test_channel_details(self):
		
		h3 = self.es('.chan.options h3')
		self.assertEqual('Channel Details'	, h3[0].text)
		self.assertEqual('Share:'			, h3[1].text)
		
		paragraph = self.e('.chan.options p')
		texts = ['Channel views:', 'Fans:', 'Pins:', 'Tours:', 'Collections:']
		for n in range(len(texts)):
			self.assertIn(texts[n], paragraph.text)
		
		button = self.e('.channel-button.left')
		self.assertEqual('Become a Fan'										, button.text)
		self.assertEqual(URL_BASE + '/user/?from=/channels/view/10649049/'	, button.get_attribute('href'))
		
		social_buttons = self.e('.addthis_toolbox span')
		self.assertIn('ss-icon', social_buttons.get_attribute('class'))
		
		social_icons = ['ss-social-circle', 'ss-social-circle', 'ss-social-circle', 'ss-plus']
		
		for n in range(len(social_icons)-1):
			self.assertIn(social_icons[n], social_buttons.get_attribute('class'))
	
	@url('/attach/uid10649049/map/index/#!/geo:-20.393764,-25.431596/zoom:3/')
	def test_map_tab(self):
		
		map_tab = self.e('.list_tabs .first')
		self.assertEqual('Map'										, map_tab.text)
		
		self.assertIsInstance(self.e('#search-filters input#location')	, WebElement)
		self.assertIsInstance(self.e('#search-filters input#tags')		, WebElement)
		self.assertIsInstance(self.e('#photo_search_submit')			, WebElement)
		self.assertEqual('GO', self.e('#photo_search_submit').e('span').text)
		
		self.assertIsInstance(self.e('#date-selector #date-slider')	, WebElement)
		self.assertIsInstance(self.e('#date-slider-labels li')		, WebElement)
	
	@url('/attach/uid10649049/map/index/#!/geo:-20.393764,-25.431596/zoom:3/')
	def test_list_tab(self):
		# TODO
		# click on List Tab
		# assert list text
		# assert list filter radio buttons and texts
		# assert img link and text
		# assert img icons - info actions
		# assert info
		# assert h5s
		# assert paragraphs
		pass
	
	@url('/attach/uid10649049/map/index/#!/geo:-20.393764,-25.431596/zoom:3/')
	def test_collections_tab(self):
		# TODO
		# click on Collections Tab
		# assert collections text
		# assert collection img
		# assert collection link
		# assert icon
		# assert text
		# assert collection link
		# assert channel link
		pass
	
	@url('/attach/uid10649049/map/index/#!/geo:-20.393764,-25.431596/zoom:3/')
	def test_tours_tab(self):
		# TODO
		# click on Tours Tab
		# assert tours text and link
		# assert image src
		# assert image link
		# assert tour icon
		# assert text
		# assert tour link
		# assert channel link
		pass
	
	@url('/channels/view/10649049/')
	def test_repeats_section(self):
		
		repeats = self.e('.chan.replicas')
		
		self.assertEqual('Historypin Repeats'									, repeats.e('h3').text)
		self.assertEqual(u'Historypin Repeats are created using the Historypin Smartphone App. They are modern replicas of your photos taken by other people or modern replicas of other person’s photos taken by you.', repeats.e('p:nth-of-type(1)').text)
		self.assertEqual('http://www.v4-22-00.historypin-hrd.appspot.com/app/'	, repeats.e('p:nth-of-type(1) a').get_attribute('href'))
		self.assertEqual('This Channel has no Historypin Repeats'				, repeats.e('p:nth-of-type(2)').text)
	
	@url('/channels/view/10649049/')
	def test_comment_feed(self):
		
		text_feed = self.e('.chan.story')
		self.assertEqual('Comment Feed'												, text_feed.e('h3').text)
		self.assertEqual('Comments posted to your media by you or by other people.'	, text_feed.e('p').text)
		
		feed = self.e('.feed.scrollbarfix li')
		
		self.assertIsInstance(feed.e('a')	, WebElement)
		self.assertIsInstance(feed.e('img')	, WebElement)
		self.assertIsInstance(feed.e('p')	, WebElement)
