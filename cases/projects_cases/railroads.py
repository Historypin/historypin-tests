# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Railroads(HPTestCase, Attach):
	
	PROJECT_URL = '/project/42-railroads'
	project_name = 'railroads'
	
	ATTACH_TABS = [
		['%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/gallery/' % (URL_BASE, PROJECT_URL), '%s/attach%s/tours/all/' % (URL_BASE, PROJECT_URL), '%s/attach%s/collections/all/' % (URL_BASE, PROJECT_URL), '%s/attach%s/slideshow/' % (URL_BASE, PROJECT_URL), '%s/attach%s/mysteries/index/' % (URL_BASE, PROJECT_URL)],
	]
	
	test_attach_tabs			= Attach.attach_tabs
	test_tab_map				= Attach.attach_tab_map
	test_tab_gallery			= Attach.attach_tab_gallery
	test_tab_tours_empty		= Attach.attach_tab_tours_empty
	test_tab_collections_empty	= Attach.attach_tab_collections_empty
	test_tab_slideshow			= Attach.attach_tab_slideshow
	test_tab_mysteries			= Attach.attach_tab_mysteries
	
	def __test_touts(self):
		
		site_cnt				= self.e('#site-content')
		tout_items = [
			['Mysteries'		, 'tout1_image', 'Help solve research questions about photos'	, 'http://www.historypin.com%s/explore/#|mysteries/index/' % self.PROJECT_URL],
			['About the project', 'tout2_image', 'Learn more about the Living with Railroads '	, 'http://blog.historypin.com/?p=3867'],
		]
		
		h3s			= site_cnt.es('.tout.w2 h3')
		images		= site_cnt.es('.tout.w2 img')
		paragraphs	= site_cnt.es('.tout.w2 p')
		h3s_link	= site_cnt.es('.tout.w2 h3 a')
		images_link	= site_cnt.es('.tout.w2 p + a')
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/42/dim/285x275/type/' + i[1] + '/crop/1/', images[n].get_attribute('src'))
			self.assertIn(i[2], paragraphs[n].text)
			self.assertEqual(i[3], h3s_link[n].get_attribute('href'))
			self.assertEqual(i[3], images_link[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		li_first = activity.e('li:first-of-type')
		
		self.assertIsInstance(li_first.e('a')		, WebElement)
		self.assertIsInstance(li_first.e('a img')	, WebElement)
		self.assertIsInstance(li_first.e('p')		, WebElement)
		self.assertIsInstance(li_first.e('p a')		, WebElement)
	
	def __test_icon_touts(self):
		
		site_cnt				= self.e('#site-content')
		
		icon_tout1				= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://blog.historypin.com/category/railroads/'	, icon_tout1.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'					, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://www.stanford.edu/group/spatialhistory/cgi-bin/site/project.php?id=997', icon_tout2.get_attribute('href'))
		self.assertEqual('Find out more about Shaping the West'	, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout2.e('span').get_attribute('class'))
		
		featured = self.e('.photosby')
		self.assertEqual('Photos and maps provided by David Rumsey Map Collection, Collection of Chuck Catania, and Lawrence & Houseworth Collection', featured.text)
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		partner_logo = self.e('.partner-logos')
		self.assertEqual('In partnership with:', partner_logo.e('span').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/yotb/partners.png', partner_logo.e('img').get_attribute('src'))
		
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Railroads | Home')
		self.assertEqual('%s/projects/img/dim/1000x250/crop/1/image_id/142' % URL_BASE, self.e('#banner_images img').get_attribute('src'))
		
		site_cnt = self.e('#site-content')
		self.assertIn('Forged from sweat, steam, and steel, the transcontinental railroads of the 19th century transfixed the American imagination.', site_cnt.e('.main_description').text)
		
		button_items = [
			['/explore/#|map/'	, 'Explore'],
			['/upload/'			, 'Contribute'],
		]
		
		button_class	= site_cnt.e('.buttons')
		button_link		= button_class.es('.big')
		button_text		= button_class.es('span')
		
		for n in range(len(button_items)):
			i = button_items[n]
			self.assertEqual(URL_BASE + self.PROJECT_URL + i[0], button_link[n].get_attribute('href'))
			self.assertEqual(i[1], button_text[n].text)
		
		self.__test_touts()
		self.__test_icon_touts()
		
		
	def test_explore(self):
		self.go(self.PROJECT_URL + '/explore/#|map/')
		
		self.assertTitle('Railroads')
		
		self.assertEqual('%s/attach%s/map/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		self.__test_touts()
		self.__test_icon_touts()
		
