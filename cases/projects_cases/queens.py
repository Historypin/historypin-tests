# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Queens(HPTestCase, Attach):
	
	PROJECT_URL = '/project/40-queens'
	project_name = 'queens'
	ATTACH_TABS = [
		['%s/attach%s/photos/gallery/' % (URL_BASE, PROJECT_URL), '%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/slideshow/' % (URL_BASE, PROJECT_URL), '%s/attach%s/tours/all/' % (URL_BASE, PROJECT_URL), '%s/attach%s/collections/all/' % (URL_BASE, PROJECT_URL)],
	]
	
	test_attach_tabs			= Attach.attach_tabs
	test_tab_gallery			= Attach.attach_tab_gallery
	test_tab_map				= Attach.attach_tab_map
	test_tab_slideshow			= Attach.attach_tab_slideshow
	test_tab_tours_empty		= Attach.attach_tab_tours_empty
	test_tab_collections_empty	= Attach.attach_tab_collections_empty
	
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Queens: Neighborhood tales | Home')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Queens: Neighborhood Stories', site_cnt.e('h1').text)
		self.assertIn('Queens is the most diverse county in the U.S., made up of many neighborhoods', site_cnt.e('.main_description').text)
		
		# TODO fix link to match the new ID - issue #2883 should be fixed
		
		tout_items = [
			['Pin your memories'	, 'tout1_image', 'What makes your neighborhood special?'					, 'http://www.historypin.com%s/upload/' % self.PROJECT_URL],
			['Get involved'			, 'tout2_image', 'Find out how you can get your neighborhood involved'		, 'http://www.bbc.co.uk/'],
		]
		
		h3s			= site_cnt.es('.tout.w2 h3')
		images		= site_cnt.es('.tout.w2 img')
		paragraphs	= site_cnt.es('.tout.w2 p')
		h3s_link	= site_cnt.es('.tout.w2 h3 a')
		images_link	= site_cnt.es('.tout.w2 p + a')
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/40/dim/276x280/type/' + i[1] + '/crop/1/', images[n].get_attribute('src'))
			self.assertIn(i[2], paragraphs[n].text)
			self.assertEqual(i[3], h3s_link[n].get_attribute('href'))
			self.assertEqual(i[3], images_link[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		li_first = activity.e('li:first-of-type')
		
		self.assertIsInstance(li_first.e('a')		, WebElement)
		self.assertIsInstance(li_first.e('a img')	, WebElement)
		self.assertIsInstance(li_first.e('p')		, WebElement)
		self.assertIsInstance(li_first.e('p a')		, WebElement)
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
