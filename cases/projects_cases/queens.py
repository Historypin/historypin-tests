# -*- coding: utf-8 -*-

from base import *

class Project_Queens(HPTestCase):
	
	PROJECT_URL = '/project/40-queens/'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Queens: Neighborhood tales | Home')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Queens: Neighborhood Stories', site_cnt.e('h1').text)
		self.assertIn('Queens is the most diverse county in the U.S., made up of many neighborhoods', site_cnt.e('.main_description').text)
		
		tout_items = [
			['Pin your memories'	, 'tout1_image', 'What makes your neighborhood special?'					, '/?p=4021'],
			['Get involved'			, 'tout2_image', 'Find out how you can get your neighborhood involved'		, '/?p=3765'],
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
			self.assertEqual('http://blog.historypin.com' + i[3], h3s_link[n].get_attribute('href'))
			self.assertEqual('http://blog.historypin.com' + i[3], images_link[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		li_first = activity.e('li:first-of-type')
		
		self.assertIsInstance(li_first.e('a')		, WebElement)
		self.assertIsInstance(li_first.e('a img')	, WebElement)
		self.assertIsInstance(li_first.e('p')		, WebElement)
		self.assertIsInstance(li_first.e('p a')		, WebElement)
		