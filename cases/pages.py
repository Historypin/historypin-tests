from base import *

class Pages(HPTestCase):
	
	@url('/about-us/')
	def test_about(self):
		self.assertTitle('Historypin | A 90 second introduction')
		self.assertEqual(self.e('h1.title').text, 'A 90 second introduction')
		self.assertEqual(self.e('iframe').get_attribute('src'), 'http://www.youtube.com/embed/FdT3eKdto4w?rel=0')
	
	@url('/app/')
	def test_app(self):
		self.assertTitle('Historypin | App')
		self.assertEqual(self.e('h2').text, 'What can you do on the Historypin app?')
		# LATER text after the title 
		
		# Android
		sel = '.appstores .col:nth-child(1) '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/content/app/app_android.png')
		self.assertEqual(self.e(sel + 'h1').text, 'Android')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'https://market.android.com/details?id=com.historypin.Historypin&feature=search_result')
		self.assertEqual(self.e(sel + 'a').text, 'Google Play Store')

		# iPhone
		sel = '.appstores .col:nth-child(2) '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/content/app/app_iphone.png')
		self.assertEqual(self.e(sel + 'h1').text, 'iOS')
		self.assertEqual(self.e(sel + 'a').text, 'iOS App Store')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://itunes.apple.com/app/historypin/id455228207?mt=8')
		
		# Windows Phone 7
		sel = '.appstores .col:nth-child(3) '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/content/app/app_wp7.png')
		self.assertEqual(self.e(sel + 'h1').text, 'Windows Phone 7')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://www.windowsphone.com/en-US/apps/05638072-742e-460c-ab97-18d2b47ef06b')
		self.assertEqual(self.e(sel + 'a').text, 'Windows Phone Marketplace')

	
	@url('/contact/')
	def test_contact(self):
		self.assertTitle('Historypin | Contact')
		self.assertEqual(self.e('.section h1.title').text, 'Contact')

		self.assertEqual(self.e('.section h2:nth-child(2)').text, 'General enquiries, technical enquiries, content enquiries')
		self.assertEqual(self.e('.section p:nth-child(3) a').get_attribute('href'), 'mailto:historypin@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(3)').text, 'historypin@wearewhatwedo.org\n+44 (0)20 7148 7666\n71 St John Street\nLondon\nEC1M 4NJ\nUnited Kingdom')

		self.assertEqual(self.e('.section h2:nth-child(4)').text, 'Media')
		self.assertEqual(self.e('.section p:nth-child(5) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(5)').text, 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670')

		self.assertEqual(self.e('.section h2:nth-child(6)').text, 'Schools, local projects and volunteers')
		self.assertEqual(self.e('.section p:nth-child(7) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(7)').text, 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670')

		self.assertEqual(self.e('.section h2:nth-child(8)').text, 'Library, archive and museum partnerships')
		self.assertEqual(self.e('.section p:nth-child(9) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(9)').text, 'Rebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7670')

		self.assertEqual(self.e('.section h2:nth-child(10)').text, 'Web')
		self.assertEqual(self.e('.section p:nth-child(11) a').get_attribute('href'), 'mailto:mark.frost@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(11)').text, 'Mark Frost\nmark.frost@wearewhatwedo.org\n+44 (0)20 7148 7675')

		self.assertEqual(self.e('.section h2:nth-child(12)').text, 'Corporate Partnerships')
		self.assertEqual(self.e('.section p:nth-child(13) a').get_attribute('href'), 'mailto:nick.stanhope@wearewhatwedo.org')
		self.assertEqual(self.e('.section p:nth-child(13)').text, 'Nick Stanhope\nnick.stanhope@wearewhatwedo.org\n+44 (0)20 7148 7667')
	

	@unittest.skip("TODO")
	@url('/faq/')
	def test_faq(self):
		# TODO LATER
		

		pass
	
	@unittest.skip("TODO")
	@url('/presscentre/')
	def test_press_center(self):
		# TODO
		# - Title - Press centre
		# - heading

		# LATER asert all p
		# - texts
		# - a [href]
		
		# sidebar?
		# - heading
		# - contacts p text 
		# - contacts a [href]

		# all awards
		# - heading
		# - img
		# - img link
		# - text
		# - link

		# press pack
		# - heading
		# - text
		# - link

		pass
	
	@unittest.skip("TODO")
	@url('/privacy-policy/')
	def test_privacy_policy(self):
		# TODO
		# - Title - Privacy Policy
		# - heading

		pass
	
	@unittest.skip("TODO")
	@url('/Friends-of-Historypin/')
	def test_support(self):
		# TODO
		# - Title - Privacy Policy
		# - heading
		# - images present

		# sidebar
		# - support heading
		# - support text
		# - support button text
		# - support button link
		# - find out heading
		# - find out text
		# - contacts heading
		# - contacts text
		# - contacts link

		pass
	
	@unittest.skip("TODO")
	@url('/terms-and-conditions/')
	def test_toc(self):
		# TODO
		# - Title - HP Terms and Conditions
		# - heading

		pass
	
	@unittest.skip("TODO")
	@url('/team/')
	def test_team(self):
		# TODO
		# - Title - The team
		# - heading


		# LATER
		# - all list itmes
		# - 2 images
		# - name
		# - title
		# - email text and url

		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_wawwd(self):
		# TODO
		# - Title - The team
		# - heading
		# - link text and url
		pass

class Community(HPTestCase):
	@unittest.skip("TODO")
	@url('/')
	def test_home(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_home_lams(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_home_projects(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_home_schools(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_how_tos(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_lams_involved(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_lams(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_projects(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_projects_studies(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_topics_to_explore(self):
		pass

class CommunitySchools(HPTestCase):
	'''
	Community - Schools
	Community - Schools - Case Studies
	Community - Schools - Case Studies - EIC
	Community - Schools - How To Guides
	Community - Schools - Resources
	Community - Schools - Case Studies - Billericay, Essex, UK
	Community - Schools - Case Studies - Cromer, Norfolk, UK
	Community - Schools - Case Studies - Nelson
	Community - Schools - Case Studies - Newport Primary School, Essex, UK
	'''
	
	
	
	pass
