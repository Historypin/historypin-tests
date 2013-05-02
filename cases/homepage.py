from base import *

class Homepage(HPTestCase):
	@url('/')
	def test_icon_touts(self):
		
		features = [
			['ss-cell', '/app/','Download the latest Historypin\nsmartphone app'],
			['ss-trophy', '/presscentre/','We\'ve won a webby award for best charity non-profit website'],
			['ss-user', '/team/','Meet the team working on Historypin around the world'],
		
		]
		
		links 	= self.es('.features a')
		classes = self.es('.features a span')
		
		for n in range(len(features)):
			i = features[n]
			
			self.assertIn('ss-icon', classes[n].get_attribute('class'))
			self.assertIn(i[0], classes[n].get_attribute('class'))
			self.assertEqual(links[n].get_attribute('href'), URL_BASE + i[1])
			self.assertEqual(links[n].text, i[2])
		
	@url('/')
	def test_explore(self):
		
		self.assertEqual(self.e('#search h2').text, 'Explore where you live...')
		
		self.e('#search-location').send_keys("London")
		
		first_suggestion = self.e_wait('.pac-container .pac-item')
		self.assertEqual(first_suggestion.text, 'London, United Kingdom')
		
		first_suggestion.click()
		sleep(.3)
		self.assertEqual(self.browser.current_url.split('#')[0], URL_BASE + '/map/')
	
	@unittest.skip("TODO")
	@url('/')
	def test_featured(self):
		# TODO 
		# - next button
		# - prev button
		# - fullscreen
		# - exit fullscreen
		
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_activity(self):
		# TODO 
		# - counter
		# - expand button
		# - collapse button
		
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_projects(self):
		# TODO 
		# - pages
		self.assertEqual(self.e('#featured-projects .bar a.right').get_attribute('href'), URL_BASE + '/projects/')
		self.assertEqual(self.e('#featured-projects .bar a.right').text, 'Browse all projects')
		
	
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
			self.assertEqual(elements[i].text, links[i][0])
			self.assertEqual(elements[i].get_attribute('href'), links[i][1], 'Wrong link - %s' % (links[i][0]))
	
	@unittest.skip("TODO")
	@url('/')
	def test_cookie_message(self):
		# TODO
		# - text-
		# - link-
		# - close-
		# - refresh 
		#   - the message should not be here anymore
		
		pass
	
	@url('/')
	def test_header(self):
		self.assertTitle('Historypin | Home')
		
		# TODO 
		# - logo image and link
		# - google plus
		# - facebook
		# - twitter
		
		self.assertEqual(self.e('#branding .home-top p').text, 'A global community collaborating around history')
	
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
			self.assertEqual(links[n].get_attribute('href'), i[0])
			self.assertEqual(images[n].get_attribute('src'), URL_BASE + i[1])
		
		support = self.es('.support .donate')
		self.assertEqual(support[0].text, 'users\nDonate to support Historypin')
		self.assertEqual(support[0].get_attribute('href'), URL_BASE + '/friends-of-Historypin')
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
			self.assertEqual(elements[i].text, links[i][0])
			self.assertEqual(elements[i].get_attribute('href'), links[i][1], 'Wrong link - %s' % (links[i][0]))