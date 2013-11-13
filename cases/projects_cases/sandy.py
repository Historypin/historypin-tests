# -*- coding: utf-8 -*-

from base import *

class Project_Sandy(HPTestCase):
	
	def __test_icon_touts(self):
		
		site_cnt				= self.e('#site-content')
		
		icon_tout1				= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('%s/project/26-sandy/pages/donate/' % URL_BASE				, icon_tout1.get_attribute('href'))
		self.assertEqual('Donate to support the rebuild'							, icon_tout1.text)
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
			self.assertEqual(URL_BASE + '/resources/images/partners/' + i[1], imgs[n].get_attribute('src'))
			
	
	@url('/project/26-sandy/')
	def test_index(self):
		
		self.assertTitle('Hurricane Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('Hurricane Sandy', tout.e('h2').text)
		self.assertIn('How have communities and neighborhoods in the Caribbean and United States been affected by Sandy?', tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/' % URL_BASE	, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'								, button_upload.e('span').text)
		
		self.assertEqual('%s/projects/img/pid/26/type/project_image/dim/665x406/crop/1/' % URL_BASE, site_cnt.e('.main-image img').get_attribute('src'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('memories and materials contributed so far', activity.e('h6').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'	, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['After Sandy'	, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
			['During Sandy'	, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
		]
		
		h2s			= projects.es('h2')
		h2s_links	= projects.es('h2 a')
		texts		= projects.es('p')
		img_links	= projects.es('p + a')
		imgs		= projects.es('img')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(i[2], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3] + '/type/banner,project_image,logo/dim/313x214/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach/project/26-sandy/map/index/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		self.__test_icon_touts()
		self.__test_support()
	
	@url('/project/27-before-sandy/')
	def test_before_sandy(self):
		
		self.assertTitle('Before Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('Before Sandy'									, tout.e('h2').text)
		self.assertIn('What did neighborhoods look like before Sandy?'	, tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/projects/?subproject=27' % URL_BASE	, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'								, button_upload.e('span').text)
		
		self.assertEqual('%s/projects/img/pid/27/type/project_image/dim/980x411/crop/1/' % URL_BASE, site_cnt.e('.main-image img').get_attribute('src'))
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['After Sandy'		, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
			['During Sandy'		, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
			['Back to homepage'	, '26-sandy/'		, 'See all the materials shared from before, during and after Sandy.'					, '26'],
		]
		
		h2s			= projects.es('h2')
		h2s_links	= projects.es('h2 a')
		texts		= projects.es('p')
		img_links	= projects.es('p + a')
		imgs		= projects.es('img')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(i[2], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3] + '/type/banner,project_image,logo/dim/313x214/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach/project/27-before-sandy/photos/gallery/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		self.__test_icon_touts()
		self.__test_support()
	
	@url('/project/29-during-sandy/')
	def test_during_sandy(self):
		
		self.assertTitle('During Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('During Sandy'																			, tout.e('h2').text)
		self.assertEqual('Memories and materials from when Sandy passed through communities and neighborhoods.'	, tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/projects/?subproject=29' % URL_BASE, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'													, button_upload.e('span').text)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'		, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['After Sandy'		, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
			['Back to homepage'	, '26-sandy/'		, 'See all the materials shared from before, during and after Sandy.'					, '26'],
		]
		
		h2s			= projects.es('h2')
		h2s_links	= projects.es('h2 a')
		texts		= projects.es('p')
		img_links	= projects.es('p + a')
		imgs		= projects.es('img')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(i[2], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3] + '/type/banner,project_image,logo/dim/313x214/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach/project/29-during-sandy/photos/gallery/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		self.__test_icon_touts()
		self.__test_support()
		
	
	@url('/project/28-after-sandy/')
	def test_after_sandy(self):
		
		self.assertTitle('After Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('After Sandy'																, tout.e('h2').text)
		self.assertEqual('Explore how people are starting to rebuild their homes and communities.'	, tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/projects/?subproject=28' % URL_BASE, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'													, button_upload.e('span').text)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'		, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['During Sandy'		, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
			['Back to homepage'	, '26-sandy/'		, 'See all the materials shared from before, during and after Sandy.'					, '26'],
		]
		
		h2s			= projects.es('h2')
		h2s_links	= projects.es('h2 a')
		texts		= projects.es('p')
		img_links	= projects.es('p + a')
		imgs		= projects.es('img')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(i[2], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3] + '/type/banner,project_image,logo/dim/313x214/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach/project/28-after-sandy/photos/gallery/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		self.__test_icon_touts()
		self.__test_support()
		
	
	@url('/project/26-sandy/pages/donate/')
	def test_donate(self):
		
		self.assertTitle('Hurricane Sandy')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		donation_cnt = site_cnt.e('.cf')
		
		self.assertIn('If you would like to support communities affected by Hurricane Sandy,', donation_cnt.e('p:nth-of-type(1)').text)
		
		button_donate = donation_cnt.e('.center')
		
		self.assertEqual('https://npo.networkforgood.org/Donate/Donate.aspx?npoSubscriptionId=1005594&skinid=107989', button_donate.get_attribute('href'))
		self.assertEqual('Donate to help the rebuild', button_donate.e('span').text)
		
		self.assertEqual('%s/resources/images/sandy_donate_img.jpg' % URL_BASE, donation_cnt.e('img').get_attribute('src'))
		
		self.__test_support()
		
	
