# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Yarra(HPTestCase, Attach):
	
	PROJECT_URL = '/project/49-yarra'
	ATTACH_TABS = [
		['%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/gallery/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/list/' % (URL_BASE, PROJECT_URL)],
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_list		= Attach.attach_tab_list
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Yarra Ranges: Changing Places | Home')
		
		self.assertEqual('%s/projects/img/dim/1020x360/crop/1/image_id/177' % URL_BASE	, self.e('#banner_images img').get_attribute('src'))
		self.assertIn('Do you have a photograph of a streetscape, shop or an event'		, self.e('.main_description').text)
		
		self.assertEqual('%s/attach%s/map/index/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		upload_button = self.e('.button.right')
		self.assertEqual('%s%s/upload/' % (URL_BASE, self.PROJECT_URL), upload_button.get_attribute('href'))
		self.assertEqual('Pin your memories', upload_button.e('span').text)
		
		tout_yarra_link = 'http://www.yarraranges.vic.gov.au/ach'
		
		touts_items = [
			['/Regional_Museum/Whats_On_The_Museum'									, 'Pin It In person'			, 'Come to a workshop at Yarra Ranges Regional'	, 'tout1_image'],
			['/Whats_On/Changing_Places_The_Evolution_of_Yarra_Ranges_Main_Streets'	, 'Changing Places exhibition'	, 'Discover how the main streets and shopping'	, 'tout2_image'],
		]
		
		h3s_links	= self.es('.w23 .inner h3 a')
		paragraphs	= self.es('.w23 .inner p')
		imgs_links	= self.es('.w23 .inner p + a')
		imgs		= self.es('.w23 .inner a img')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(tout_yarra_link + i[0], h3s_links[n].get_attribute('href'))
			self.assertEqual(tout_yarra_link + i[0], imgs_links[n].get_attribute('href'))
			self.assertEqual(i[1], h3s_links[n].text)
			self.assertIn(i[2], paragraphs[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/49/dim/287x300/type/' + i[3] + '/crop/1/', imgs[n].get_attribute('src'))
		
		activity = self.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('pieces of content added so far', activity.e('h6').text)
		
		item_feed = self.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		self.assertIsInstance(item_feed.e('p')	, WebElement)
		
		
		