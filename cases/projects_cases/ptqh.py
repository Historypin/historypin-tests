# -*- coding: utf-8 -*-

from base import *

class Project_PTQH(HPTestCase):
	@url('/project/5-DiamondJubilee')
	def test_homepage(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		self.PROJECT_URL = '%s/project/5-DiamondJubilee' % URL_BASE
		
		self.assertEqual("Queen's Diamond Jubilee", self.e('.queen_logo').text)
		self.assertEqual('%s/' % self.PROJECT_URL, self.e('.queen_logo').get_attribute('href'))
		
		nav = [
			['%s/' % self.PROJECT_URL			, 'Home'],
			['%s/visits/' % self.PROJECT_URL	, 'Visits'],
			['%s/map/' % self.PROJECT_URL		, 'Map'],
			['%s/pin/' % self.PROJECT_URL		, 'Pin'],
			['%s/about/' % self.PROJECT_URL	, 'About'],
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
		self.assertEqual('%s/map/' % self.PROJECT_URL, buttons[0].get_attribute('href'))
		self.assertEqual('%s/pin/' % self.PROJECT_URL, buttons[1].get_attribute('href'))
		
		img_link = '%s/resources/images/webapps/buckingham/' % URL_BASE
		
		touts = [
			['HRH Prince William has added a photo and story!'				, '%s/map/#!/geo:51.340048,-0.768437/marker:11011001/zoom:14/' % self.PROJECT_URL	, '%shome_prince_william.jpg?1' % img_link],
			[u'See all 261 of the Queen’s State and Commonwealth visits'	, '%s/visits/' % self.PROJECT_URL													, '%shome_visits.jpg?1' % img_link],
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
		self.assertEqual('%s/pin/' % self.PROJECT_URL	, upload_photo.get_attribute('href'))
		self.assertEqual('Pin your own'			, upload_photo.text)
		
		
		items = [
			['{0}/tours/view/9200092/title/The%201953-1954%20Commonwealth%20Tour'.format(self.PROJECT_URL)							, '%spqth_feature_01.jpg' % img_link, 'The Commonwealth Tour, 1953-1954'],
			['{0}/tours/view/8747019/title/State%20Visit%20to%20the%20USA%2C%201957'.format(self.PROJECT_URL)						, '%spqth_feature_02.jpg' % img_link, 'State Visit to USA, 1957'],
			['{0}/collections/view/8734070/title/Silver%20Jubilee%20Street%20Parties%20Collection'.format(self.PROJECT_URL)		, '%spqth_feature_03.jpg' % img_link, 'Silver Jubilee Street Parties'],
			['{0}/collections/view/8739050/title/Queen%20Elizabeth%20II%20Fancy%20Headwear%20Collection'.format(self.PROJECT_URL)	, '%spqth_feature_04.jpg' % img_link, "Queen Elizabeth II's Headwear Collection"],
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
			['%s/about'					% self.PROJECT_URL, 'About'],
			['%s/faq'					% self.PROJECT_URL, 'FAQs'],
			['%s/terms-and-conditions'	% self.PROJECT_URL, 'Terms & Conditions'],
			['%s/contact'				% self.PROJECT_URL, 'Contact'],
		]
		
		footer = self.e('.footer')
		links = footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
		
		support_link = self.e('.support')
		self.assertEqual('http://www.jubileetribute.org/', support_link.get_attribute('href'))
		self.assertEqual('%squeens_foot_logo.png' % img_link, support_link.e('img').get_attribute('src'))
	
	@url('/project/5-DiamondJubilee/visits/')
	def test_visits(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		self.assertIsInstance(self.e('#jubilee'), WebElement)
		self.assertEqual(u'The Queen\u2019s   State and Commonwealth visits\n1952 \u2013 2012'	, self.e('h2').text)
		self.assertEqual(u'Click on a visit to see what’s been pinned in each country...'		, self.e('h4').text)
		
		link_visit = self.e('.list:nth-of-type(1) li:nth-of-type(1) a')
		self.assertEqual(URL_BASE + '/project/5-DiamondJubilee/map/index/index/geo/-0.221313,38.054509/zoom/6/', link_visit.get_attribute('href'))
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
		
		self.assertEqual(URL_BASE + '/project/5-DiamondJubilee/upload/'									, site_cnt.e('a').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/webapps/buckingham/queen_elizabeth_pinning.jpg'	, site_cnt.e('img').get_attribute('src'))
	
	@url('/project/5-DiamondJubilee/about/')
	def test_about(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		img_link = URL_BASE + '/resources/images/webapps/buckingham/'
		
		items_about = [
			['About the project', '%squeen_elizabeth.jpg'	% img_link],
			['Historypin'		, '%shistorypin_logo.jpg'	% img_link],
			['Google'			, '%sgoogle_logo.jpg'		% img_link],
		]
		
		site_cnt	= self.e('#site-content')
		h1s			= site_cnt.es('.section h1')
		imgs		= site_cnt.es('.section img')
		
		for n in range(len(items_about)):
			i = items_about[n]
			self.assertEqual(i[0], h1s[n].text)
			self.assertEqual(i[1], imgs[n].get_attribute('src'))
		
		links = site_cnt.es('.section a')
		
		self.assertEqual('http://wearewhatwedo.org/', links[0].get_attribute('href'))
		self.assertEqual('http://historypin.com/'	, links[1].get_attribute('href'))
		self.assertEqual('http://google.com/'		, links[2].get_attribute('href'))
	
	@url('/project/5-DiamondJubilee/contact/')
	def test_contact(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		section = self.e('.section')
		self.assertEqual('Contact', section.e('h1').text)
		
		headings_h2 = ['General enquiries, technical enquiries, content enquiries', 'Media', 'Schools, local projects and volunteers', 'Library, archive and museum partnerships', 'Web', 'Corporate Partnerships']
		
		h2s = section.es('h2')
		for n in range(len(headings_h2)): self.assertEqual(headings_h2[n], h2s[n].text)
