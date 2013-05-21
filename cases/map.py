# -*- coding: utf-8 -*-

from base import *

class Map(HPTestCase):
	
	@url('/map/')
	def test_index(self):
		self.assertTitle('Historypin | Map')
		
		self.assertEqual('Search\nby place'										, self.e('.main-panel h1').text)
		self.assertIsInstance(self.e('#search-filters .input-container input')	, WebElement)
		
		button		= self.e('a#photo_search_submit')
		self.assertEqual(URL_BASE + '/map/#'		, button.get_attribute('href'))
		self.assertEqual('GO'						, button.text)
		
		nav			= self.e('.filter-nav')
		self.assertEqual('Narrow down'				, nav.e('h2').text)
		self.assertEqual('by date'					, nav.e('p a.date').text)
		self.assertEqual('by subject'				, nav.e('p a.subject').text)
		
		check_cnt	= self.e('.check_container')
		self.assertIsInstance(check_cnt.e('input')	, WebElement)
		self.assertEqual('show thumbnails'			, check_cnt.e('label').text)
		
		fullscr		= self.e('#fullscreen-on a')
		self.assertEqual('Full\nScreen'				, fullscr.text)
		self.assertIn('ss-icon'						, fullscr.e('span').get_attribute('class'))
		self.assertIn('ss-scaleup'					, fullscr.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('#map-canvas')	, WebElement)
	
	@url('/map/')
	def test_search_by_place(self):
		
		input_cnt = self.e('#search-filters .input-container input')
		input_cnt.click()
		sleep(1)
		
		input_cnt.send_keys('Sofia')
		sleep(1)
		
		self.e('.button.left').click()
		sleep(1)
		
		self.assertIn('42.697839,23.32167', URL_BASE + '/map/#!/geo:42.697839,23.32167/zoom:10/location:Sofia, Bulgaria/')
	
	@url('/map/')
	def test_search_by_date(self):
		
		self.e('a.date').click()
		sleep(1)
		
		# TODO
		# click on by date link
		# assert search bar by date:
		# - refine by date text
		# - assert date selector
		# - assert date slider labels
		# - assert date slider marker from and to
		# set a date from(e.g. 1887) and date to (e.g. 2005)
		# check if the id='from' and span class has the 1887 value
		# check if the id='to' and span class has the 2005 value
		# click on a photo cluster
		# in "Details' tab check if the photo is in the set interval
		# close the dialogue
		# click on a single photo marker
		# in "Details' tab check if the photo is in the set interval
		# close the dialogue
		# assert Some content is hidden(reset) text
		# double click on Some content.. link
		pass
	
	@url('/map/')
	def test_search_by_subject(self):
		# TODO
		# click on by subject link
		# assert search bar by subject:
		# - Refine your results by subject text
		# - Search by keyword text
		# assert input text field
		# - click in the input field
		# - type "transport" keyword
		# assert refine button link and text
		# - click "Refine"
		# click on a photo cluster
		#	- in "Details' tab, assert that in Tags section there is transport keyword
		# close the dialogue
		# click on a single photo marker
		# 		in "Details' tab, assert that in Tags section there is transport keyword
		# close the dialogue
		# assert Some content is hidden(reset) text
		# double click on Some content.. link
		pass
	
	@url('/map/')
	def test_fullscreen_map(self):
		
		self.e('#fullscreen-on a').click()
		sleep(2)
		
		main_panel = self.e('.main-panel a')
		self.assertEqual(URL_BASE + '/', main_panel.get_attribute('href'))
		self.assertIn('fullscreen_logo', main_panel.get_attribute('class'))
		
		search_filters = self.e('#search-filters')
		self.assertEqual('Location'									, search_filters.e('label').text)
		self.assertIsInstance(search_filters.e('input')				, WebElement)
		self.assertIsInstance(self.e('#photo_search_submit span')	, WebElement)
		
		self.assertEqual('Narrow down'		, self.e('.filter-nav h2').text)
		
		fullscr_off = self.e('#fullscreen-off')
		self.assertEqual('Exit fullscreen'	, fullscr_off.text)
		self.assertIn('ss-icon'				, fullscr_off.e('span').get_attribute('class'))
		self.assertIn('ss-scaledown'		, fullscr_off.e('span').get_attribute('class'))
		
		fullscr_off.click()
		sleep(2)
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:22363018/tab:details/')
	def test_pin_dialogue(self):
		# TODO
		# Details Tab:
		# - assert Details text
		# - assert img src
		# - assert heading
		# - assert paragraph and views
		# - assert Suggest more accurate details link and text
		# - assert channel img and link and text pinned by
		# - assert pin description text
		# - Tags text and links
		# - favourite, report streetview links and texts
		# - assert see bigger icon and text
		# - click on see bigger
		# 	- assert image src and see smaller text
		# click on see smaller
		# Comments Tab:
		# - click on Comments Tab
		# - assert Comments text
		# - in the sidebar:
		# - assert image src
		# - assert pinner info - img src, channel link, pinned by text
		# - assert heading, paragraph, year 
		# - in the stories list:
		# - assert channel img text, channel link and paragraph
		# - assert write story wrap link
		# - assert avatar
		# - click on area for writing a story
		# - go back to the dialogue
		# Streetview Tab:
		# - click on Streetview tab
		# - assert streetview text
		# - assert text under the image
		# - assert streetview slider and icon
		# - assert reset text and icon
		# - assert fullscr text and icon
		# - click on fullscr
		# - assert img src
		# - assert exit fullscr link and text
		# - click on exit fullscr
		# Repeats Tab:
		# - assert img src
		# - assert HP Repeats text
		# - assert paragraph
		# - assert app link
		# - assert paragraph 
		# Copyright Tab:
		# - assert copyright text
		# -assert sidebar like in the comment tab
		# assert share text
		# assert share media icons
		pass
	
	@url('/map/')
	def test_pin_cluster(self):
		# TODO
		# assert a photo cluster img src
		# click on the photo cluster
		# in cluster gallery, assert thumbs link and text, paragraph, img src and link
		# click on the first thumb
		# func for testing dialogue
		pass
	
	url('/map/')
	def test_hp_marker(self):
		# TODO
		# click on a single photo marker
		# assert marker img src
		# func for testing dialogue
		# assert icons for left and right arrows
		# click on the arrow for previous and next
		pass
	
	@url('/map/')
	def test_footer(self):
		
		footer = [
			[URL_BASE + '/'						, 'Home'],
			[URL_BASE + '/about-us'				, 'About'],
			[URL_BASE + '/faq'					, 'FAQs'],
			[URL_BASE + '/presscentre'			, 'Press Centre'],
			[URL_BASE + '/donate'				, 'Support us'],
			[URL_BASE + '/app'					, 'Mobile App'],
			[URL_BASE + '/terms-and-conditions'	, 'Terms and Conditions'],
			[URL_BASE + '/privacy-policy'		, 'Privacy Policy'],
			[URL_BASE + '/cookies'				, 'Cookies'],
			[URL_BASE + '/contact'				, 'Contact'],
			['http://wearewhatwedo.org/'		, u'© 2012 We Are What We Do'],
		]
		
		lists = self.es('.nav.cf li a')
		
		for n in range(len(footer)):
			i = footer[n]
			self.assertEqual(i[0]			, lists[n].get_attribute('href'))
			self.assertEqual(i[1]			, lists[n].text)
	
