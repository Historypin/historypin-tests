# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Lincoln(HPTestCase, Attach):
	
	PROJECT_URL = '/project/57-remembering-lincoln'
	ATTACH_TABS = [
		'{0}/attach{1}/map/index/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/gallery/'	.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/slideshow/'		.format(URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_slideshow	= Attach.attach_tab_slideshow
	test_tab_map		= Attach.attach_tab_map
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Remembering Lincoln | Home')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Remembering Lincoln', site_cnt.e('h1').text)
		self.assertIn(u'Remembering Lincoln is a digital project to commemorate the 150th anniversary of Abraham Lincoln’s assassination.', site_cnt.e('.main_description').text)
		
		self.assertEqual('{0}/attach{1}/map/index/'.format(URL_BASE, self.PROJECT_URL), site_cnt.e('#embed-frame').get_attribute('src'))
		
		button_pin = site_cnt.e('.button.pin')
		self.assertEqual('Pin your items here', button_pin.e('span').text)
		self.assertEqual('{0}{1}/upload/'.format(URL_BASE, self.PROJECT_URL), button_pin.get_attribute('href'))
		
		touts_items = [
			['How to participate'		, 'http://www.fords.org/remembering-lincoln/seeking-contributions', u'Learn what kinds of items we’re seeking for the project.', 'tout1_image'],
			['About Remembering Lincoln', 'http://www.fords.org/remembering-lincoln', 'Learn more about the project.'							, 'tout2_image'],
		]
		
		h3s			= site_cnt.es('.w23 .inner h3')
		h3s_link	= site_cnt.es('.w23 .inner h3 a')
		images		= site_cnt.es('.w23 .inner img')
		images_link	= site_cnt.es('.w23 .inner p + a')
		paragraphs	= site_cnt.es('.w23 .inner p')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], h3s_link[n].get_attribute('href'))
			self.assertEqual(i[1], images_link[n].get_attribute('href'))
			self.assertEqual(i[2], paragraphs[n].text)
			self.assertEqual('{0}/projects/img/pid/57/dim/270x309/type/{1}/crop/1/'.format(URL_BASE, i[3]), images[n].get_attribute('src'))
		
		# TODO add assertion for the activity feed's first item
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('content, comments, and contributions', activity.e('h6').text)
		
		self.assertEqual('Share:', self.e('.addthis_toolbox h3').text)
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		self.assertEqual("Images courtesy of Ford's Theatre and Library of Congress\nThis project was made possible in part by the Institute of Museum and Library Services, grant number MA-10-13-0274-13", self.e('.image-credits').text)
		
		icon_tout1	= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://blog.fords.org/category/history-museums/remembering-lincoln/', icon_tout1.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'	, icon_tout1.text)
		self.assertIn('ss-icon'								, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper'						, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2	= site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://www.fords.org/join-our-email-list', icon_tout2.get_attribute('href'))
		self.assertEqual('Join our email list'	, icon_tout2.text)
		self.assertIn('ss-icon'					, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-mail'					, icon_tout2.e('span').get_attribute('class'))
		
		icon_tout3	= site_cnt.e('#icon-tout-2 a')
		
		self.assertEqual('http://www.fords.org/remembering-lincoln/historypin-image-credits', icon_tout3.get_attribute('href'))
		self.assertEqual("More about the images on this page", icon_tout3.text)
		self.assertIn('ss-icon'		, icon_tout3.e('span').get_attribute('class'))
		self.assertIn('ss-picture'	, icon_tout3.e('span').get_attribute('class'))
		
		partnership		= self.e('.partnership')
		partners		= partnership.es('a')
		
		partners_items	= ['http://www.fords.org/', 'http://www.imls.gov/']
		for n in range(len(partners_items)): self.assertEqual(partners_items[n], partners[n].get_attribute('href'))
	