# -*- coding: utf-8 -*-

from base import *

class Tours(HPTestCase):
	
	def __test_collection_listing(self):
		self.assertTitle('Historypin | Tours')
		
		main_cnt = self.e('.inner.cf')
		self.assertEqual(URL_BASE + '/tours/'									, main_cnt.e('a.main-image').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/tour-homepage-index.png'	, main_cnt.e('img').get_attribute('src'))
		self.assertEqual('What are Tours?'										, main_cnt.e('h1').text)
		self.assertEqual('Tours lead you step-by-step through a series of pieces of content, telling a story, exploring a place or walking through time. Take one of the Tours below or put your own together, using any content on Historypin.'
						, main_cnt.e('p').text)
		button = main_cnt.e('a.next-button')
		self.assertEqual(URL_BASE + '/tours/add'								, button.get_attribute('href'))
		self.assertEqual('Make your own tour'									, button.text)
		
		self.assertEqual('Return to Tours & Collections', self.e('h3.right').text)
		self.assertEqual(URL_BASE + '/curated'			, self.e('h3.right a').get_attribute('href'))
		self.assertEqual('All Tours'					, self.e('h3.right ~ h3').text)
		
		cnt = self.es('#photo_list_content .list li:nth-of-type(1)')
		self.assertIsInstance(cnt[0].e('a')	, WebElement)
		self.assertIsInstance(cnt[0].e('img')	, WebElement)
		self.assertIsInstance(cnt[0].e('p')	, WebElement)
		
		self.assertIn('tour-icon'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-hiker'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'		, cnt[0].e('a span').get_attribute('class'))
		
	@url('/tours/')
	def test_index(self):
		self.__test_collection_listing()
	
	@url('/tours/all')
	def test_all(self):
		self.__test_collection_listing()
		
		next = self.e('.show-next')
		self.assertEqual('Next'							, next.text)
		self.assertEqual(URL_BASE + '/tours/all/page/2/', next.get_attribute('href'))
	
	@url('/tours/view/id/' + KEY_TOUR)
	def test_view(self):
		self.assertTitle('Historypin | Tours - Test Tour for automated test')
		
		self.assertEqual(URL_BASE + '/services/thumb/phid/1031013/dim/451x302/crop/1/'	, self.e('img.index').get_attribute('src'))
		self.assertEqual(URL_BASE + '/tours/view/id/22354015/title/Test%2520Tour%2520for%2520automated%2520test/#', self.e('a.main-image').get_attribute('href'))
		self.assertEqual('Test Tour for automated test'									, self.e('.info h2').text)
		
		paragraphs = self.es('.info p')
		self.assertEqual('Description for Test Tour for automated test'					, paragraphs[0].text)
		self.assertEqual('Created by Gabss'												, paragraphs[1].text)
		self.assertEqual(URL_BASE + '/channels/view/10649049'							, paragraphs[1].e('a').get_attribute('href'))
		
		button = self.e('.tour-button')
		self.assertEqual('Take the Tour'																	, button.text)
		self.assertEqual(URL_BASE + '/tours/take/id/22354015/title/Test%20Tour%20for%20automated%20test/#1'	, button.get_attribute('href'))
		
		tabs = self.es('.list_tabs li')
		self.assertIsInstance(tabs[0]	, WebElement)
		self.assertEqual('Map View'		, tabs[0].e('span').text)
		self.assertIsInstance(tabs[1]	, WebElement)
		self.assertEqual('List View'	, tabs[1].e('span').text)
		self.assertIsInstance(tabs[2]	, WebElement)
		self.assertEqual('Tour View'	, tabs[2].e('span').text)
		
		photo_list_cnt = [
				['1', '1031013', 'Airplane crash on Wallace Road - 13 July 1952'],
				['2', '1076031', "'Hop Bine', Drove Road, Biggleswade 1914 - 1 January 1914"],
				['3', '2172029', 'Sabarabussu,MG,Brasil - 1898'],
				['4', '3255004', 'Diving Horse at Hanlan\'s Point - 1908'],
				['5', '22363018', 'National Theatre in Sofia, Bulgaria - 2 August 2012'],
		]
		
		photos_list	= self.e('#list_view .list')
		number		= photos_list.es('strong')
		links		= photos_list.es('.link-image')
		images		= photos_list.es('img')
		paragraphs	= photos_list.es('p:nth-of-type(1)')
		start		= photos_list.es('.start-here')
		start_link	= URL_BASE + '/tours/take/id/22354015/title/Test%20Tour%20for%20automated%20test/#'
		
		for n in range(len(photo_list_cnt)):
			i = photo_list_cnt[n]
			self.assertEqual(i[0]				, number[n].text)
			self.assertEqual(start_link + i[0]	, links[n].get_attribute('href'))
			self.assertEqual(start_link + i[0]	, start[n].get_attribute('href'))
			self.assertEqual(i[2]				, paragraphs[n].text)
			self.assertEqual('Start from here'	, start[n].text)
			
			self.assertEqual(URL_BASE + '/services/thumb/phid/' + i[1] + '/dim/195x150/crop/1/', images[n].get_attribute('src'))
			
		# assert all images, links texts and start from here button text and link, and photo number start from here and start from here link like [1]
		# TODO LATER
		# - representing photo
	
	@unittest.skip('TODO')
	@url('/tours/take/id/' + KEY_TOUR)
	def test_take(self):
		# 
		# 
		# 
		# 
		# 
		# 
		# 
		# 
		# 
		# 
		pass
	