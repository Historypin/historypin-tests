# -*- coding: utf-8 -*-

from base import *

class Curated(HPTestCase):
	@url('/curated/')
	def test_index(self):
		
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
		
		cnt	= self.e('#page-index .section.col.w2 .inner #photo_list_content .list li:nth-of-type(1)')
		self.assertIsInstance(cnt.e('a')	, WebElement)
		self.assertIsInstance(cnt.e('img')	, WebElement)
		self.assertIsInstance(cnt.e('p')	, WebElement)
		
		self.assertIn('collection-icon'	, cnt.e('a span.ss-icon.ss-pictures').get_attribute('class'))
		self.assertIn('ss-pictures'		, cnt.e('a span.ss-icon').get_attribute('class'))
		self.assertIn('ss-icon'			, cnt.e('a span').get_attribute('class'))
		
		# TODO
		# when logged in as admin to check icons for edit delete and publish/unpusblish
		# - tours - to check tour icon
	
		button_text = self.es('.inner a.button.left span')
		self.assertEqual('Make your own Collection'	, button_text[0].text)
		self.assertEqual('See all Collections'		, button_text[1].text)
		self.assertEqual('Make your own Tour'		, button_text[2].text)
		self.assertEqual('See all Tours'			, button_text[3].text)
		
		button_add = self.es('.inner a.button.left:nth-of-type(1)')
		self.assertEqual(URL_BASE + '/collections/add'	, button_add[0].get_attribute('href'))
		self.assertEqual(URL_BASE + '/tours/add'		, button_add[1].get_attribute('href'))
		
		button_all = self.es('.inner a.button.left:nth-of-type(2)')
		self.assertEqual(URL_BASE + '/collections/all/'	, button_all[0].get_attribute('href'))
		self.assertEqual(URL_BASE + '/tours/all/'		, button_all[1].get_attribute('href'))