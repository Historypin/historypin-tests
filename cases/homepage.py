from base import *

class Homepage(HPTestCase):
	@classmethod
	def setUpClass(cls):
		cls.browser.get(URL_BASE)
	
	def test_content(self):
		self.assert_title('Historypin | Home')
		
		# check top of the page
		self.assertEqual(self._t('#branding .home-top p'), 'A global community collaborating around history')
		self.assertEqual(self._t('.support .donate'), 'users\nDonate to support Historypin')
		self.assertEqual(self._a('.support .donate', 'href'), URL_BASE + 'friends-of-Historypin')
	
	@unittest.expectedFailure
	def test_header(self):
		self.fail('TBD')
	
	# @unittest.expectedFailure
	def test_footer(self):
		links = [
			[ 'About'							, URL_BASE + 'about-us/' ],
			[ 'FAQ'								, URL_BASE + 'faq/' ],
			[ 'How To Guides'					, URL_BASE + 'how-to/' ],
			[ 'We Are What We Do'				, URL_BASE + 'wearewhatwedo/' ],
			[ 'Team'							, URL_BASE + 'team/' ],
			[ 'Press Centre'					, URL_BASE + 'presscentre/' ],
			[ 'Contact'							, URL_BASE + 'contact/' ],
			
			[ 'Map'								, URL_BASE + 'map/' ],
			[ 'Projects'						, URL_BASE + 'projects/' ],
			[ 'Tours and Collections'			, URL_BASE + 'curated/' ],
			[ 'Channels'						, URL_BASE + 'channels/' ],
			[ 'Pin'								, URL_BASE + 'upload/bridge/' ],
			[ 'Mobile App'						, URL_BASE + 'app/' ],
			
			[ 'Community'						, URL_BASE + 'community/' ],
			[ 'Local Projects'					, URL_BASE + 'community/localprojects/' ],
			[ 'Schools'							, URL_BASE + 'community/schools/' ],
			[ 'Libraries, Archives and Museums'	, URL_BASE + 'community/lams/' ],
			[ 'Support Historypin'				, URL_BASE + 'Friends-of-Historypin/' ],
			
			[ 'Blog'							, 'http://blog.historypin.com' ],
			[ 'Facebook'						, 'http://www.facebook.com/pages/Historypin/192291707448024' ],
			[' Twitter'							, 'http://twitter.com/Historypin' ],
			[ 'Google+'							, 'https://plus.google.com/116628462065893538180/posts' ],
			[ 'Newsletter'						, URL_BASE + 'newsletter' ],
			
			[ 'Privacy policy'					, URL_BASE + 'privacy-policy/' ],
			[ 'Cookies'							, URL_BASE + 'cookies/' ],
			[ 'Terms and Conditions'			, URL_BASE + 'terms-and-conditions/' ],
			[ u'\xa9 We Are What We Do'			, 'http://www.wearewhatwedo.org' ],
		]
		
		elements = self._e('.footer ul a')
		for i in range(len(elements)):
			self.assertEqual(elements[i].text, links[i][0])
			self.assertEqual(elements[i].get_attribute('href'), links[i][1])
	
	@unittest.expectedFailure
	def test_failing(self):
		self.assertEqual(1, 0, 'this is an example of failing test prepared to be developed')