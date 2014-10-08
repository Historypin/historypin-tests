# -*- coding: utf-8 -*-

from base import *

class Attach():
	ATTACH_URL		= '/attach'
	LOCATION_URL	= ''
	
	def attach_tabs(self):
		self.go('{0}{1}/map/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		sleep(3)
		
		embed_tabs = self.e('#embed_tabs')
		tabs_links = embed_tabs.es('li a')
		
		for t in range(len(self.ATTACH_TABS)):
			self.assertIsInstance(tabs_links[t], WebElement)
	
	def attach_tab_map(self):
		self.go('{0}{1}/map/index/#!{2}'.format(self.ATTACH_URL, self.PROJECT_URL, self.LOCATION_URL))
		
		sleep(3)
		
		self.assertIsInstance(self.e('#date-selector'), WebElement)
		self.assertIsInstance(self.e('#search-filters'), WebElement)
		
		sleep(3)
		
		# no way to do this in selenium as the counter element is hidden to fix this
		self.browser.execute_script("ms = $('.hp-marker.hp-marker-cluster'); for(i in ms){ m = ms[i]; if($('.hp-marker-count', m).text() < 100 || $.address.current_path.zoom >= 21){ m.click(); break; } }")
		
		sleep(5)
		cluster = self.e('#galleryInfoWindow_contents li:nth-of-type(1)')
		
		sleep(5)
		self.assertIsInstance(cluster.e('.hp-info-gallery-pin'), WebElement)
		self.assertIsInstance(cluster.e('.info h6 a'), WebElement)
		self.assertIsInstance(cluster.e('.info p'), WebElement)
		
		cluster.e('.hp-info-gallery-pin').click()
		sleep(2)
		self.assertIsInstance(self.e('#info-dialog'), WebElement)
	
	def attach_tab_gallery(self):
		self.go('{0}{1}/photos/gallery/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		filter_bar = self.e('.list-filter')
		
		# TODO uncomment
		# self.assertEqual('Filter by:', filter_bar.e('p strong').text)
		
		input_recent = filter_bar.e('#date_upload')
		
		self.assertIsInstance(input_recent, WebElement)
		# TODO imcomment
		# self.assertTrue(input_recent.is_selected())
		
		sleep(6)
		picture = self.e('.gallery:nth-of-type(1) li:nth-of-type(1)')
		sleep(3)
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
		
		sleep(6)
		picture = self.e('.gallery:nth-of-type(1) li:nth-of-type(1)')
		self.assertIsInstance(picture.e('img'), WebElement)
		self.hover(picture)
		
		overlay = picture.e('.overlay')
		
		self.assertIsInstance(overlay.e('h3'), WebElement)
		self.assertIsInstance(overlay.e('p'), WebElement)
		self.assertIsInstance(overlay.e('p a'), WebElement)
		self.assertIsInstance(overlay.e('p span'), WebElement)
		
	def attach_tab_collections(self):
		self.go('{0}{1}/collections/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
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
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		
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
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		h3 = self.e('#page-index h3')
		
		self.assertEqual(self.project_name + " hasn't yet published any Tours.", h3.text)
	
	def attach_tab_collections_empty(self):
		self.go('{0}{1}/collections/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		h3 = self.e('#page-index h3')
		
		self.assertEqual("{0} hasn't yet published any Collections.".format(self.project_name), h3.text)
	
	def attach_tab_slideshow(self):
		self.go('{0}{1}/photos/slideshow/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		self.assertIsInstance(self.e('#prevthumb img')	, WebElement)
		self.assertIsInstance(self.e('#nextthumb img')	, WebElement)
		self.assertIsInstance(self.e('#slidecounter')	, WebElement)
		self.assertIsInstance(self.e('#slidecaption')	, WebElement)
		self.assertIsInstance(self.e('#navigation')		, WebElement)
	
	def attach_tab_comments(self):
		self.go('{0}{1}/photos/stories/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		sleep(3)
		comment = self.e('.stories li:nth-of-type(1)')
		
		self.assertIsInstance(comment.e('.user'), WebElement)
		self.assertIsInstance(comment.e('.story a'), WebElement)
		self.assertIsInstance(comment.e('.story p'), WebElement)
		self.assertIsInstance(comment.e('.story .details a'), WebElement)
	
	def attach_tab_list(self):
		self.go('{0}{1}/photos/list/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		filter_bar = self.e('.list-filter')
		
		self.assertEqual('Sort by:', filter_bar.e('p strong').text)
		
		input_recent = filter_bar.e('#date_upload')
		
		self.assertIsInstance(input_recent, WebElement)
		self.assertTrue(input_recent.is_selected())
		
		sleep(3)
		picture = self.e('.list:nth-of-type(1) li:nth-of-type(1)')
		self.assertIsInstance(picture.e('a'), WebElement)
		
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
		self.go('{0}{1}/mysteries/index/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
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
		
		sleep(4)
		mystery_first = self.e('.attach.mysteries > .list section:nth-of-type(1)')
		self.assertIsInstance(mystery_first.e('h3'), WebElement)
		self.assertIsInstance(mystery_first.e('header a'), WebElement)
		self.assertIsInstance(mystery_first.e('.thumb a'), WebElement)
		self.assertIsInstance(mystery_first.e('.cnt h4 a'), WebElement)
		self.assertIsInstance(mystery_first.e('.clues h6'), WebElement)
		
		solve_button	= mystery_first.e('footer .button')
		status.e('#showme_all').click()
		sleep(5)
		mystery_first	= self.e('.attach.mysteries > .list section:nth-of-type(1)')
		
		self.assertIsInstance(mystery_first.e('h3'), WebElement)
		self.assertIsInstance(mystery_first.e('header a'), WebElement)
		self.assertIsInstance(mystery_first.e('.thumb a'), WebElement)
		self.assertIsInstance(mystery_first.e('.cnt h4 a'), WebElement)
		self.assertIsInstance(mystery_first.e('.clues h6'), WebElement)
		
		status.e('#showme_investigation').click()
		sleep(2)
		mystery_first	= self.e('.attach.mysteries > .list section:nth-of-type(1)')
		solve_button	= mystery_first.e('footer .button')
		
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
		
		