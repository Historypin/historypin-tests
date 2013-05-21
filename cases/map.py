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
		
		search_bar = self.e_wait('.search-bar.by_date')
		self.assertIsInstance(search_bar	, WebElement)
		self.assertEqual('Refine by date'	, search_bar.e('h3').text)
		
		icons = self.es('.search-bar.by_date a span')
		self.assertIn('ss-icon'		, icons[0].get_attribute('class'))
		self.assertIn('ss-location'	, icons[0].get_attribute('class'))
		self.assertIn('ss-icon'		, icons[1].get_attribute('class'))
		self.assertIn('ss-location'	, icons[1].get_attribute('class'))
		
		self.assertEqual('1840', self.e('#from span').text)
		self.assertEqual('2013', self.e('#to span').text)
		
		labels = [
			['1840-01-01', '1840'],
			['1850-01-01', '1850'],
			['1860-01-01', '1860'],
			['1870-01-01', '1870'],
			['1880-01-01', '1880'],
			['1890-01-01', '1890'],
			['1900-01-01', '1900'],
			['1910-01-01', '1910'],
			['1920-01-01', '1920'],
			['1930-01-01', '1930'],
			['1940-01-01', '1940'],
			['1950-01-01', '1950'],
			['1960-01-01', '1960'],
			['1970-01-01', '1970'],
			['1980-01-01', '1980'],
			['1990-01-01', '1990'],
			['2000-01-01', '2000'],
			['2010-01-01', ''], 	 # 2010 - this is item is display: none
			['2013-01-01', '2013'],
		]
		
		link_label = self.es('#date-slider-labels a')
		
		for n in range(len(labels)):
			i = labels[n]
			self.assertEqual(URL_BASE + '/photos/search/date_from/' + i[0]	, link_label[n].get_attribute('href'))
			self.assertEqual(i[1]											, link_label[n].text)
		
		date_from	= self.e_wait('#date-slider-labels li:nth-of-type(3) a')
		date_to		= self.e_wait('#date-slider-labels li:nth-of-type(7) a')
		date_from.click()
		self.assertEqual('1860', date_from.text)
		# date_to.click()
		# self.assertEqual('1990', date_to.text)
		
		# TODO
		# set a date from(e.g. 1887) and date to (e.g. 2005)
		# check if the id='from' and span class has the 1887 value
		# check if the id='to' and span class has the 2005 value 
		# assert that the date slider icon is on 1887
		# assert that the date slider icon is on 2005
		# assert if the URL is changing with selected years
		
		reset = self.e('a.reset')
		self.assertEqual('Some content is hidden (reset)', reset.text)
		self.double_click(reset)
	
	@url('/map/')
	def test_search_by_subject(self):
		
		self.e_wait('p a.subject').click()
		tag = self.e('.by_tag')
		self.assertEqual('Refine your results by subject'	, tag.e('h3').text)
		self.assertEqual('Search by keyword'				, tag.e('label').text)
		
		tag.e('.input-container input').send_keys('transport')
		
		refine = tag.e('.button.right')
		self.assertEqual('REFINE', refine.text)
		refine.click()
		self.assertIn('tags:transport', URL_BASE + '/map/#!/geo:51.6,0.05/zoom:7/tags:transport/')
		
		reset = self.e('a.reset')
		self.assertEqual('Some content is hidden (reset)', reset.text)
		self.double_click(reset)
		
		# click on a photo cluster
		# - in "Details' tab, assert that in Tags section there is transport keyword
		# close the dialogue
		# click on a single photo marker
		# - in "Details' tab, assert that in Tags section there is transport keyword
		# close the dialogue
	
	@url('/map/')
	def test_fullscreen_map(self):
		
		self.e('#fullscreen-on a').click()
		
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
	
	@url('/map/#!/geo:42.697839,23.32167/zoom:10/dialog:22363018/tab:details/')
	def test_dialogue(self):
		
		sleep(3) # ajax on success
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/2000x440/quality/80/', self.e('#details_cnt .image .main-img').get_attribute('src'))
		
		info = self.e('#details_cnt .side.right.scrollbarfix .info')
		self.assertEqual('National Theatre in Sofia, Bulgaria'				, info.e('h2.photo-title').text)
		self.assertEqual('ulitsa "Kuzman Shapkarev" 1, 1000 Sofia, Bulgaria', info.e('strong .photo-address').text)
		self.assertEqual('2 August 2012'									, info.e('strong .photo-date').text)
		
		details_link = self.e('.suggest-details-photo')
		self.assertEqual(URL_BASE + '/contact-us/?suggest/#!/geo:42.697839,23.32167/zoom:10/dialog:22363018/tab:details/'	, details_link.get_attribute('href'))
		self.assertEqual('Suggest more accurate details'																	,details_link.text )
		
		about = self.e('.about')
		self.assertEqual(URL_BASE + '/channels/img/10649049/logo/1/dim/46x46/'		, about.e('img').get_attribute('src'))
		self.assertEqual('Pinned by\nGabss'										, about.e('p.pinned').text)
		self.assertEqual(URL_BASE + '/channels/view/10649049/'						, about.e('p.pinned a').get_attribute('href'))
		self.assertEqual('This is a photo of National Theatre in Sofia, Bulgaria'	, about.e('p.photo-story-copy').text)
		
		self.assertEqual('Tags: national, theatre', self.e('.tags').text)
		keyword = self.es('.tags .photo-keywords a')
		self.assertEqual(URL_BASE + '/map/#!/geo:42.697839,23.32167/zoom:10/dialog:22363018/tab:details/tags:national/'	, keyword[0].get_attribute('href'))
		self.assertEqual(URL_BASE + '/map/#!/geo:42.697839,23.32167/zoom:10/dialog:22363018/tab:details/tags:theatre/'	, keyword[1].get_attribute('href'))
		
		actions = self.e('.bottom-actions')
		
		favourite = actions.e('.action.favourite span')
		self.assertIn('ss-icon', favourite.get_attribute('class'))
		self.assertIn('ss-heart', favourite.get_attribute('class'))
		
		report = actions.e('.action.report')
		self.assertEqual(URL_BASE + '/contact-us/?report/#!/geo:42.697839,23.32167/zoom:10/dialog:22363018/tab:details/', report.get_attribute('href'))
		self.assertIn('ss-icon'	, report.e('span').get_attribute('class'))
		self.assertIn('ss-alert', report.e('span').get_attribute('class'))
		
		streetview = actions.e('.action.photo-view-on-streetview.sv-marker')
		self.assertEqual(URL_BASE + '/map/#streetview_cnt'	, streetview.get_attribute('href'))
		self.assertEqual('Street View'						, streetview.text)
		
		fullscr = actions.e('.action.fullscr.right')
		self.assertEqual('See Bigger  ', fullscr.text)
		self.assertIn('ss-icon'		, fullscr.e('span').get_attribute('class'))
		self.assertIn('ss-scaleup'	, fullscr.e('span').get_attribute('class'))
		fullscr.click()
		self.assertEqual(URL_BASE + '/services/thumb/phid/22363018/dim/3000x500/quality/80/', self.e('#preview_cnt .image img').get_attribute('src'))
		
		fullscr_off = actions.e('.action.see-smaller.right')
		self.assertEqual('See Smaller  '	, fullscr_off.text)
		self.assertIn('ss-icon'			, fullscr_off.e('span').get_attribute('class'))
		self.assertIn('ss-scaledown'	, fullscr_off.e('span').get_attribute('class'))
		fullscr_off.click()
		
		# TODO
		# url is changing to tab:details
		
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
		
	
	@url('/map/')
	def test_pin_cluster(self):
		# TODO
		# assert a photo cluster img src
		# click on the photo cluster
		# in cluster gallery, assert thumbs link and text, paragraph, img src and link
		# click on the first thumb
		# func for testing dialogue
		# assert icons for left and right arrows
		# click on the arrow for previous and next
		pass
	
	url('/map/')
	def test_hp_marker(self):
		# TODO
		# click on a single photo marker
		# assert marker img src
		# func for testing dialogue
		# assert there are noicons for left and right arrows
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
	
