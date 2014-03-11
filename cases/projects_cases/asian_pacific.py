# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_AsianPacific(HPTestCase, Attach):
	
	PROJECT_URL = '/project/51-east-at-main-street'
	
	ATTACH_TABS = [
		'%s/photos/index/'		% PROJECT_URL,
		'%s/photos/gallery/'	% PROJECT_URL,
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('East at Main Street | Home')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('East at Main Street', site_cnt.e('h1').text)
		self.assertIn('Few sites associated with Asian Pacific Islander (API) American history and culture have been recognized as landmarks', site_cnt.e('.main_description').text)
		
		self.assertEqual('Pin your memories', site_cnt.e('.right.next-button span').text)
		self.assertEqual(URL_BASE + self.PROJECT_URL + '/upload/', site_cnt.e('.right.next-button').get_attribute('href'))
		
		self.assertEqual(URL_BASE + '/attach%s/map/index/' % self.PROJECT_URL, self.e('#embed-frame').get_attribute('src'))
		
		# TODO Add links when they're provided
		
		tout_items = [
			['How to participate'	, 'Learn how to share information and memories about places that matter.', 'tout1_image'],
			['Explore API America'	, 'Visit API sites through tours and collections posted by our partners.', 'tout2_image'],
		]
		
		h3s			= self.es('.w23 .inner h3')
		paragraphs	= self.es('.w23 .inner p')
		imgs		= self.es('.w23 .inner img')
		
		# TODO test activity feed when there is content in the project
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], paragraphs[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/51/dim/287x331/type/' + i[2] + '/crop/1/', imgs[n].get_attribute('src'))
		
		link = 'http://apiahipmappingproject.blogspot.com'
		
		icon_tout_items = [
			['%s/2014/03/welcome-to-apia-mapping-project.html'	% link, 'Find out more about this project', 'ss-icon ss-users'],
			['%s/'	% link				, 'Read the latest news on our blog', 'ss-icon ss-newspaper'],
			['http://www.apiahip.org/'	, 'Learn more about APIAHiP'		, 'ss-icon ss-desktop'],
		]
		
		links = self.es('.w3 .inn a')
		icons = self.es('.w3 .inn a span')
		
		for n in range(len(icon_tout_items)):
			i = icon_tout_items[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
			self.assertEqual(i[2], icons[n].get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		self.assertEqual('Images courtesy Asian & Pacific Islander Americans in Historic Preservation', self.e('.image-credits').text)
		
		items		= ['http://www.nps.gov/AAPI/', 'http://ncptt.nps.gov/', 'http://www.preservationnation.org/']
		
		supporters	= self.e('.sup-by')
		links		= supporters.es('a')
		
		for n in range(len(items)): self.assertEqual(items[n], links[n].get_attribute('href'))
		
