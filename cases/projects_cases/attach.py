# -*- coding: utf-8 -*-

from base import *

class Attach():
	
	def attach_tabs(self):
		self.go('/attach' + self.PROJECT_URL + '/map/')
		
		embed_tabs = self.e('#embed_tabs')
		tabs_links = embed_tabs.es('li a')
		
		for t in range(len(self.ATTACH_TABS)):
			self.assertIsInstance(tabs_links[t], WebElement)
	
	def attach_tab_map(self):
		self.go('/attach' + self.PROJECT_URL + '/map/')
		
		sleep(2)
		
		# no way to do this in selenium as the counter element is hidden
		self.browser.execute_script("ms = $('.hp-marker.hp-marker-cluster'); for(i in ms){ m = ms[i]; if($('.hp-marker-count', m).text() < 100 ){ m.click(); break; } }")
		
		sleep(5)
		
		cluster = self.e('#galleryInfoWindow_contents li:nth-of-type(1)')
		
		self.assertIsInstance(cluster.e('.hp-info-gallery-pin img'), WebElement)
		self.assertIsInstance(cluster.e('.info h6 a'), WebElement)
		self.assertIsInstance(cluster.e('.info p'), WebElement)
	
	def attach_tab_gallery(self):
		self.go('/attach' + self.PROJECT_URL + '/photos/gallery/')
		
		filter_bar = self.e('.list-filter')
		
		self.assertEqual('Filter by:', filter_bar.e('p strong').text)
		
		input_recent = filter_bar.e('#date_upload')
		
		self.assertIsInstance(input_recent, WebElement)
		self.assertTrue(input_recent.is_selected())
		
		sleep(3)
		picture = self.e('.gallery:nth-of-type(1) .picture:nth-of-type(1)')
		self.assertIsInstance(picture.e('img'), WebElement)
		self.hover(picture)
		
		overlay = picture.e('.overlay')
		
		self.assertIsInstance(overlay.e('h3'), WebElement)
		self.assertIsInstance(overlay.e('p'), WebElement)
		self.assertIsInstance(overlay.e('p a'), WebElement)
		self.assertIsInstance(overlay.e('p span'), WebElement)
		
		input_popular = filter_bar.e('#view_count')
		self.assertIsInstance(input_popular, WebElement)
		
		input_popular.click()
		self.assertFalse(input_recent.is_selected())
		
		sleep(3)
		picture = self.e('.gallery:nth-of-type(1) .picture:nth-of-type(1)')
		self.assertIsInstance(picture.e('img'), WebElement)
		self.hover(picture)
		
		overlay = picture.e('.overlay')
		
		self.assertIsInstance(overlay.e('h3'), WebElement)
		self.assertIsInstance(overlay.e('p'), WebElement)
		self.assertIsInstance(overlay.e('p a'), WebElement)
		self.assertIsInstance(overlay.e('p span'), WebElement)
		
	def attach_tab_collections(self):
		self.go('/attach' + self.PROJECT_URL + '/collections/all/')
		
		item = self.e('#list li:nth-of-type(1) > a')
		
		self.assertIsInstance(item, WebElement)
		self.assertIsInstance(item.e('img'), WebElement)
		
		self.assertIn('collection-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'			, item.e('span').get_attribute('class'))
		self.assertIn('ss-pictures'		, item.e('span').get_attribute('class'))
		
		paragraph = self.e('#list li:nth-of-type(1) p')
		self.assertIsInstance(paragraph.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(paragraph.e('a:nth-of-type(2)'), WebElement)
	
	def attach_tab_tours(self):
		self.go('/attach' + self.PROJECT_URL + '/tours/all/')
		
		
		item = self.e('#list li:nth-of-type(1) > a')
		
		self.assertIsInstance(item, WebElement)
		self.assertIsInstance(item.e('img'), WebElement)
		
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-hiker'	, item.e('span').get_attribute('class'))
		
		paragraph = self.e('#list li:nth-of-type(1) p')
		self.assertIsInstance(paragraph.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(paragraph.e('a:nth-of-type(2)'), WebElement)
	
	def attach_tab_slideshow(self):
		self.go('/attach' + self.PROJECT_URL + '/photos/slideshow/')
		
		self.assertIsInstance(self.e('#prevthumb img')	, WebElement)
		self.assertIsInstance(self.e('#nextthumb img')	, WebElement)
		self.assertIsInstance(self.e('#slidecounter')	, WebElement)
		self.assertIsInstance(self.e('#slidecaption')	, WebElement)
		self.assertIsInstance(self.e('#navigation')		, WebElement)
	
	def attach_tab_comments(self):
		self.go('/attach' + self.PROJECT_URL + '/#|photos/stories/')
		# TODO fix this not find the element
		sleep(10)
		comment = self.e('.stories li:nth-of-type(1)')
		
		self.assertIsInstance(comment.e('.user'), WebElement)
		self.assertIsInstance(comment.e('.story a'), WebElement)
		self.assertIsInstance(comment.e('.story p'), WebElement)
		self.assertIsInstance(comment.e('.story .details a'), WebElement)
