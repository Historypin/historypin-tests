# -*- coding: utf-8 -*-

from base import *

class Project_PTQH(HPTestCase):
	@url('/project/5-DiamondJubilee')
	def test_homepage(self):
		
		self.assertTitle("Pinning The Queen's history")
		
		ptqh_link = URL_BASE + '/project/5-DiamondJubilee'
		
		self.assertEqual("Queen's Diamond Jubilee", self.e('.queen_logo').text)
		self.assertEqual('%s/' % ptqh_link, self.e('.queen_logo').get_attribute('href'))
		
		nav = [
			['%s/' % ptqh_link			, 'Home'],
			['%s/visits/' % ptqh_link	, 'Visits'],
			['%s/map/' % ptqh_link		, 'Map'],
			['%s/pin/' % ptqh_link		, 'Pin'],
			['%s/about/' % ptqh_link	, 'About'],
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
		self.assertEqual('%s/map/' % ptqh_link, buttons[0].get_attribute('href'))
		self.assertEqual('%s/pin/' % ptqh_link, buttons[1].get_attribute('href'))
		
		img_link = URL_BASE + '/resources/images/webapps/buckingham/'
		
		touts = [
			['HRH Prince William has added a photo and story!'				, '%s/map/#!/geo:51.340048,-0.768437/marker:11011001/zoom:14/' % ptqh_link	, '%shome_prince_william.jpg?1' % img_link],
			[u'See all 261 of the Queen’s State and Commonwealth visits'	, '%s/visits/' % ptqh_link													, '%shome_visits.jpg?1' % img_link],
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
		self.assertEqual('%s/pin/' % ptqh_link	, upload_photo.get_attribute('href'))
		self.assertEqual('Pin your own'			, upload_photo.text)
		
		
		items = [
			['{0}/tours/view/9200092/title/The%201953-1954%20Commonwealth%20Tour'.format(ptqh_link)							, '%spqth_feature_01.jpg' % img_link, 'The Commonwealth Tour, 1953-1954'],
			['{0}/tours/view/8747019/title/State%20Visit%20to%20the%20USA%2C%201957'.format(ptqh_link)						, '%spqth_feature_02.jpg' % img_link, 'State Visit to USA, 1957'],
			['{0}/collections/view/8734070/title/Silver%20Jubilee%20Street%20Parties%20Collection'.format(ptqh_link)		, '%spqth_feature_03.jpg' % img_link, 'Silver Jubilee Street Parties'],
			['{0}/collections/view/8739050/title/Queen%20Elizabeth%20II%20Fancy%20Headwear%20Collection'.format(ptqh_link)	, '%spqth_feature_04.jpg' % img_link, "Queen Elizabeth II's Headwear Collection"],
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
			['%s/about'					% ptqh_link, 'About'],
			['%s/faq'					% ptqh_link, 'FAQs'],
			['%s/terms-and-conditions'	% ptqh_link, 'Terms & Conditions'],
			['%s/contact'				% ptqh_link, 'Contact'],
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
		# TODO
		# check the title
		# check the video element present
		# check title
		# check text
		# check at least one visit
		pass
	
	@url('/project/5-DiamondJubilee/map/')
	def test_map(self):
		# TODO
		# title
		# check text
		# check the input
		# check year slider
		# check if there is a map
		pass
	
	@url('/project/5-DiamondJubilee/pin/')
	def test_pin_page(self):
		# TODO
		# check the title
		# check the button link and text
		# check the image
		# check share text and icons
		pass
	
	@url('/project/5-DiamondJubilee/about/')
	def test_about(self):
		# check the title
		# check the titles
		# check the images
		# check the texts
		pass
	
	@url('/project/5-DiamondJubilee/contact/')
	def test_contact(self):
		# check the title
		# check the titles
		# check the images
		# check the texts
		pass
