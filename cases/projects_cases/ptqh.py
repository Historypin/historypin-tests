# -*- coding: utf-8 -*-

from base import *

class Project_PTQH(HPTestCase):
	@url('/project/5-DiamondJubilee')
	def test_homepage(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		self.PROJECT_URL = '{0}/project/5-DiamondJubilee'.format(URL_BASE)
		
		self.assertEqual("Queen's Diamond Jubilee", self.e('.queen_logo').text)
		self.assertEqual('{0}/'.format(self.PROJECT_URL), self.e('.queen_logo').get_attribute('href'))
		
		nav = [
			['{0}/'.format(self.PROJECT_URL)			, 'Home'],
			['{0}/visits/'.format(self.PROJECT_URL)		, 'Visits'],
			['{0}/map/'.format(self.PROJECT_URL)		, 'Map'],
			['{0}/pin/'.format(self.PROJECT_URL)		, 'Pin'],
			['{0}/about/'.format(self.PROJECT_URL)		, 'About'],
		]
		
		header = self.e('.map_header')
		nav_li = header.es('.inner_nav li a')
		
		for n in range(len(nav)):
			i = nav[n]
			self.assertEqual(i[0], nav_li[n].get_attribute('href'))
			self.assertEqual(i[1], nav_li[n].text)
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u"A global interactive archive of The Queen’s visits and her Jubilee celebrations to mark the Diamond Jubilee", site_cnt.e('h3').text)
		self.assertIn('Her Majesty visits a large number of places around the UK every year.', site_cnt.e('h3+p').text)
		self.assertIsInstance(site_cnt.e('.big_pin'), WebElement)
		
		buttons = self.es('#site-content .main_cnt a')
		self.assertEqual('{0}/map/'.format(self.PROJECT_URL), buttons[0].get_attribute('href'))
		self.assertEqual('{0}/pin/'.format(self.PROJECT_URL), buttons[1].get_attribute('href'))
		
		img_link = '{0}/resources/images/webapps/buckingham/'.format(URL_BASE)
		
		touts = [
			['HRH Prince William has added a photo and story!'				, '{0}/map/#!/geo:51.340048,-0.768437/marker:11011001/zoom:14/'.format(self.PROJECT_URL), '{0}home_prince_william.jpg?1'.format(img_link)],
			[u'See all 261 of the Queen’s State and Commonwealth visits'	, '{0}/visits/'.format(self.PROJECT_URL)												, '{0}home_visits.jpg?1'.format(img_link)],
		]
		
		h4s			= self.es('.section.w3 .left h4')
		links		= self.es('.section.w3 .left a')
		imgs		= self.es('.section.w3 .left img')
		
		for n in range(len(touts)):
			i = touts[n]
			self.assertEqual(i[0], h4s[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
			self.assertEqual(i[2], imgs[n].get_attribute('src'))
		
		self.assertEqual('The most recent pins', self.e('.section h6').text)
		
		recent_photo = self.e('.recent li:nth-of-type(1) .image-container')
		self.assertIsInstance(recent_photo			, WebElement)
		self.assertIsInstance(recent_photo.e('img')	, WebElement)
		
		upload_photo = self.e('.upload-photo a')
		self.assertEqual('{0}/pin/'.format(self.PROJECT_URL), upload_photo.get_attribute('href'))
		self.assertEqual('Pin your own'			, upload_photo.text)
		
		
		items = [
			['{0}/tours/view/9200092/title/The%201953-1954%20Commonwealth%20Tour'.format(self.PROJECT_URL)							, '{0}pqth_feature_01.jpg'.format(img_link), 'The Commonwealth Tour, 1953-1954'],
			['{0}/tours/view/8747019/title/State%20Visit%20to%20the%20USA%2C%201957'.format(self.PROJECT_URL)						, '{0}pqth_feature_02.jpg'.format(img_link), 'State Visit to USA, 1957'],
			['{0}/collections/view/8734070/title/Silver%20Jubilee%20Street%20Parties%20Collection'.format(self.PROJECT_URL)			, '{0}pqth_feature_03.jpg'.format(img_link), 'Silver Jubilee Street Parties'],
			['{0}/collections/view/8739050/title/Queen%20Elizabeth%20II%20Fancy%20Headwear%20Collection'.format(self.PROJECT_URL)	, '{0}pqth_feature_04.jpg'.format(img_link), "Queen Elizabeth II's Headwear Collection"],
		]
		
		links	= self.es('.features > .col a')
		imgs	= self.es('.features > .col img')
		texts	= self.es('.features > .col span')
		
		for n in range(len(items)):
			i = items[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], imgs[n].get_attribute('src'))
			self.assertEqual(i[2], texts[n].text)
		
		self.assertIsInstance(self.e('.social.center'), WebElement)
		
		footer_items = [
			['{0}/about'					.format(self.PROJECT_URL), 'About'],
			['{0}/faq'					.format(self.PROJECT_URL), 'FAQs'],
			['{0}/terms-and-conditions'	.format(self.PROJECT_URL), 'Terms & Conditions'],
			['{0}/contact'				.format(self.PROJECT_URL), 'Contact'],
		]
		
		footer = self.e('.footer')
		links = footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
		
		support_link = self.e('.support')
		self.assertEqual('http://www.jubileetribute.org/', support_link.get_attribute('href'))
		self.assertEqual('{0}queens_foot_logo.png'.format(img_link), support_link.e('img').get_attribute('src'))
	
	@url('/project/5-DiamondJubilee/visits/')
	def test_visits(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		self.assertIsInstance(self.e('#jubilee'), WebElement)
		self.assertEqual(u'The Queen\u2019s   State and Commonwealth visits\n1952 \u2013 2012'	, self.e('h2').text)
		self.assertEqual(u'Click on a visit to see what’s been pinned in each country...'		, self.e('h4').text)
		
		link_visit = self.e('.list:nth-of-type(1) li:nth-of-type(1) a')
		self.assertEqual('{0}/project/5-DiamondJubilee/map/index/index/geo/-0.221313,38.054509/zoom/6/'.format(URL_BASE), link_visit.get_attribute('href'))
		self.assertEqual('Kenya', link_visit.e('span').text)
	
	@url('/project/5-DiamondJubilee/map/')
	def test_map(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		filter_bar = self.e('#filter-bar')
		
		self.assertEqual('find content near'								, filter_bar.e('label').text)
		self.assertIsInstance(filter_bar.e('#location')						, WebElement)
		self.assertIsInstance(filter_bar.e('#photo_search_submit')			, WebElement)
		self.assertIsInstance(self.e('.ui-slider-range.ui-widget-header')	, WebElement)
		self.assertIsInstance(self.e('#date-slider-labels li')				, WebElement)
		self.assertIsInstance(self.e('#map')								, WebElement)
	
	@url('/project/5-DiamondJubilee/pin/')
	def test_pin_page(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual("Make your content part of The Queen's History", site_cnt.e('h1').text)
		self.assertIn("If you would like to submit your pictures, videos or audio recordings of the Queen's visits", site_cnt.e('p:first-of-type').text)
		
		self.assertEqual('{0}/project/5-DiamondJubilee/upload/'									.format(URL_BASE), site_cnt.e('a').get_attribute('href'))
		self.assertEqual('{0}/resources/images/webapps/buckingham/queen_elizabeth_pinning.jpg'	.format(URL_BASE), site_cnt.e('img').get_attribute('src'))
	
	@url('/project/5-DiamondJubilee/about/')
	def test_about(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		img_link = '{0}/resources/images/webapps/buckingham/'.format(URL_BASE)
		
		items_about = [
			['About the project', '{0}queen_elizabeth.jpg'	.format(img_link)],
			['Historypin'		, '{0}historypin_logo.jpg'	.format(img_link)],
			['Google'			, '{0}google_logo.jpg'		.format(img_link)],
		]
		
		site_cnt	= self.e('#site-content')
		h1s			= site_cnt.es('.section h1')
		imgs		= site_cnt.es('.section img')
		
		for n in range(len(items_about)):
			i = items_about[n]
			self.assertEqual(i[0], h1s[n].text)
			self.assertEqual(i[1], imgs[n].get_attribute('src'))
		
		links = site_cnt.es('.section a')
		
		self.assertEqual('http://shiftdesign.org.uk/', links[0].get_attribute('href'))
		self.assertEqual('{0}/'.format(URL_BASE)		, links[1].get_attribute('href'))
		self.assertEqual('http://google.com/'			, links[2].get_attribute('href'))
	
	@url('/project/5-DiamondJubilee/contact/')
	def test_contact(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		section = self.e('.section')
		self.assertEqual('Contact', section.e('h1').text)
		
		headings_h2 = ['General enquiries, technical enquiries, content enquiries', 'Media', 'Schools, local projects and volunteers', 'Library, archive and museum partnerships', 'Web', 'Corporate Partnerships']
		
		h2s = section.es('h2')
		for n in range(len(headings_h2)): self.assertEqual(headings_h2[n], h2s[n].text)
