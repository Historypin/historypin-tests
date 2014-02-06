# -*- coding: utf-8 -*-

from base import *

class Homepage(HPTestCase):
	@url('/')
	def test_cookie_message(self):
		self.assertEqual(
			'We want you to enjoy your visit to our website. That\'s why we use cookies to enhance your experience.\nBy staying on our website you agree to our use of cookies. Find out more about the cookies we use.',
			self.e('.cookies-popup p').text,
		)
		
		self.assertEqual('%s/cookies/' % URL_BASE, self.e('.cookies-popup p a').get_attribute('href'))
		a = self.e('.cookies-popup a.right')
		self.assertEqual('Close this message  close', a.text)
		a.click()
		
		self.browser.refresh()
		self.assertRaises(NoSuchElementException, self.e, '.cookies-popup')
	
	@url('/')
	def test_navigation(self):
		
		links = [
			[ 'Home'					, '%s/' % URL_BASE ],
			[ 'Map'						, '%s/map/' % URL_BASE ],
			[ 'Projects'				, '%s/projects/' % URL_BASE ],
			[ 'Channels'				, '%s/channels/' % URL_BASE ],
			[ 'Tours and Collections'	, '%s/curated/' % URL_BASE ],
			[ 'Get Involved'			, '%s/community/' % URL_BASE ],
			[ 'Blog'					, 'http://blog.historypin.com/' ],
			[ 'Login'					, '%s/user/' % URL_BASE ],
			[ 'Join'					, '%s/user/' % URL_BASE ],
			[ 'Pin'						, '%s/upload/' % URL_BASE ],
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
		self.assertEqual('%s/'								% URL_BASE, branding.e('a').get_attribute('href'))
		self.assertEqual('%s/resources/images/hp_logo.png'	% URL_BASE, branding.e('img').get_attribute('src'))
		self.assertEqual('A global community collaborating around history VM', self.e('#branding .home-top p').text)
		
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
		featured = self.e('#featured')
		prev	= featured.e('.prev')
		next	= featured.e('.next')
		ul		= featured.e('ul')
		li		= featured.e_wait('li:first-of-type')
		
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
	
	@url('/')
	def test_activity(self):
		
		self.assertGreater(int(self.e('.counter').text.replace(',', '')), 0)
		more = self.e('#activity .more')
		
		more.click()
		sleep(.5)
		# activity_height = self.e('.scrollbarfix').height()
		# self.assertEqual('613.484375px', activity_height)
		
		less = self.e('#activity .less')
		less.click()
		sleep(.5)
		
		# TODO
		# verify if the activity is expaned to check if element has style property with height= 388 and 700px
		# verify if projects are collapsed
	
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
		self.assertEqual(self.browser.current_url.split('#')[0], '%s/map/' % URL_BASE)
	
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
		self.assertEqual('%s/projects/' % URL_BASE	, browse_all.get_attribute('href'))
		self.assertEqual('Browse all projects'		, browse_all.text)
	
	@url('/')
	def test_icon_touts(self):
		
		features = [
			['ss-cell'				, URL_BASE + '/app/'			, 'Download the latest Historypin\nsmartphone app'],
			['ss-trophy'			, URL_BASE + '/presscentre/'	, 'We\'ve won a webby award for best charity non-profit website'],
			['ss-exclamationchat'	, 'http://blog.historypin.com/2013/05/31/weve-updated-our-terms-and-conditions', "We've updated our\nTerms and Conditions"],
		]
		
		icons = self.es('.features span')
		links = self.es('.features a')
		for n in range(len(features)):
			i = features[n]
			
			self.assertIn('ss-icon'				, icons[n].get_attribute('class'))
			self.assertIn(i[0]					, icons[n].get_attribute('class'))
			self.assertEqual(i[1]	, links[n].get_attribute('href'))
			self.assertEqual(i[2]				, links[n].text)
	
	@url('/')
	def test_sponsors(self):
		
		self.assertEqual(self.e('.support h5').text, 'Supported by:')
		
		partners = ['http://www.nominettrust.org.uk/', 'http://www.google.co.uk/intl/en/about/']
		links	= self.es('.partners li a')
		
		for n in range(len(partners)): self.assertEqual(partners[n], links[n].get_attribute('href'))
		
		self.assertIn('data:image/png;base64,iVBORw0KGgoAAAANS'		, links[0].css('background'))
		self.assertIn('data:image/jpeg;base64,/9j'					, links[1].css('background'))
		
		
		support = self.es('.support .donate')
		self.assertEqual('users\nDonate to support Historypin'	, support[0].text)
		self.assertEqual('%s/friends-of-Historypin'	% URL_BASE, support[0].get_attribute('href'))
		self.assertIn('ss-icon', self.e('.support .donate .ss-icon').get_attribute('class'))
		
	@url('/')
	def test_footer(self):
		links = [
			[ 'About'							, '%s/about-us/' % URL_BASE],
			[ 'FAQ'								, '%s/faq/' % URL_BASE],
			[ 'How To Guides'					, '%s/how-to/' % URL_BASE],
			[ 'We Are What We Do'				, '%s/wearewhatwedo/' % URL_BASE],
			[ 'Team'							, '%s/team/' % URL_BASE],
			[ 'Press Centre'					, '%s/presscentre/' % URL_BASE],
			[ 'Contact'							, '%s/contact/' % URL_BASE],
			
			[ 'Map'								, '%s/map/' % URL_BASE],
			[ 'Projects'						, '%s/projects/' % URL_BASE],
			[ 'Tours and Collections'			, '%s/curated/' % URL_BASE],
			[ 'Channels'						, '%s/channels/' % URL_BASE],
			[ 'Pin'								, '%s/upload/' % URL_BASE],
			[ 'Mobile App'						, '%s/app/' % URL_BASE],
			
			[ 'Community'						, '%s/community/' % URL_BASE],
			[ 'Local Projects'					, '%s/community/localprojects/' % URL_BASE],
			[ 'Schools'							, '%s/community/schools/' % URL_BASE],
			[ 'Libraries, Archives and Museums'	, '%s/community/lams/' % URL_BASE],
			[ 'Support Historypin'				, '%s/Friends-of-Historypin/' % URL_BASE],
			
			[ 'Blog'							, 'http://blog.historypin.com/' ],
			[ 'Facebook'						, 'http://www.facebook.com/pages/Historypin/192291707448024/' ],
			[ 'Twitter'							, 'http://twitter.com/Historypin/' ],
			[ 'Google+'							, 'https://plus.google.com/116628462065893538180/posts/' ],
			[ 'Newsletter'						, '%s/newsletter/' % URL_BASE],
			
			[ 'Privacy policy'					, '%s/privacy-policy/' % URL_BASE],
			[ 'Cookies'							, '%s/cookies/' % URL_BASE],
			[ 'Terms and Conditions'			, '%s/terms-and-conditions/' % URL_BASE],
			[ u'\xa9 We Are What We Do'			, 'http://www.wearewhatwedo.org/' ],
		]
		
		elements = self.es('.footer ul a')
		for i in range(len(elements)):
			item = links[i]
			self.assertEqual(item[0], elements[i].text)
			self.assertEqual(item[1], elements[i].get_attribute('href'), 'Wrong link - %s' % (links[i][0]))
