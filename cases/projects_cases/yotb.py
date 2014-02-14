# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_YOTB(HPTestCase, Attach):
	
	PROJECT_URL = '/project/22-yearofthebay'
	
	ATTACH_TABS = [
		'%s/attach%s/mysteries/index/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/tours/all/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/collections/all/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/slideshow/'		% (URL_BASE, PROJECT_URL)
		
	]
	
	test_attach_tabs		= Attach.attach_tabs
	test_tab_mysteries		= Attach.attach_tab_mysteries
	test_tab_map			= Attach.attach_tab_map
	test_tab_gallery		= Attach.attach_tab_gallery
	test_tab_tours			= Attach.attach_tab_tours
	test_tab_collections	= Attach.attach_tab_collections
	test_tab_slideshow		= Attach.attach_tab_slideshow
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Year of the Bay | Home')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Year of the Bay', site_cnt.e('h1').text)
		
		button = site_cnt.e('.big')
		self.assertEqual('%s%s/upload/' % (URL_BASE, self.PROJECT_URL), button.get_attribute('href'))
		self.assertEqual('Pin your memories', button.e('span').text)
		
		touts_items = [
			['Dogpatch Mysteries', 'Read about how you can help us solve Dogpatch-themed mysteries from the SFPL.', 'tout1_image', '01/23/solving-dogpatch-mysteries-in-year-of-the-bay/'],
			['How to Pin a Photo', 'Short video of how to pin a photograph to Year of the Bay.', 'tout2_image', '01/23/solving-dogpatch-mysteries-in-year-of-the-bay/'],
		]
		
		h3s		= site_cnt.es('.w2 h3')
		texts	= site_cnt.es('.w2 p')
		images	= site_cnt.es('.w2 img')
		links	= site_cnt.es('.w2 a')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/22/dim/271x311/type/' + i[2] + '/crop/1/', images[n].get_attribute('src'))
			self.assertEqual('http://blog.historypin.com/2014/' + i[3], links[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('materials, memories and\ncontributions to mysteries', activity.e('h6').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('p')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		self.assertEqual('%s/attach%s/mysteries/index/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		
		icon_tout1	= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://blog.historypin.com/?p=3386'	, icon_tout1.get_attribute('href'))
		self.assertEqual('Find out more about this project'	, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('%s%s/behind-the-scenes/' % (URL_BASE, self.PROJECT_URL), icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'	, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper', icon_tout2.e('span').get_attribute('class'))
		
		icon_tout3 = site_cnt.e('#icon-tout-2 a')
		
		self.assertEqual('https://groups.google.com/forum/#!forum/year-of-the-bay-community', icon_tout3.get_attribute('href'))
		self.assertEqual('Ask us a question', icon_tout3.text)
		self.assertIn('ss-icon'		, icon_tout3.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout3.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/yotb/partners.png', self.e('.partner-logos img').get_attribute('src'))
