# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Queens(HPTestCase, Attach):
	
	PROJECT_URL = '/project/40-queens'
	project_name = 'queens'
	ATTACH_TABS = [
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/slideshow/'		% (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs			= Attach.attach_tabs
	test_tab_gallery			= Attach.attach_tab_gallery
	test_tab_map				= Attach.attach_tab_map
	test_tab_slideshow			= Attach.attach_tab_slideshow
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Queens: Neighborhood Stories | Home')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Queens: Neighborhood Stories', site_cnt.e('h1').text)
		self.assertIn('Queens is the most diverse county in the U.S., made up of many neighborhoods', site_cnt.e('.main_description').text)
		
		tout_items = [
			['Pin your memories'	, 'tout1_image', 'What makes your neighborhood special?'					, 'http://www.historypin.com%s/upload/' % self.PROJECT_URL],
			['Get involved'			, 'tout2_image', 'Find out how you can get your neighborhood involved'		, 'http://blog.historypin.com/2013/01/29/neighborhood-stories-get-your-community-involved/'],
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
