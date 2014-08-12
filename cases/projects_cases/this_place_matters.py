# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_This_Place_Matters(HPTestCase, Attach):
	
	PROJECT_URL = '/project/61-this-place-matters'
	
	ATTACH_TABS = [
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/mysteries/index/'	% (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_map		= Attach.attach_tab_map
	test_tab_mysteries	= Attach.attach_tab_mysteries
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('This Place Matters Australia | Home')
		
		self.assertIsInstance(self.e('.banner.small'), WebElement)
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('This Place Matters Australia', site_cnt.e('h1').text)
		self.assertIn('Share your stories, photos, videos and audio clips and help the National Trust celebrate the places that matter.', site_cnt.e('.main_description').text)
		
		pin_button = site_cnt.e('.right.next-button')
		self.assertEqual('Pin your places', pin_button.e('span').text)
		self.assertEqual('%s%s/upload/' % (URL_BASE, self.PROJECT_URL), pin_button.get_attribute('href'))
		
		
		tout_items = [
			['How to pin'			, 'http://blog.historypin.com/?p=4954'									, 'tout1_image', 'Find out how to upload'],
			['Mysterious Matters'	, 'http://www.historypin.com%s/#!mysteries/index/' % self.PROJECT_URL	, 'tout2_image', 'Help us solve the mystery'],
		]
		
		h3s			= site_cnt.es('.tout.w2 h3')
		images		= site_cnt.es('.tout.w2 img')
		paragraphs	= site_cnt.es('.tout.w2 p')
		h3s_link	= site_cnt.es('.tout.w2 h3 a')
		images_link	= site_cnt.es('.tout.w2 p + a')
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], h3s_link[n].get_attribute('href'))
			self.assertEqual(i[1], images_link[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/projects/img/pid/61/dim/270x309/type/' + i[2] + '/crop/1/', images[n].get_attribute('src'))
			self.assertIn(i[3], paragraphs[n].text)
		
		activity = site_cnt.e('#activity')
		
		li_first = activity.e('li:first-of-type')
		
		self.assertIsInstance(li_first.e('a')		, WebElement)
		self.assertIsInstance(li_first.e('a img')	, WebElement)
		self.assertIsInstance(li_first.e('p')		, WebElement)
		self.assertIsInstance(li_first.e('p a')		, WebElement)
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		icon_tout1				= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://blog.historypin.com/wp-content/uploads/2014/07/This-Place-Matters-Australia-User-Guide_web.pdf', icon_tout1.get_attribute('href'))
		self.assertEqual('How you can share (pdf guide)', icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://www.nationaltrust.org.au/', icon_tout2.get_attribute('href'))
		self.assertEqual('Find out about the National Trust', icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-desktop'	, icon_tout2.e('span').get_attribute('class'))
		
		icon_tout3 = site_cnt.e('#icon-tout-2 a')
		
		self.assertEqual('mailto:placesmatter@nattrust.com.au', icon_tout3.get_attribute('href'))
		self.assertEqual('Ask a question'			, icon_tout3.text)
		self.assertIn('ss-icon'	, icon_tout3.e('span').get_attribute('class'))
		self.assertIn('ss-chat'	, icon_tout3.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		self.assertEqual('Image credit: Luna Park, Melbourne', self.e('.image-credits').text)
		
		partners = self.e('.partnership')
		texts	 = partners.es('span')
		links	 = partners.es('a')
		
		partners_items = [
			['Brought to you by', 'http://www.nationaltrust.org.au/', 'Australian Government'],
			['Supported by'	, 'http://www.environment.gov.au/', 'National trust'],
		]
		
		for n in range(len(partners_items)):
			i = partners_items[n]
			self.assertEqual(i[0], texts[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
			
