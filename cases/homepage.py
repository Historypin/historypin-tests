# -*- coding: utf-8 -*-

from base import *

class Homepage(HPTestCase):
	@url('/')
	def test_cookie_message(self):
		self.assertEqual(
			'We want you to enjoy your visit to our website. That\'s why we use cookies to enhance your experience.\nBy staying on our website you agree to our use of cookies. Find out more about the cookies we use.',
			self.e('.cookies-popup p').text,
		)
		
		self.assertEqual('{0}/cookies/'.format(URL_BASE), self.e('.cookies-popup p a').get_attribute('href'))
		a = self.e('.cookies-popup a.right')
		self.assertEqual('Close this message  close', a.text)
		a.click()
		
		self.browser.refresh()
		self.assertRaises(NoSuchElementException, self.e, '.cookies-popup')
	
	@url('/')
	def test_navigation(self):
		
		links = [
			[ 'Home'					, '{0}/'			.format(URL_BASE) ],
			[ 'Map'						, '{0}/map/'		.format(URL_BASE) ],
			[ 'Projects'				, '{0}/projects/'	.format(URL_BASE) ],
			[ 'Profiles'				, '{0}/channels/'	.format(URL_BASE) ],
			[ 'Tours and Collections'	, '{0}/curated/'	.format(URL_BASE) ],
			[ 'Get Involved'			, '{0}/community/'	.format(URL_BASE) ],
			[ 'Blog'					, 'http://blog.historypin.com/' ],
			[ 'Login'					, '{0}/user/'		.format(URL_BASE) ],
			[ 'Join'					, '{0}/user/join/'	.format(URL_BASE) ],
			[ 'Pin'						, '{0}/upload/'		.format(URL_BASE) ],
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
		self.assertEqual('{0}/'								.format(URL_BASE), branding.e('a').get_attribute('href'))
		self.assertEqual('{0}/resources/images/hp_logo.png'	.format(URL_BASE), branding.e('img').get_attribute('src'))
		self.assertEqual('A global community collaborating around history', self.e('#branding .home-top p').text)
		
		circle_icon = 'ss-social-circle'
		
		social_icons = [
			[circle_icon, 'https://plus.google.com/116628462065893538180/posts'],
			[circle_icon, 'http://www.facebook.com/pages/Historypin/192291707448024'],
			[circle_icon, 'http://twitter.com/Historypin'],
		]
		
		links	= self.es('.social_links a')
		
		for n in range(len(social_icons)):
			i = social_icons[n]
			self.assertIn('ss-icon'	, links[n].get_attribute('class'))
			self.assertIn(i[0]		, links[n].get_attribute('class'))
			self.assertEqual(i[1]	, links[n].get_attribute('href'))
	
	@url('/')
	def test_featured(self):
		featured	= self.e('#featured')
		prev		= featured.e('.prev')
		next		= featured.e('.next')
		ul			= featured.e('ul')
		li			= featured.e('li:first-of-type')
		
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
	
	# TODO
	# This test will fail, because the expand/collapse functionality was removed
	# @url('/')
	# def test_activity(self):
		
	# 	self.assertGreater(int(self.e('.counter').text.replace(',', '')), 0)
	# 	more = self.e('#activity .more')
		
	# 	more.click()
	# 	sleep(2)
	# 	# activity_height = self.e('.scrollbarfix').height()
	# 	# self.assertEqual('613.484375px', activity_height)
		
	# 	less = self.e('#activity .less')
	# 	less.click()
	# 	sleep(2)
		
	# 	# TODO
	# 	# verify if the activity is expaned to check if element has style property with height= 388 and 700px
	# 	# verify if projects are collapsed
	
	@url('/')
	def test_activity_items_len(self):
		
		activity = self.e('.scrollbarfix')
		activity_items = activity.es('li')
		self.assertEqual(20, len(activity_items))
	
	@unittest.expectedFailure
	@url('/')
	def test_explore(self):
		
		self.assertEqual('Explore where you live...', self.e('#search h2').text)
		
		self.e('#search-location').send_keys("London, United Kingdom")
		sleep(3)
		self.e('#search-location').click()
		sleep(3)
		first_suggestion = self.e('.pac-container .pac-item-refresh')  # TODO fix this
		# self.assertIsInstance(first_suggestion, WebElement)
		
		first_suggestion.click()
		sleep(.3)
		self.assertEqual(self.browser.current_url.split('#')[0], '{0}/map/'.format(URL_BASE))
	
	@url('/')
	def test_projects(self):
	
		listing = self.e('.listing .w320')
		self.assertIsInstance(listing.e('h2'), WebElement)
		self.assertIsInstance(listing.e('p'), WebElement)
		self.assertIsInstance(listing.e('img'), WebElement)
		self.assertIsInstance(listing.e('a.banner-holder'), WebElement)
		# pages = self.es('.slider-paging .page')
		# pages[0].click()
		# pages[1].click()
		
		browse_all = self.e('#featured-projects .bar a.right')
		self.assertEqual('{0}/projects/'.format(URL_BASE), browse_all.get_attribute('href'))
		self.assertEqual('Browse all projects'		, browse_all.text)
	
	@url('/')
	def test_icon_touts(self):
		
		features = [
			['ss-newtag'			, '{0}/en/explore/first-world-war-centenary/'		.format(URL_BASE)			, 'The First World War Centenary Hub'],
			['ss-trophy'			, '{0}/presscentre/'.format(URL_BASE)											, 'We\'ve won a webby award for best charity non-profit website'],
			['ss-exclamationchat'	, 'http://blog.historypin.com/2013/05/31/weve-updated-our-terms-and-conditions'	, "We've updated our\nTerms and Conditions"],
		]
		
		icons = self.es('.features span')
		links = self.es('.features a')
		for n in range(len(features)):
			i = features[n]
			
			self.assertIn('ss-icon'	, icons[n].get_attribute('class'))
			self.assertIn(i[0]		, icons[n].get_attribute('class'))
			self.assertEqual(i[1]	, links[n].get_attribute('href'))
			self.assertEqual(i[2]	, links[n].text)
	
	@url('/')
	def test_sponsors(self):
		
		self.assertEqual(self.e('.support h5').text, 'Supported by:')
		
		partners = ['http://www.nominettrust.org.uk/', 'http://www.google.co.uk/intl/en/about/']
		links	= self.es('.partners li a')
		
		for n in range(len(partners)): self.assertEqual(partners[n], links[n].get_attribute('href'))
		
		# support = self.es('.support .donate')
		# self.assertEqual('users\nDonate to support Historypin'	, support[0].text)
		# self.assertEqual('{0}/friends-of-Historypin'.format(URL_BASE), support[0].get_attribute('href'))
		# self.assertIn('ss-icon', self.e('.support .donate .ss-icon').get_attribute('class'))
		
	@url('/')
	def test_footer(self):
		links = [
			[ 'About'							, '{0}/about-us/'.format(URL_BASE)],
			[ 'FAQ'								, '{0}/faq/'.format(URL_BASE)],
			[ 'How To Guides'					, '{0}/how-to/'.format(URL_BASE)],
			[ 'Shift'							, '{0}/wearewhatwedo/'.format(URL_BASE)],
			[ 'Team'							, '{0}/team/'.format(URL_BASE)],
			[ 'Press Centre'					, '{0}/presscentre/'.format(URL_BASE)],
			[ 'Contact'							, '{0}/contact/'.format(URL_BASE)],
			
			[ 'Map'								, '{0}/map/'.format(URL_BASE)],
			[ 'Projects'						, '{0}/projects/'.format(URL_BASE)],
			[ 'Tours and Collections'			, '{0}/curated/'.format(URL_BASE)],
			[ 'Profiles'						, '{0}/channels/'.format(URL_BASE)],
			[ 'Pin'								, '{0}/upload/'.format(URL_BASE)],
			[ 'Mobile App'						, '{0}/app/'.format(URL_BASE)],
			
			[ 'Community'						, '{0}/community/'.format(URL_BASE)],
			[ 'Local Projects'					, '{0}/community/localprojects/'.format(URL_BASE)],
			[ 'Schools'							, '{0}/community/schools/'.format(URL_BASE)],
			[ 'Libraries, Archives and Museums'	, '{0}/community/lams/'.format(URL_BASE)],
			[ 'Support Historypin'				, '{0}/Friends-of-Historypin/'.format(URL_BASE)],
			
			[ 'Blog'							, 'http://blog.historypin.com/' ],
			[ 'Facebook'						, 'http://www.facebook.com/pages/Historypin/192291707448024/' ],
			[ 'Twitter'							, 'http://twitter.com/Historypin/' ],
			[ 'Google+'							, 'https://plus.google.com/116628462065893538180/posts/' ],
			[ 'Newsletter'						, '{0}/newsletter/'.format(URL_BASE)],
			
			[ 'Privacy policy'					, '{0}/privacy-policy/'.format(URL_BASE)],
			[ 'Cookies'							, '{0}/cookies/'.format(URL_BASE)],
			[ 'Terms and Conditions'			, '{0}/terms-and-conditions/'.format(URL_BASE)],
			[ u'\xa9 Shift'						, 'http://www.shiftdesign.org.uk/' ],
		]
		
		elements = self.es('.footer ul a')
		for i in range(len(elements)):
			item = links[i]
			self.assertEqual(item[0], elements[i].text)
			self.assertEqual(item[1], elements[i].get_attribute('href'), 'Wrong link - %s' % (links[i][0]))
