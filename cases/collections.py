# -*- coding: utf-8 -*-

from base import *

class Collections(HPTestCase):
	
	def __test_collection_listing(self):
		self.assertTitle('Historypin | Collections')
		
		main_cnt	= self.e('.col.w34')
		self.assertEqual('What are Collections?'									, main_cnt.e('h1').text)
		self.assertEqual(URL_BASE + '/collections/'									, main_cnt.e('a.main-image.no-shadow').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/collections_page_image.jpg'	, main_cnt.e('img').get_attribute('src'))
		self.assertEqual('Collections bring together content around a particular topic or theme. You can explore the Collections or create a Collection of your own.',
						main_cnt.e('p').text)
		
		button		= self.e('.col.w34 a.next-button.left')
		self.assertEqual(URL_BASE + '/collections/add'	, button.get_attribute('href'))
		self.assertEqual('Make your own collection'		, button.e('span').text)
		
		self.assertEqual('All Collections'				, self.e('h3:last-of-type').text)
		
		h3 = self.e('h3.right a')
		self.assertEqual('Return to Tours & Collections', h3.text)
		self.assertEqual(URL_BASE + '/curated'			, h3.get_attribute('href'))
		
		cnt	= self.es('#photo_list_content .list li:nth-of-type(1)')
		self.assertIsInstance(cnt[0].e('a')	, WebElement)
		self.assertIsInstance(cnt[0].e('img')	, WebElement)
		self.assertIsInstance(cnt[0].e('p')	, WebElement)
		
		self.assertIn('collection-icon'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-pictures'		, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'			, cnt[0].e('a span').get_attribute('class'))
	
	@url('/collections/')
	def test_index(self):
		self.__test_collection_listing()
	
	@url('/collections/all')
	def test_all(self):
		self.__test_collection_listing()
		
		next = self.e('.show-next')
		self.assertEqual('Next'									, next.text)
		self.assertEqual(URL_BASE + '/collections/all/page/2/'	, next.get_attribute('href'))
	
	@url('/collections/view/id/' + KEY_COLLECTION)
	def test_view(self):
		self.assertTitle('Historypin | Collection - Test Collection for automated test')
		
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/451x302/crop/1/'	, self.e('img.index').get_attribute('src'))
		self.assertEqual('Test Collection for automated test'							, self.e('.info h2').text)
		
		paragraphs = self.es('.info p')
		self.assertEqual('Description for Test Collection for automated test'	, paragraphs[0].text)
		self.assertEqual('Created by Gabss'										, paragraphs[1].text)
		self.assertEqual(URL_BASE + '/channels/view/10649049'					, paragraphs[1].e('a').get_attribute('href'))
		
		button = self.e('.info ~ a')
		self.assertEqual(URL_BASE + '/collections/slideshow/id/22782015/'	, button.get_attribute('href'))
		self.assertEqual('Slide Show'										, button.text)
		
		collection_view = [
			['/map/#!/geo:42.693738,23.326101/zoom:15/dialog:22363018/tab:details/', '/services/thumb/phid/22363018/dim/195x150/crop/1/', '2 August 2012, from Gabss', '/channels/view/10649049'],
			['/map/#!/geo:51.362619,0.513102/zoom:15/dialog:1031013/tab:details/', '/services/thumb/phid/1031013/dim/195x150/crop/1/', '13 July 1952, from Mirrorpix Archives', '/channels/view/571038'],
			['/map/#!/geo:52.087599,-0.25404/zoom:15/dialog:1076031/tab:details/', '/services/thumb/phid/1076031/dim/195x150/crop/1/', '1 January 1914, from Biggleswade History Society', '/channels/view/1042029'],
			['/map/#!/geo:-19.8891792,-43.8048137/zoom:15/dialog:2172029/tab:details/', '/services/thumb/phid/2172029/dim/195x150/crop/1/', '1898, from by Dyno', '/channels/view/2137026'],
			['/map/#!/geo:43.622221047,-79.3740749359/zoom:15/dialog:3255004/tab:details/', '/services/thumb/phid/3255004/dim/195x150/crop/1/', '1908, from FQ', '/channels/view/3154007'],
		]
		
		item = self.es('#list_view .list li')
		for n in range(len(collection_view)):
			i = collection_view[n]
			self.assertEqual(URL_BASE + i[0], item[n].e('a.link-image').get_attribute('href'))
			self.assertEqual(URL_BASE + i[1], item[n].e('img').get_attribute('src'))
			self.assertEqual(i[2]			, item[n].e('p').text)
			self.assertEqual(URL_BASE + i[3], item[n].e('.username-wrapper a').get_attribute('href'))
		
		# TODO LATER
		# - representing photo
	
	@url('/collections/slideshow/id/' + KEY_COLLECTION)
	def test_slideshow(self):
		self.assertTitle('HistoryPin | Collection | Test Collection for automated test')
		self.assertEqual('Test Collection for automated test\nExit Slideshow'										, self.e('#slide-content p').text)
		self.assertEqual(URL_BASE + '/collections/view/id/22782015/title/Test%20Collection%20for%20automated%20test', self.e('#slide-content a').get_attribute('href'))
		
		# TODO LATER
		# 
		# 
		# 
	