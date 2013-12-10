# -*- coding: utf-8 -*-

from base import *

class Project_Sourdough(HPTestCase):
	
	PROJECT_URL = '/project/43-sourdough-and-rye'
	
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
		# TODO
		# assert title
		# assert nav
		# assert text
		# assert image
	
	def test_explore(self):
		self.go(self.PROJECT_URL + '/explore#|map/')
		# TODO
		# assert title
		# assert embed frame
		
	def test_events(self):
		self.go(self.PROJECT_URL + '/events/')
		# TODO
		# assert title
		# assert links images and paragraphs
	