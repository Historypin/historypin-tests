# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_YOTB(HPTestCase, Attach):
	
	PROJECT_URL = '/project/22-yearofthebay'
	
	ATTACH_TABS = [
		'{0}/attach{1}/mysteries/index/'.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/map/index/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/gallery/'	.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/tours/all/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/collections/all/'.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/slideshow/'		.format(URL_BASE, PROJECT_URL),
		
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
		self.assertEqual('{0}{1}/upload/'.format(URL_BASE, self.PROJECT_URL), button.get_attribute('href'))
		self.assertEqual('Pin your memories', button.e('span').text)
		
		touts_items = [
			["Tour North Beach in the 70's and 80's", "From the SFPL."						, 'tout1_image', '{0}/project/22-yearofthebay/#!tours/view/id/3959/title/A%20Tour%20of%20North%20Beach%20in%20the%2070%27s%20and%2080%27s'.format(URL_BASE)],
			['Tour the 1906 Earthquake in SF'		, "Before and after the big 1906 quake.", 'tout2_image', '{0}/project/22-yearofthebay/#!tours/view/id/3871/title/1906%20San%20Francisco%20Earthquake%20and%20Fire'.format(URL_BASE)],
		]
		
		h3s		= site_cnt.es('.w2 h3')
		texts	= site_cnt.es('.w2 p')
		images	= site_cnt.es('.w2 img')
		links	= site_cnt.es('.w2 h3 a')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], texts[n].text)
			self.assertEqual('{0}/projects/img/pid/22/dim/271x311/type/{1}/crop/1/'.format(URL_BASE, i[2]), images[n].get_attribute('src'))
			self.assertEqual(i[3], links[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('materials, memories and\ncontributions to mysteries', activity.e('h6').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('p')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		self.assertEqual('{0}/attach{1}/map/index/'.format(URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		icon_tout1	= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://blog.historypin.com/?p=3386'	, icon_tout1.get_attribute('href'))
		self.assertEqual('Find out more about this project'	, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('{0}{1}/behind-the-scenes/'.format(URL_BASE, self.PROJECT_URL), icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'	, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper', icon_tout2.e('span').get_attribute('class'))
		
		icon_tout3 = site_cnt.e('#icon-tout-2 a')
		
		self.assertEqual('http://blog.historypin.com/2014/01/01/how-you-can-participate-in-year-of-the-bay/', icon_tout3.get_attribute('href'))
		self.assertEqual('How-to\'s', icon_tout3.text)
		self.assertIn('ss-icon'		, icon_tout3.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper', icon_tout3.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		self.assertEqual('{0}://wawwd-resources.s3.amazonaws.com/historypin/projects/yotb/partners.png'.format(PROTOCOL), self.e('.partner-logos img').get_attribute('src'))
