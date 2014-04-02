# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Hertfordshire(HPTestCase, Attach):
	
	
	PROJECT_URL = '/project/55-hertfordshire-on-the-map'
	ATTACH_TABS = [
		'%s/attach%s/map/index/'	% (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_slideshow	= Attach.attach_tab_slideshow
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Hertfordshire on the Map | Home')
		
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Hertfordshire on the Map', site_cnt.e('h1').text)
		self.assertIn(u'Hertfordshire’s past is one of farms, market gardens and small towns.', site_cnt.e('.main_description').text)
		
		self.assertEqual('%s/attach%s/map/index/' % (URL_BASE, self.PROJECT_URL), site_cnt.e('#embed-frame').get_attribute('src'))
		
		upload_button = site_cnt.e('.contribute_wrap a')
		self.assertEqual('%s%s/upload/' % (URL_BASE, self.PROJECT_URL)	, upload_button.get_attribute('href'))
		self.assertEqual('Pin your memories'							, upload_button.e('span').text)
		
		touts_items = [
			[u"Explore Herts' landscapes"	, "%s#!map/index/#!/geo:51.809782,-0.237674/zoom:10/map-type:hybrid/"	% self.PROJECT_URL, 'Use satellite view to locate your histories'	, 'tout1_image'],
			['Can you help?'				, '%s/upload/' % self.PROJECT_URL, 'What was it like to live, work or play here?', 'tout2_image'],
		]
		
		h3s_links	= site_cnt.es('.w23 .inner h3 a')
		paragraphs	= site_cnt.es('.w23 .inner p')
		imgs_links	= site_cnt.es('.w23 .inner p + a')
		imgs		= site_cnt.es('.w23 .inner img')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(i[0], h3s_links[n].text)
			self.assertEqual('http://www.historypin.com' + i[1], h3s_links[n].get_attribute('href'))
			self.assertEqual('http://www.historypin.com' + i[1], imgs_links[n].get_attribute('href'))
			self.assertIn(i[2], paragraphs[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/55/dim/270x270/type/' + i[3] + '/crop/1/', imgs[n].get_attribute('src'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('pieces of content added so far', activity.e('h6').text)
		# TODO add assertion for activity when there is one
		
		icon_tout1	= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://heritagehub.herts.ac.uk/partners-in-history.htm', icon_tout1.get_attribute('href'))
		self.assertEqual('Find out more about this project'	, icon_tout1.text)
		self.assertIn('ss-icon'								, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'							, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2	= site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://heritagehub.herts.ac.uk/news-and-events.htm', icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news'	, icon_tout2.text)
		self.assertIn('ss-icon'					, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper'			, icon_tout2.e('span').get_attribute('class'))
		
		icon_tout3	= site_cnt.e('#icon-tout-2 a')
		
		self.assertEqual('http://www.hertsmemories.org.uk/'						, icon_tout3.get_attribute('href'))
		self.assertEqual("Connect with Hertfordshire's online community archive", icon_tout3.text)
		self.assertIn('ss-icon'		, icon_tout3.e('span').get_attribute('class'))
		self.assertIn('ss-desktop'	, icon_tout3.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		self.assertEqual('Image credit: Hertfordshire Studies and Local Archives', site_cnt.e('.image-credits').text)
		
		partnership		= self.e('.partnership')
		partners		= partnership.es('a')
		
		partners_items	= ['http://heritagehub.herts.ac.uk/', 'http://www.hertsdirect.org/services/leisculture/heritage1/hals/', 'http://www.ahrc.ac.uk/']
		for n in range(len(partners_items)): self.assertEqual(partners_items[n], partners[n].get_attribute('href'))
		
		
		
		
		
		