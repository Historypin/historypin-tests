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
		toc = {
			'heading': 'General',
			'items': [
				['#title1', 'What is Historypin?'],
				['#title2', 'Why was Historypin created?'],
				['#title3', 'What are Historypin\'s long-term aims?'],
				['#title4', 'Who is behind Historypin?'],
				['#title5', 'What has happened during the beta phase of Historypin?'],
			],
			'heading': 'Using the site',
			'items': [
				['#title6', 'What kind of content can I add to Historypin?'],
				['#title7', 'How do I pin photographic images?'],
				['#title8', 'How do I pin video content?'],
				['#title9', 'How do I pin audio content?'],
				['#title10', 'How do I add stories and recollections?'],
				['#title116', 'How do I edit a piece of content that I have pinned?'],
				['#title117', 'How do I delete a piece of content that I have pinned?'],
				['#title11', 'Why can\'t I "pin" stories to the map on their own?'],
				['#title12', 'What about other types of materials, like letters, diaries or records?'],
				['#title13', 'How can I pin very large amounts of content?'],
				['#title14', 'If there is content already there, can I pin more on that spot?'],
				['#title15', 'Can content still be pinned if I don\'t know the date?'],
				['#title16', 'Can I link content I\'ve pinned to more info on my website or blog?'],
				['#title17', 'How do I find the content I\'ve uploaded when I come back to the site?'],
				['#title18', 'Why does your time filter only go back to 1840?'],
				['#title19', 'What is Street View and why doesn\'t it exist all over the world?'],
				['#title20', 'What are Tours?'],
				['#title21', 'What are Collections?'],
				['#title22', 'I\'ve found content that is inaccurately pinned, what should I do?'],
				['#title23', 'I\'ve found inappropriate content, what should I do?'],
				['#title24', 'I\'ve found content that infringes my copyright, what should I do?'],
				['#title25', 'How are you moderating what goes on the site?'],
				['#title112', 'Historypin is not functioning or displaying as I would expect, what should I do?'],
				['#title113', 'I am having trouble uploading photos, what should I do?'],
				['#title114', 'How do I change my Username?'],
			],
			'heading': 'Bulk Uploader',
			'items': [
				['#title99', 'How can I find out more about doing a bulk upload?'],
				['#title100', 'Do I have to pay to use the bulk uploader?'],
				['#title101', 'Is there a limited number of bulk uploads that I can do?'],
				['#title102', 'Is there a limit to how many images I can upload in a single bulk upload?'],
				['#title103', 'Can I edit my data once I have completed a bulk upload?'],
				['#title104', 'Can I make multiple edits to my content?'],
				['#title105', 'Can I make global changes to the data attached to my photos?'],
				['#title106', 'Can I delete a bulk upload?'],
				['#title107', 'Do I need to complete all the fields for my bulk upload to work?'],
				['#title108', 'Why haven\'t the fields on my bulk upload populated with meta-data?'],
				['#title109', 'Why am I getting \'Bad Request\'?'],
				['#title110', 'Why am I getting \'Internal server error\'?'],
				['#title111', 'I used the Bulk Uploader, but the content on my Channel is \'unpinned\''],
			],
			'heading': 'Getting involved',
			'items': [
				['#title27', 'How can I get more involved personally?'],
				['#title28', 'Can I volunteer with Historypin?'],
				['#title29', 'How can I get my local school more involved?'],
				['#title31', 'How can I use Historypin in my local area?'],
				['#title32', 'Do you give talks or run events?'],
				['#title33', 'Do you offer any training?'],
			],
			'heading': 'Partners',
			'items': [
				['#title34', 'Who are Historypin\'s existing partners?'],
				['#title35', 'What does your partnership with Google involve?'],
				['#title36', 'How can library, archive or museums get involved?'],
				['#title37', 'How can schools get involved?'],
				['#title38', 'How can universities and academic institutions get involved?'],
				['#title39', 'How can community organisations, historical associations or photography societies get more involved?'],
				['#title40', 'I\'d like to talk about partnering with Historypin, who can I contact?'],
			],
			'heading': 'Data',
			'items': [
				['#title41', 'Where is the content stored?'],
				['#title42', 'Is there any limit to the amount of content that can go on the site?'],
				['#title43', 'How can I help improve data on Historypin?'],
				['#title44', 'Is data shared with other parties?'],
			],
			'heading': 'Integration with other platforms',
			'items': [
				['#title45', 'Can I embed Historypin tools on my site?'],
				['#title46', 'Does Historypin have an API?'],
				['#title47', 'Can I get statistics on my content?,'],
			],
			'heading': 'Copyright and use of content',
			'items': [
				['#title49', 'How will the content be protected?'],
				['#title50', 'How will my content be credited on the site?'],
				['#title51', 'What can other users do with my content?'],
				['#title52', 'What can Historypin do with my content?'],
			],
			'heading': 'Privacy',
			'items': [
				['#title53', 'Do you share my user information with anyone?'],
			],
			'heading': 'App',
			'items': [
				['#title54', 'What can the Historypin app do?'],
				['#title55', 'How do I get the Historypin app?'],
				['#title115', 'Why does the Historypin app require my Google Account details?'],
			],
			'heading': 'Funding',
			'items': [
				['#title56', 'How is Historypin funded?'],
				['#title57', 'What happens to the profits from Historypin?'],
				['#title58', 'How can I donate to Historypin?'],
			],
			'heading': 'Future Plans',
			'items': [
				['#title59', 'What\'s next for Historypin?'],
				['#title60', 'What\'s next for We Are What We Do?'],
			],
			'heading': 'Contact',
			'items': [
				['#title61','I\'m a journalist and want to write a fabulously complimentary article about you. What do I do?'],
				['#title62','I\'ve got another question, what should I do?'],
			],
		}
 
		pass
	

	@url('/presscentre/')
	def test_press_center(self):
		
		self.assertTitle('Historypin | Press Centre')
		self.assertEqual(self.e('h1.title').text, 'Press Centre')

		#TODO
		# LATER asert all p
		# - texts
		# - a [href]
		
		sel = '.sidebar .inner:nth-child(1) '
		self.assertEqual(self.e(sel + 'h3').text, 'Contact Details')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'UK & Global\nRebekkah Abraham\nrebekkah.abraham@wearewhatwedo.org\n+44 (0)20 7148 7666')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
		self.assertEqual(self.e(sel + 'p:nth-child(3)').text, 'US\nJon Voss\njon.voss@wearewhatwedo.org\n+1 415 935 4701')
		self.assertEqual(self.e(sel + 'p:nth-child(3) a').get_attribute('href'), 'mailto:jon.voss@wearewhatwedo.org')

		sel = '.sidebar .inner:nth-child(2) '
		self.assertEqual(self.e(sel + 'h3').text, 'Awards')
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://www.webbyawards.com/webbys/current.php?season=15#webby_entry_charitable_organizations_non-profit')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/webby_pink.png')
		self.assertEqual(self.e(sel + 'p:nth-child(3) a').get_attribute('href'), 'http://www.webbyawards.com/webbys/current.php?season=15#webby_entry_charitable_organizations_non-profit')
		self.assertEqual(self.e(sel + 'p:nth-child(3)').text, 'Webby for Best Charitable Organisation/Not-for-Profit Website')

		sel = '.sidebar .inner:nth-child(3) '	
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://thetim.es/y1vL3P')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/sundaytimes500.png')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://thetim.es/y1vL3P')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Sunday Times The App List 2012.')	

		sel = '.sidebar .inner:nth-child(4) '	
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://lovieawards.eu/winners/')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/lovie_pink.png')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://lovieawards.eu/winners/')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Lovie Award for Best Education & Reference Website')

		sel = '.sidebar .inner:nth-child(5) '	
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://www.ala.org/aasl/guidelinesandstandards/bestlist/bestwebsitestop25')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/aasl.jpg')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://www.ala.org/aasl/guidelinesandstandards/bestlist/bestwebsitestop25')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'American Association of School Librarians 2012 Best Website for Teaching and Learning')

		sel = '.sidebar .inner:nth-child(6) '	
		self.assertEqual(self.e(sel + 'a:nth-child(1)').get_attribute('href'), 'http://www.familytreemagazine.com/article/best-old-map-and-photo-websites-for-genealogy-2012')
		self.assertEqual(self.e(sel + 'img:nth-child(1)').get_attribute('src'), URL_BASE + '/resources/images/presscenter/101-best-genealogy-websites-2012.jpg')
		self.assertEqual(self.e(sel + 'p:nth-child(2) a').get_attribute('href'), 'http://www.familytreemagazine.com/article/best-old-map-and-photo-websites-for-genealogy-2012')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Family Tree Magazine: 101 best family history websites')	
	
		sel = '.sidebar .inner:nth-child(7) '
		self.assertEqual(self.e(sel + 'h3').text, 'Press Pack')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://wawwd-resources.s3.amazonaws.com/presspacks/Historypin.zip')
		self.assertEqual(self.e(sel + 'p').text, u'Download press releases, pictures and all the info you\u2019ll need to write a fabulously complimentary article about us.')
		
	
	
	@url('/privacy-policy/')
	def test_privacy_policy(self):
		self.assertTitle('Historypin | Privacy Policy')
		self.assertEqual(self.e('#site-content h1').text, 'Privacy Policy')

		# TODO Test all headings
	
	@url('/Friends-of-Historypin/')
	def test_support(self):
		# TODO fix this is the code and change the testcase
		# self.assertTitle('Historypin | Friends of Historypin')
		self.assertTitle('Historypin | Community | Partners')
		self.assertEqual(self.e('h2').text, 'What does the Foundation do?')
		
		sel = '.section '
		self.assertEqual(self.e(sel + 'img').get_attribute('src'), URL_BASE + '/resources/images/home/friends_of_Historypin.png')
		self.assertEqual(self.e(sel + 'p:nth-child(8) img').get_attribute('src'), URL_BASE + '/resources/images/home/friendsOfPhoto01.jpg')
		self.assertEqual(self.e(sel + 'p:nth-child(9) img').get_attribute('src'), URL_BASE + '/resources/images/home/friendsOfPhoto02.jpg')
		
		sel = '.sidebar .inner:nth-child(1) '
		self.assertEqual(self.e(sel + 'h3').text, 'Support Us')
		self.assertEqual(self.e(sel + 'p:nth-child(2)').text, 'Your donation to the We Are What We Do Charitable Foundation will go a long way in helping support Historypin Community and Education Programmes.')
		self.assertEqual(self.e(sel + 'p:nth-child(3)').text, 'Registered Charity Number\n1134546')
		self.assertEqual(self.e(sel + 'a').get_attribute('href'), 'http://www.charitygiving.co.uk/donate/donate_b.asp?charityid=5366')
		self.assertEqual(self.e(sel + 'a span').text, 'Donate')

		sel = '.sidebar .inner:nth-child(2) '
		self.assertEqual(self.e(sel + 'h3').text, 'Find out more')
		self.assertEqual(self.e(sel + 'h3 a').get_attribute('href'), URL_BASE + '/HistorypinCommunityandEducationProgrammes')
		self.assertEqual(self.e(sel + 'p').text, 'Read more about the aims of the Historypin Community and Education Programmes.')

		sel = '.sidebar .inner:nth-child(3) '
		self.assertEqual(self.e(sel + 'h3').text, 'Contact us')
		self.assertEqual(self.e(sel + 'p').text, 'To find out more, please contact ella.wiggans@wearewhatwedo.org')
		self.assertEqual(self.e(sel + 'p a').get_attribute('href'), 'mailto:ella.wiggans@wearewhatwedo.org')

	
	@url('/terms-and-conditions/')
	def test_toc(self):
		self.assertTitle('Historypin | Terms and Conditions')
		self.assertEqual(self.e('.rte h1').text, 'Historypin Terms and Conditions')
		# TODO
		# Terms and Conditions links need to be tested	
	
	@url('/team/')
	def test_team(self):
		self.assertTitle('Historypin | Team')
		self.assertEqual(self.e('#site-content h1').text, 'The Team')

		# LATER
		# - all list items
		# - 2 images
		# - name
		# - title
		# - email text and url

	
	@url('/wearewhatwedo/')
	def test_wawwd(self):
		self.assertTitle('Historypin | We Are What We Do')
		self.assertEqual(self.e('.title').text, 'We Are What We Do')
		
		sel = '.rte p:nth-child(5) a'
		self.assertEqual(self.e(sel).get_attribute('href'), 'http://wearewhatwedo.org/')
		self.assertEqual(self.e(sel).text, 'wearewhatwedo.org')


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
