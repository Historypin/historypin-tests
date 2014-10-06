# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Sandy(HPTestCase, Attach):
	
	PROJECT_URL = '/project/26-sandy'
	ATTACH_TABS = [
		'{0}/attach{1}/map/index/'			.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/gallery/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/stories/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/slideshow/'	.format (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_comments	= Attach.attach_tab_comments
	test_tab_slideshow	= Attach.attach_tab_slideshow
	
	def __test_icon_touts(self):
		
		site_cnt				= self.e('#site-content')
		
		icon_tout1				= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('{0}/project/26-sandy/pages/donate/'.format(URL_BASE)	, icon_tout1.get_attribute('href'))
		self.assertEqual('Donate to support the rebuild'						, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://blog.historypin.com/category/hurricane-sandy'	, icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'						, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, icon_tout2.e('span').get_attribute('class'))
		
		featured = self.e('.bottom-p')
		self.assertEqual('Featured photos by Sleepness, Rob Ketcherside, Wallyg and Jim Henderson', featured.text)
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
	
	def __test_support(self):
		
		support_cnt = self.e('.support')
		self.assertEqual('With support from:', support_cnt.e('h5').text)
		
		partners = [
			['http://www.google.co.uk/intl/en/about/'	, 'google_logo.jpg'],
			['http://metro.org/'						, 'metropolitan.png'],
			['http://www2.archivists.org/'				, 'saa.png'],
			['http://www.aaslh.org/'					, 'aaslh.png'],
		]
		
		links	= support_cnt.es('li a')
		imgs	= support_cnt.es('li a img')
		
		for n in range(len(partners)):
			i = partners[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual('{0}/resources/images/partners/{1}'.format(URL_BASE, i[1]), imgs[n].get_attribute('src'))
			
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Hurricane Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('{0}{1}/'.format(URL_BASE, self.PROJECT_URL), h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('Hurricane Sandy', tout.e('h2').text)
		self.assertIn('How have communities and neighborhoods in the Caribbean and United States been affected by Sandy?', tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('{0}{1}/upload/'.format(URL_BASE, self.PROJECT_URL), button_upload.get_attribute('href'))
		self.assertEqual('Contribute'										, button_upload.e('span').text)
		
		self.assertEqual('{0}/projects/img/pid/26/type/project_image/dim/648x406/crop/1/'.format(URL_BASE), site_cnt.e('.main-image img').get_attribute('src'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('memories and materials contributed so far', activity.e('h6').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'	, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['During Sandy'	, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
			['After Sandy'	, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
		]
		
		h2s			= projects.es('h2')
		h2s_links	= projects.es('h2 a')
		texts		= projects.es('p')
		img_links	= projects.es('p + a')
		imgs		= projects.es('img')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual('{0}/project/{1}'.format(URL_BASE, i[1]), h2s_links[n].get_attribute('href'))
			self.assertEqual('{0}/project/{1}'.format(URL_BASE, i[1]), img_links[n].get_attribute('href'))
			self.assertEqual(i[2], texts[n].text)
			self.assertEqual('{0}/projects/img/pid/{1}/type/banner,project_image,logo/dim/313x214/crop/1/'.format(URL_BASE, i[3]), imgs[n].get_attribute('src'))
		
		self.assertEqual('{0}/attach{1}/map/index/'.format(URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		self.__test_icon_touts()
		self.__test_support()
	
	@url('/project/26-sandy/pages/donate/')
	def test_donate(self):
		
		self.assertTitle('Hurricane Sandy')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('{0}/project/26-sandy/'.format(URL_BASE)		, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		donation_cnt = site_cnt.e('.cf')
		
		self.assertIn('If you would like to support communities affected by Hurricane Sandy,', donation_cnt.e('p:nth-of-type(1)').text)
		
		button_donate = donation_cnt.e('.center')
		
		self.assertEqual('https://npo.networkforgood.org/Donate/Donate.aspx?npoSubscriptionId=1005594&skinid=107989', button_donate.get_attribute('href'))
		self.assertEqual('Donate to help the rebuild', button_donate.e('span').text)
		
		self.assertEqual('{0}/resources/images/sandy_donate_img.jpg'.format(URL_BASE), donation_cnt.e('img').get_attribute('src'))
		
		self.__test_support()
		
	
