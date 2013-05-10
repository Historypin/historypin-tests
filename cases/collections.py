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
	
	@url('/collections/view/id/6935421/title/Some%20of%20the%20Best')
	def test_view(self):
		self.assertTitle('Historypin | Collection - Some of the Best')
		
		self.assertEqual(URL_BASE + '/services/thumb/phid/6604908/dim/451x302/crop/1/'	, self.e('img.index').get_attribute('src'))
		self.assertEqual('Some of the Best'												, self.e('.info h2').text)
		
		paragraphs = self.es('.info p')
		self.assertEqual('A selection of photos from our Collection.'	, paragraphs[0].text)
		self.assertEqual('Created by Missouri History Museum'			, paragraphs[1].text)
		self.assertEqual(URL_BASE + '/channels/view/6573747'			, paragraphs[1].e('a').get_attribute('href'))
		
		button = self.e('.info ~ a')
		self.assertEqual(URL_BASE + '/collections/slideshow/id/6935421/', button.get_attribute('href'))
		self.assertEqual('Slide Show'									, button.text)
		
		collection_view = [
			['/map/#!/geo:38.638601,-90.286128/zoom:15/dialog:6604908/tab:details/', '/services/thumb/phid/6604908/dim/195x150/crop/1/', '1897, from Missouri History Museum', '/channels/view/6573747'],
			['/map/#!/geo:38.643055,-90.18634/zoom:15/dialog:6623055/tab:details/', '/services/thumb/phid/6623055/dim/195x150/crop/1/', '1854, from Missouri History Museum', '/channels/view/6573747'],
			['/map/#!/geo:38.627384,-90.187917/zoom:15/dialog:6612414/tab:details/', '/services/thumb/phid/6612414/dim/195x150/crop/1/', '1848, from Missouri History Museum', '/channels/view/6573747'],
			['/map/#!/geo:38.626224,-90.189725/zoom:15/dialog:6619312/tab:details/', '/services/thumb/phid/6619312/dim/195x150/crop/1/', '1877, from Missouri History Museum', '/channels/view/6573747'],
			['/map/#!/geo:38.612449,-90.196964/zoom:15/dialog:6605749/tab:details/', '/services/thumb/phid/6605749/dim/195x150/crop/1/', '1910, from Missouri History Museum', '/channels/view/6573747'],
		]
		
		item = self.es('#list_view .list li')
		for n in range(len(collection_view)):
			i = collection_view[n]
		self.assertEqual(URL_BASE + i[0]	, item[n].e('a.link-image').get_attribute('href'))
		self.assertEqual(URL_BASE + i[1]	, item[n].e('img').get_attribute('src'))
		self.assertEqual(i[2]				, item[n].e('p').text)
		self.assertEqual(URL_BASE + i[3]	, item[n].e('.username-wrapper a').get_attribute('href'))
		
		# TODO LATER
		# - representing photo
		
	
	@url('/collections/slideshow/id/6935421/')
	def test_slideshow(self):
		# assert text
		# exit slideshow link and text
		# 
		# 
		# 
		# 
		# 
		# 
		# 
		# 
		pass
	