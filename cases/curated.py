# -*- coding: utf-8 -*-

from base import *

class Curated(HPTestCase):
	@url('/curated/')
	def test_index(self):
		self.assertTitle('Historypin | Tours & Collections')
		
		main = [
			['What are Collections?', 'Collections bring together content around a particular topic or theme. You can explore the Collections or create a Collection of your own.', '/collections/all', '/resources/images/collections_page_image.jpg'],
			['What are Tours?', 'Tours lead you step-by-step through a series of pieces of content, telling a story, exploring a place or walking through time. Take one of the Tours below or put your own together, using any content on Historypin.', '/tours/all', '/resources/images/tour-homepage-index.png']
		]
		
		h2s			= self.es('#page-index h2')
		paragraphs	= self.es('.w2 h2 ~ p')
		links		= self.es('.w2 h2 ~ a')
		images		= self.es('.w2 h2 ~ a > img')
		
		for n in range(len(main)):
			i = main[n]
			self.assertEqual(i[0]			, h2s[n].text)
			self.assertEqual(i[1]			, paragraphs[n].text)
			self.assertEqual(URL_BASE + i[2], links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + i[3], images[n].get_attribute('src'))
		
		h3s = self.es('#page-index .section.col.w2 .inner h3')
		self.assertEqual('Featured Collections'	, h3s[0].text)
		self.assertEqual('Featured Tours'		, h3s[1].text)
		
		cnt	= self.es('#page-index .section.col.w2 .inner #photo_list_content .list li:nth-of-type(1)')
		
		self.assertIsInstance(cnt[0].e('a')	, WebElement)
		self.assertIsInstance(cnt[0].e('img')	, WebElement)
		self.assertIsInstance(cnt[0].e('p')	, WebElement)
		
		self.assertIn('collection-icon'	, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-pictures'		, cnt[0].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'			, cnt[0].e('a span').get_attribute('class'))
		
		self.assertIsInstance(cnt[1].e('a')	, WebElement)
		self.assertIsInstance(cnt[1].e('img')	, WebElement)
		self.assertIsInstance(cnt[1].e('p')	, WebElement)
		
		self.assertIn('tour-icon'	, cnt[1].e('a span').get_attribute('class'))
		
		self.assertIn('ss-hiker'	, cnt[1].e('a span').get_attribute('class'))
		self.assertIn('ss-icon'		, cnt[1].e('a span').get_attribute('class'))
		
		button_text = self.es('.inner a.button.left span')
		self.assertEqual('Make your own Collection'	, button_text[0].text)
		self.assertEqual('See all Collections'		, button_text[1].text)
		self.assertEqual('Make your own Tour'		, button_text[2].text)
		self.assertEqual('See all Tours'			, button_text[3].text)
		
		button_links = self.es('.inner a.button.left')
		self.assertEqual('%s/collections/add'	% URL_BASE, button_links[0].get_attribute('href'))
		self.assertEqual('%s/collections/all/'	% URL_BASE, button_links[1].get_attribute('href'))
		self.assertEqual('%s/tours/add'			% URL_BASE, button_links[2].get_attribute('href'))
		self.assertEqual('%s/tours/all/'		% URL_BASE, button_links[3].get_attribute('href'))
		