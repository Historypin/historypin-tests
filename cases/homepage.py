# -*- coding: utf-8 -*-

from base import *

class Homepage(HPTestCase):
	@url('/')
	def test_cookie_message(self):
		self.assertEqual(
			'We want you to enjoy your visit to our website. That\'s why we use cookies to enhance your experience.\nBy staying on our website you agree to our use of cookies. Find out more about the cookies we use.',
			self.e('.cookies-popup p').text,
		)
		
		self.assertEqual(URL_BASE + '/pages/cookies/',				self.e('.cookies-popup p a').get_attribute('href'))
		a = self.e('.cookies-popup a.right')
		self.assertEqual('Close this message  close', a.text)
		a.click()
		
		self.browser.refresh()
		self.assertRaises(NoSuchElementException, self.e, '.cookies-popup')
	
	@unittest.expectedFailure
	@url('/')
	def test_navigation(self):
		
		links = [
			[ 'Home'					, URL_BASE + '/' ],
			[ 'Map'						, URL_BASE + '/map/' ],
			[ 'Projects'				, URL_BASE + '/projects/' ],
			[ 'Channels'				, URL_BASE + '/channels/' ],
			[ 'Tours and Collections'	, URL_BASE + '/curated/' ],
			[ 'Get Involved'			, URL_BASE + '/community/' ],
			[ 'Blog'					, 'http://blog.historypin.com/' ],
			[ 'Login'					, URL_BASE + '/_ah/login?continue=http%3A//www.localhost.com%3A8080/user/login/' ],
			[ 'Join'					, URL_BASE + '/user/' ],
			[ 'Pin'						, URL_BASE + '/upload/' ],
		]
		
		elements = self.es('#header .nav a')
		for i in range(len(elements)):
			item = links[i]
			self.assertEqual(item[0], elements[i].text)
			self.assertEqual(item[1], elements[i].get_attribute('href'))
	
	@url('/')
	def test_header(self):
		self.assertTitle('Historypin | Home')
		
		branding = self.e('#branding h1')
		self.assertEqual(URL_BASE + '/'								, branding.e('a').get_attribute('href'))
		self.assertEqual(URL_BASE + '/resources/images/hp_logo.png'	, branding.e('img').get_attribute('src'))
		self.assertEqual('A global community collaborating around history', self.e('#branding .home-top p').text)
		
		social_icons = [
			['ss-social-circle', 'https://plus.google.com/116628462065893538180/posts'],
			['ss-social-circle', 'http://www.facebook.com/pages/Historypin/192291707448024'],
			['ss-social-circle', 'http://twitter.com/Historypin'],
		]
		
		links	= self.es('.social_links a')
		
		for n in range(len(social_icons)):
			i = social_icons[n]
			self.assertIn('ss-icon'	, links[n].get_attribute('class'))
			self.assertIn(i[0]		, links[n].get_attribute('class'))
			self.assertEqual(i[1]	, links[n].get_attribute('href'))
	
	@url('/')
	def test_featured(self):
		prev	= self.e('#featured .prev')
		next	= self.e('#featured .next')
		ul		= self.e('#featured ul')
		li		= self.e_wait('#featured li:first-of-type')
		
		self.assertEqual('0px', ul.css('left'))
		
		next.click()
		sleep(.5)
		self.assertEqual('-' + li.css('width'), ul.css('left'))
		
		prev.click()
		sleep(.5)
		self.assertEqual('0px', ul.css('left'))
		
		fulscr	= self.e('.fullscr')
		body	= self.e('body')
		
		fulscr.click()
		sleep(.5)
		self.assertIn('home-fullscreen', body.get_attribute('class'))
		
		fulscr.click()
		self.assertNotIn('home-fullscreen', body.get_attribute('class'))
		sleep(.5)
		
		# TODO LATER
		# - favourite
	
	@url('/')
	def test_activity(self):
		
		self.assertGreater(int(self.e('.counter').text.replace(',', '')), 0)
		more = self.e('#activity .more')
		
		more.click()
		sleep(.5)
		
		less = self.e('#activity .less')
		less.click()
		sleep(.5)
		
		# TODO
		# verify if the activity is expaned to check if element has style property with height= 388 and 700px
		# verify if projects are collapsed
	
	@url('/')
	def test_explore(self):
		
		self.assertEqual('Explore where you live...', self.e('#search h2').text)
		
		self.e('#search-location').send_keys("London, United Kingdom")
		
		first_suggestion = self.e_wait('.pac-container .pac-item')
		self.assertEqual('London, United Kingdom', first_suggestion.text)
		
		first_suggestion.click()
		sleep(.3)
		self.assertEqual(self.browser.current_url.split('#')[0], URL_BASE + '/map/')
	
	# @unittest.skip("TODO")
	# @url('/')
	# def test_explore_go_button(self):
		
	# 	self.assertEqual('Explore where you live...', self.e('#search h2').text)
		
	# 	self.e('#search-location').send_keys("London")
		
		# first_suggestion = self.e_wait('.pac-container .pac-item')
		# self.assertEqual(first_suggestion.text, 'London, United Kingdom')
		
		# first_suggestion.click()
		# sleep(.3)
		# self.assertEqual(self.browser.current_url.split('#')[0], URL_BASE + '/map/')
	
	@url('/')
	def test_projects(self):
	
		listing		= self.e('.listing .w320')
		self.assertIsInstance(listing.e('h2'), WebElement)
		self.assertIsInstance(listing.e('p'), WebElement)
		self.assertIsInstance(listing.e('img'), WebElement)
		self.assertIsInstance(listing.e('a.banner-holder'), WebElement)
		pages = self.es('.slider-paging .page')
		pages[0].click()
		pages[1].click()
		
		browse_all = self.e('#featured-projects .bar a.right')
		self.assertEqual(URL_BASE + '/projects/'	, browse_all.get_attribute('href'))
		self.assertEqual('Browse all projects'		, browse_all.text)
	
	# @url('/')
	# def test_icon_touts(self):
		
	# 	features = [
	# 		['ss-cell', URL_BASE + '/app/', 'Download the latest Historypin\nsmartphone app'],
	# 		['ss-trophy', 'http://blog.historypin.com/2013/05/31/weve-updated-our-terms-and-conditions', 'We\'ve won a webby award for best charity non-profit website'],
	# 		['ss-user', URL_BASE + '/team/', 'Meet the team working on Historypin around the world'],
	# 	]
		
	# 	icons = self.es('.features span')
	# 	links = self.es('.features a')
	# 	for n in range(len(features)):
	# 		i = features[n]
			
	# 		self.assertIn('ss-icon'	, icons[n].get_attribute('class'))
	# 		# self.assertIn(i[0]	, icons[n].get_attribute('class'))
	# 		self.assertEqual(i[1]	, links[n].get_attribute('href'))
	# 		self.assertEqual(i[2]	, links[n].text)
	
	@url('/')
	def test_sponsors(self):
		
		self.assertEqual(self.e('.support h5').text, 'Supported by:')
		
		partners = [
			['http://www.nominettrust.org.uk/', '/resources/images/partners/nominet_colored.png'],
			['http://www.google.co.uk/intl/en/about/', '/resources/images/partners/google_logo.jpg'],
		]
		
		links	= self.es('.partners li a')
		images	= self.es('.partners li img')
		for n in range(len(partners)):
			i = partners[n]
			self.assertEqual(i[0]				, links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + i[1]	, images[n].get_attribute('src'))
		
		support = self.es('.support .donate')
		self.assertEqual('users\nDonate to support Historypin'	, support[0].text)
		self.assertEqual(URL_BASE + '/friends-of-Historypin'	, support[0].get_attribute('href'))
		self.assertIn('ss-icon', self.e('.support .donate .ss-icon').get_attribute('class'))
		
	@url('/')
	def test_footer(self):
		links = [
			[ 'About'							, URL_BASE + '/about-us/' ],
			[ 'FAQ'								, URL_BASE + '/faq/' ],
			[ 'How To Guides'					, URL_BASE + '/how-to/' ],
			[ 'We Are What We Do'				, URL_BASE + '/wearewhatwedo/' ],
			[ 'Team'							, URL_BASE + '/team/' ],
			[ 'Press Centre'					, URL_BASE + '/presscentre/' ],
			[ 'Contact'							, URL_BASE + '/contact/' ],
			
			[ 'Map'								, URL_BASE + '/map/' ],
			[ 'Projects'						, URL_BASE + '/projects/' ],
			[ 'Tours and Collections'			, URL_BASE + '/curated/' ],
			[ 'Channels'						, URL_BASE + '/channels/' ],
			[ 'Pin'								, URL_BASE + '/upload/' ],
			[ 'Mobile App'						, URL_BASE + '/app/' ],
			
			[ 'Community'						, URL_BASE + '/community/' ],
			[ 'Local Projects'					, URL_BASE + '/community/localprojects/' ],
			[ 'Schools'							, URL_BASE + '/community/schools/' ],
			[ 'Libraries, Archives and Museums'	, URL_BASE + '/community/lams/' ],
			[ 'Support Historypin'				, URL_BASE + '/Friends-of-Historypin/' ],
			
			[ 'Blog'							, 'http://blog.historypin.com/' ],
			[ 'Facebook'						, 'http://www.facebook.com/pages/Historypin/192291707448024/' ],
			[ 'Twitter'							, 'http://twitter.com/Historypin/' ],
			[ 'Google+'							, 'https://plus.google.com/116628462065893538180/posts/' ],
			[ 'Newsletter'						, URL_BASE + '/newsletter/' ],
			
			[ 'Privacy policy'					, URL_BASE + '/privacy-policy/' ],
			[ 'Cookies'							, URL_BASE + '/cookies/' ],
			[ 'Terms and Conditions'			, URL_BASE + '/terms-and-conditions/' ],
			[ u'\xa9 We Are What We Do'			, 'http://www.wearewhatwedo.org/' ],
		]
		
		elements = self.es('.footer ul a')
		for i in range(len(elements)):
			item = links[i]
			self.assertEqual(item[0], elements[i].text)
			self.assertEqual(item[1], elements[i].get_attribute('href'), 'Wrong link - %s' % (links[i][0]))
