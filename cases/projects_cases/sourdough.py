# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Sourdough(HPTestCase, Attach):
	
	PROJECT_URL = '/project/43-sourdough-and-rye'
	
	ATTACH_TABS = [
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/tours/all/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/collections/all/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/slideshow/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/list/'		% (URL_BASE, PROJECT_URL)
	]
	
	test_attach_tabs		= Attach.attach_tabs
	test_tab_map			= Attach.attach_tab_map
	test_tab_gallery		= Attach.attach_tab_gallery
	test_tab_tours			= Attach.attach_tab_tours
	test_tab_collections	= Attach.attach_tab_collections
	test_tab_slideshow		= Attach.attach_tab_slideshow
	test_tab_list			= Attach.attach_tab_list
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Sourdough and Rye | Home')
		self.assertEqual('%s/projects/img/dim/1030x250/crop/1/image_id/150' % URL_BASE, self.e('#banner_images img').get_attribute('src'))
		
		site_cnt = self.e('#site-content')
		about_link = site_cnt.e('.w23 a')
		
		self.assertEqual('%s%s/about' % (URL_BASE, self.PROJECT_URL), about_link.get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		
		self.assertIsInstance(activity.e('h1')		, WebElement)
		self.assertEqual('pieces of content added so far'	, activity.e('p').text)
		
		item_first = activity.es('.activity li:first-of-type a')
		
		self.assertIsInstance(item_first[0], WebElement)
		self.assertIsInstance(item_first[0].e('img'), WebElement)
		self.assertIsInstance(item_first[1], WebElement)
		self.assertIsInstance(item_first[2], WebElement)
		
		items = [
			['/explore'	, 'sr-explore.jpg'],
			['/upload'	, 'sr-contribute.jpg'],
			['/events'	, 'sr-events.jpg'],
		]
		
		image_links	= site_cnt.e('.image-links')
		links		= image_links.es('a')
		images		= image_links.es('img')
		
		for n in range(len(items)):
			i = items[n]
			self.assertEqual(URL_BASE + self.PROJECT_URL + i[0], links[n].get_attribute('href'))
			self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/sandr/' + i[1], images[n].get_attribute('src'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		self.assertEqual('Images provided by The Magnes Collection of Jewish Art and Life', site_cnt.e('.image-credit').text)
		self.assertEqual('http://www.magnes.org/', site_cnt.e('.image-credit a').get_attribute('href'))
		
		supported = self.e('.additional-footer')
		self.assertEqual('Supported by:', supported.e('h5').text)
		
		supported_items = [
			['http://www.jewishfed.org/', 'btm-logo1.jpg'],
			['http://www.ldgfund.org/'	, 'btm-logo2.jpg'],
		]
		
		supported_links	= supported.es('a')
		supported_imgs	= supported.es('img')
		
		for n in range(len(supported_items)):
			i = supported_items[n]
			self.assertEqual(i[0], supported_links[n].get_attribute('href'))
			self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/sandr/' + i[1], supported_imgs[n].get_attribute('src'))
		
	
	def test_about(self):
		self.go(self.PROJECT_URL + '/about/')
		
		self.assertTitle('Sourdough and Rye')
		
		nav_items = [
			['%s%s/'		% (URL_BASE, self.PROJECT_URL), 'Home'],
			['%s%s/about'	% (URL_BASE, self.PROJECT_URL), 'About'],
			['%s%s/explore'	% (URL_BASE, self.PROJECT_URL), 'Explore'],
			['%s%s/upload'	% (URL_BASE, self.PROJECT_URL), 'Contribute'],
			['%s%s/events'	% (URL_BASE, self.PROJECT_URL), 'Events'],
			['http://sourdoughandryehistory.org/'			, 'Blog'],
		]
		
		site_cnt = self.e('#site-content')
		local_nav = site_cnt.e('.localnav')
		nav_links = local_nav.es('a')
		
		for n in range(len(nav_items)):
			i = nav_items[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
		
		self.assertIn('Like the great delis that once populated the Fillmore District', site_cnt.e('.about-inner p').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/sandr/bread.jpg', site_cnt.e('#about-video').get_attribute('src'))
	
	def test_explore(self):
		self.go(self.PROJECT_URL + '/explore#|map/')
		
		self.assertTitle('Sourdough and Rye')
		self.assertEqual('%s/attach%s/map/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
	
	def test_events(self):
		self.go(self.PROJECT_URL + '/events/')
		
		site_cnt	= self.e('#site-content')
		touts		= site_cnt.e('.image-links')
		img_links	= touts.es('.item > a')
		imgs		= touts.es('.item > a img')
		h3s_links	= touts.es('h3 a')
		paragraphs	= touts.es('p')
		
		touts_items = [
			['/#', 'tout1_image', 'Upcoming events'		, 'More information coming soon!'],
			['/#', 'tout2_image', 'Past events'			, 'More information coming soon!'],
			['/#', 'tout3_image', 'Run your own event'	, 'More information coming soon!'],
		]
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(URL_BASE + self.PROJECT_URL + '/events' + i[0], img_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + self.PROJECT_URL + '/events' + i[0], h3s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/projects/img/pid/43/dim/307x265/type/' + i[1] + '/crop/1/', imgs[n].get_attribute('src'))
			self.assertEqual(i[2], h3s_links[n].text)
			self.assertEqual(i[3], paragraphs[n].text)
		
	