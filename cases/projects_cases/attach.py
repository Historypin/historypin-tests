# -*- coding: utf-8 -*-

from base import *

class Attach():
	ATTACH_URL = '/attach'
	
	def attach_tabs(self):
		self.go(self.ATTACH_URL + self.PROJECT_URL + '/map/')
		
		sleep(3)
		embed_tabs = self.e('#embed_tabs')
		tabs_links = embed_tabs.es('li a')
		
		for t in range(len(self.ATTACH_TABS)):
			self.assertIsInstance(tabs_links[t], WebElement)
	
	def attach_tab_map(self):
		self.go('/attach' + self.PROJECT_URL + '/map/')
		
		sleep(4)
		
		self.assertIsInstance(self.e('#date-selector'), WebElement)
		self.assertIsInstance(self.e('#search-filters'), WebElement)
		
		sleep(5)
		
		# no way to do this in selenium as the counter element is hidden to fix this
		self.browser.execute_script("ms = $('.hp-marker.hp-marker-cluster'); for(i in ms){ m = ms[i]; if($('.hp-marker-count', m).text() < 100 ){ m.click(); break; } }")
		
		cluster = self.e('#galleryInfoWindow_contents li:nth-of-type(1)')
		
		self.assertIsInstance(cluster.e('.hp-info-gallery-pin img'), WebElement)
		self.assertIsInstance(cluster.e('.info h6 a'), WebElement)
		self.assertIsInstance(cluster.e('.info p'), WebElement)
		
		cluster.e('.hp-info-gallery-pin img').click()
		sleep(2)
		self.assertIsInstance(self.e('#info-dialog'), WebElement)
	
	def attach_tab_gallery(self):
		self.go('/attach' + self.PROJECT_URL + '/photos/gallery/')
		
		filter_bar = self.e('.list-filter')
		
		# TODO uncomment
		# self.assertEqual('Filter by:', filter_bar.e('p strong').text)
		
		input_recent = filter_bar.e('#date_upload')
		
		self.assertIsInstance(input_recent, WebElement)
		# TODO imcomment
		# self.assertTrue(input_recent.is_selected())
		
		sleep(5)
		picture = self.e('.gallery:nth-of-type(1) li:nth-of-type(1)')
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
		# TODO ucomment
		# self.assertFalse(input_popular.is_selected())
		
		sleep(3)
		picture = self.e('.gallery:nth-of-type(1) li:nth-of-type(1)')
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
	
	def attach_tab_tours_empty(self):
		self.go('/attach' + self.PROJECT_URL + '/tours/all/')
		
		h3 = self.e('#page-index h3')
		
		self.assertEqual(self.project_name + " hasn't yet published any Tours.", h3.text)
	
	def attach_tab_collections_empty(self):
		self.go('/attach' + self.PROJECT_URL + '/collections/all/')
		
		h3 = self.e('#page-index h3')
		
		self.assertEqual(self.project_name + " hasn't yet published any Collections.", h3.text)
	
	def attach_tab_slideshow(self):
		self.go('/attach' + self.PROJECT_URL + '/photos/slideshow/')
		
		self.assertIsInstance(self.e('#prevthumb img')	, WebElement)
		self.assertIsInstance(self.e('#nextthumb img')	, WebElement)
		self.assertIsInstance(self.e('#slidecounter')	, WebElement)
		self.assertIsInstance(self.e('#slidecaption')	, WebElement)
		self.assertIsInstance(self.e('#navigation')		, WebElement)
	
	def attach_tab_comments(self):
		self.go('/attach' + self.PROJECT_URL + '/photos/stories/')
		
		comment = self.e('.stories li:nth-of-type(1)')
		
		self.assertIsInstance(comment.e('.user'), WebElement)
		self.assertIsInstance(comment.e('.story a'), WebElement)
		self.assertIsInstance(comment.e('.story p'), WebElement)
		self.assertIsInstance(comment.e('.story .details a'), WebElement)
	
	def attach_tab_list(self):
		self.go('/attach' + self.PROJECT_URL + '/photos/list/')
		
		filter_bar = self.e('.list-filter')
		
		self.assertEqual('Sort by:', filter_bar.e('p strong').text)
		
		input_recent = filter_bar.e('#date_upload')
		
		self.assertIsInstance(input_recent, WebElement)
		self.assertTrue(input_recent.is_selected())
		
		sleep(3)
		picture = self.e('.list:nth-of-type(1) li:nth-of-type(1)')
		self.assertIsInstance(picture.e('a img'), WebElement)
		
		self.assertIsInstance(picture.e('.info-actions a'), WebElement)
		self.assertIsInstance(picture.e('.info h5'), WebElement)
		self.assertIsInstance(picture.e('.info p'), WebElement)
		
		input_popular = filter_bar.e('#view_count')
		self.assertIsInstance(input_popular, WebElement)
		
		input_popular.click()
		self.assertFalse(input_recent.is_selected())
		
		sleep(3)
		picture = self.e('.list:nth-of-type(1) li:nth-of-type(1)')
		self.assertIsInstance(picture.e('a img'), WebElement)
		
		self.assertIsInstance(picture.e('.info-actions a'), WebElement)
		self.assertIsInstance(picture.e('.info h5'), WebElement)
		self.assertIsInstance(picture.e('.info p'), WebElement)
	
	def attach_tab_mysteries(self):
		self.go('/attach' + self.PROJECT_URL + '/mysteries/index/')
		
		statistics = self.e('.statistics')
		mods = statistics.es('.mod label')
		
		self.assertEqual('Total mysteries'		, mods[0].text)
		self.assertEqual('Unsolved mysteries'	, mods[1].text)
		self.assertEqual('Under investigation'	, mods[2].text)
		self.assertEqual('Mysteries solved'		, mods[3].text)
		
		sidebar			= self.e('.sidebar')
		status			= sidebar.e('#status')
		mystery_type	= sidebar.e('#bytype')
		
		self.assertEqual('Show me'	, status.e('h4').text)
		self.assertEqual('Only show', mystery_type.e('h4').text)
		self.assertTrue(status.e('#showme_incomplete').is_selected())
		
		status_labels = ['All mysteries', 'Unsolved mysteries', 'Under investigation', 'Solved mysteries']
		
		labels = status.es('label')
		
		for n in range(len(status_labels)): self.assertEqual(status_labels[n], labels[n].text)
		
		mystery_first = self.e('.attach.mysteries > .list section:nth-of-type(1)')
		self.assertIsInstance(mystery_first.e('h3'), WebElement)
		self.assertIsInstance(mystery_first.e('header a'), WebElement)
		self.assertIsInstance(mystery_first.e('.thumb a img'), WebElement)
		self.assertIsInstance(mystery_first.e('.cnt h4 a'), WebElement)
		self.assertIsInstance(mystery_first.e('.clues h6'), WebElement)
		
		status.e('#showme_all').click()
		sleep(5)
		mystery_first = self.e('.attach.mysteries > .list section:nth-of-type(1)')
		solve_button = mystery_first.e('footer .button')
		
		self.assertEqual('Solve', solve_button.text)
		self.assertIsInstance(solve_button, WebElement)
		
		status.e('#showme_investigation').click()
		sleep(2)
		mystery_first = self.e('.attach.mysteries > .list section:nth-of-type(1)')
		solve_button = mystery_first.e('footer .button')
		
		self.assertEqual('Solve', solve_button.text)
		self.assertIsInstance(solve_button, WebElement)
		
		status.e('#showme_solved').click()
		sleep(4)
		
		mystery_first = self.e('.attach.mysteries > .list section:nth-of-type(1)')
		self.assertFalse(mystery_first.exists('footer .button'))
		
		self.assertEqual('Solved', mystery_first.e('.thumb span').text)
		
		self.assertTrue(mystery_type.e('#bytype_all').is_selected())
		
		type_labels = ['All mystery types', 'Title mysteries', 'Date mysteries', 'Location mysteries', 'Street View mysteries', 'Tag mysteries']
		
		labels = mystery_type.es('label')
		
		for n in range(len(type_labels)): self.assertEqual(type_labels[n], labels[n].text)
		
		