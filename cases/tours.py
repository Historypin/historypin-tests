# -*- coding: utf-8 -*-

from base import *

class Tours(HPTestCase):
	@url('/tours/')
	def test_index(self):
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
		# assertIsInstance for one element(check for link and img src text and channel link )
		self.assertIn('tour-icon'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-hiker'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'		, cnt[0].e('a span').get_attribute('class'))
		
	@url('/tours/all')
	@unittest.skip('TODO')
	def test_all(self):
		# assert title
		# assert main img
		# assert heading
		# assert make your own tour button 
		# assert all tours and return ..link and text
		# assertIsInstance for one element(check for link and img src text and channel link )
		# assert next link and text
		pass
	
	@unittest.skip('TODO')
	@url('/tours/view/id/' + KEY_TOUR)
	def test_view(self):
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
		# TODO LATER
		# - representing photo
		pass
	
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
	