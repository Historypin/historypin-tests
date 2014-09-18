# -*- coding: utf-8 -*-

from base import *
class Community(HPTestCase):
	
	@url('/community/')
	def test_home(self):
		self.assertTitle('Historypin | Community Homepage')
		self.assertEqual('Get Involved', self.e('.info h1').text)
		self.assertEqual('%s/resources/images/channels/channels_home_promo_image.jpg' % URL_BASE, self.e('.main-image').get_attribute('src'))
		self.assertEqual('Welcome to the Historypin community, made up of people, groups and organisations working together to unearth and pin as much history as possible from all over the world - from within archives, in attics, and saved up in wise old heads.', self.e('.info p').text)
		
		mods = [
			['Schools'			, '/community/schools'],
			['Local projects'	, '/community/localprojects'],
			['Libraries, Archives and Museums', '/community/lams'],
		]
		
		links = self.es('.inner.mod a')
		for n in range(len(mods)):
			i = mods[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(URL_BASE + i[1], links[n].get_attribute('href'))
		
		headings = ['Latest News', 'Challenges', 'Get Involved']
		h2s = self.es('.grid h2')
		for n in range(len(headings)):
			self.assertEqual(headings[n], h2s[n].text)
		
		link_images	= '%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/' % PROTOCOL
		
		groups = [
			['Pinning The Queen\'s History', 'What pics and stories do you have of the Queen\'s visits and Jubilee celebrations?'					, 'http://wearewhatwedo.org/queen.jpg', u'View The Queen’s Collection'		, '%s/DiamondJubilee/' % URL_BASE],
			['The Chevy Centenary', u'We’re looking for pics and stories of each of the Chevy models created over the last 100 years.'				, '%schevy_img.png'					% link_images, 'View Chevy Collection'	, '%s/chevy/' % URL_BASE],
			['Life Story Challenge', 'Create a Life Story about someone you know with photos and memories telling the story of their life.'			, '%sicon_life_stories.png'			% link_images, 'View Life Stories Challenge', 'http://www.11492009-gats.historypin.com/en/page/life-stories/'],
			['Google Groups', u'Talk to other users, learn from each other’s experience, plus give us feedback as we experiment with new features.'	, '%sicon_google_groups.png'		% link_images, 'Visit the Group', 'https://groups.google.com/forum/?fromgroups#!forum/historypin'],
			['Meet the team', 'Check out the people working away to bring you Historypin.'															, '%stheteam.jpg'					% link_images, 'Meet the team'			, '%s/team' % URL_BASE],
			['The Foundation', 'Find out about our Charitable Foundation which works on the ground in local communities and education.'				, '%sfriends_of_historypin.jpg'		% link_images, 'Read more'				, '%s/Friends-Of-Historypin/' % URL_BASE],
		]
		
		headings	= self.es('.group ~ .group .col h3')
		paragraphs	= self.es('.group ~ .group .col p')
		images		= self.es('.group ~ .group .col img')
		links		= self.es('.group ~ .group .col a')
		
		for n in range(len(groups)):
			i = groups[n]
			self.assertEqual(i[0], headings[n].text)
			self.assertEqual(i[1], paragraphs[n].text)
			self.assertEqual(i[2], images[n].get_attribute('src'))
			self.assertEqual(i[4], links[2 * n].get_attribute('href'))
			self.assertEqual(i[4], links[2 * n + 1].get_attribute('href'))
			self.assertEqual(i[3], links[2 * n + 1].text)
		
		self.assertEqual(3, len(self.es('.group:nth-of-type(1) .col')))
	
	@url('/community/schools')
	def test_sidebar(self):
		
		link_community = '%s/community' % URL_BASE
		
		sidebar = [
			['Community Homepage'						, link_community, 'Lots of news, ideas, and info for Historypinners round the world'],
			['Schools Homepage'							, '%s/schools'						% link_community, 'Want to run a Historypin session or event in your school?'],
			['Local Projects Homepage'					, '%s/localprojects'				% link_community, 'Want to run a Historypin session or event with your group?'],
			['Libraries, Archives and Museums Homepage'	, '%s/lams'							% link_community, 'Want to get your institution involved?'],
			['Libraries, Archives and Museums Involved'	, '%s/lams-involved'				% link_community, 'Find out the institutions that are already sharing their history on Historypin.'],
			['How To Guides'							, '%s/how-to'						% URL_BASE, 'Downloadable pdfs and videos to explain how to do everything'],
			['Activities & Downloadables for schools'	, '%s/schools-resources'			% link_community, 'Resources to make running sessions and events easier.'],
			['Activities & Downloadables for projects'	, '%s/localprojects-resources'		% link_community, 'Resources to make running sessions and events easier.'],
			['Topics to Explore'						, '%s/topics-to-explore'			% link_community, 'Some of the most interesting photos, Tours and Collections to explore in sessions.'],
			['School Case Studies'						, '%s/schools-case-studies'			% link_community, 'Some examples of schools around the word using Historypin'],
			['Local Project Case Studies'				, '%s/localprojects-case-studies' 	% link_community, 'Some examples of local projects around the world using Historypin'],
			['Support Us'								, '%s/donate/'						% URL_BASE		, u'Donate to Friends of Historypin and you’ll be helping support Historypin Community and Education Programmes.\n\nRegistered Charity Number 1134546'],
			['Blog'										, 'http://blog.historypin.com/'						, 'Find out the latest community, site development, partnership and Challenges news'],
			['Contact'									, '%s/contact-us'					% URL_BASE		, 'For more information contact Rebekkah Abraham, Historypin Content Manager on rebekkah.abraham@wearewhatwedo.org.'],
		]
		
		headings	= self.es('.sidebar .inner h4')
		links		= self.es('.sidebar .inner h4 a')
		paragraphs	= self.es('.sidebar .inner p')
		
		for n in (range(len(sidebar))):
			i = sidebar[n]
			self.assertEqual(i[0], headings[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
			self.assertEqual(i[2], paragraphs[n].text)
			
		self.assertEqual('mailto:rebekkah.abraham@wearewhatwedo.org', self.e('.sidebar .inner p:last-of-type a').get_attribute('href'))
	
	@url('/community/schools')
	def test_home_schools(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual('Schools', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/schools_main.jpg' % PROTOCOL, self.e('.section img').get_attribute('src'))
		
		questions = [
			['Why use Historypin in schools?', '', ''],
			['How can I use it?', '/how-to', 'Have a look at our How to Guides for more help'],
			['How are other schools using it?', '/community/schools-case-studies', 'Have a look at our Case Studies for some ideas'],
			['What are the best things to look at in the classroom?', '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', '/community/schools-resources', 'See our Activities and Downloadables'],
		]
		
		headings = self.es('.section h3')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(i[0], headings[n].text)
			
			if i[1] and i[2]:
				self.assertEqual(URL_BASE + i[1], paragraphs[k].get_attribute('href'))
				self.assertEqual(i[2], paragraphs[k].text)
				
				k += 1
	
	@url('/community/localprojects')
	def test_home_projects(self):
		self.assertTitle('Historypin | Community | Local Projects')
		self.assertEqual('Local Projects', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/localprojects_main.jpg' % PROTOCOL, self.e('.section img').get_attribute('src'))
		
		questions = [
			['Why use Historypin in local projects?', '', ''],
			['How can I use it?', '/how-to', 'Have a look at our How to Guides for more help'],
			['How are other local projects using it?', '/community/localprojects-case-studies', 'Have a look at our Local Projects Case Studies for some ideas'],
			['What are the best things to look at?', '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', '/community/localprojects-resources', 'See our Activites and Downloadables for Local Projects'],
		]
		
		headings = self.es('.section h2')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(i[0], headings[n].text)
			
			if i[1] and i[2]:
				self.assertEqual(URL_BASE + i[1], paragraphs[k].get_attribute('href'))
				self.assertEqual(i[2], paragraphs[k].text)
				
				k += 1
	
	@url('/community/lams')
	def test_home_lams(self):
		self.assertTitle('Historypin | Community | Libraries, Archives & Museums')
		self.assertEqual('Libraries, Archives and Museums homepage', self.e('.right h1').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/lams_main.jpg' % PROTOCOL, self.e('.right img').get_attribute('src'))
		
		headings = self.es('.inner.right h3')
		links	 = self.es('.inner.right h3+p a')
		
		h3s = [
			['Get Started'					, '%s://wawwd-resources.s3.amazonaws.com/Getting%%20Started%%20on%%20Historypin.pdf' % PROTOCOL, 'Getting Started Guide'],
			['Institutions Involved'		, '%s/community/lams-involved' % URL_BASE, u'See what other institutions are already involved and what they’re saying about Historypin.'],
			['10 reasons to get Involved'	, '', ''],
			['Frequently Asked Questions'	, '%s/faq/' % URL_BASE, 'FAQ section'],  # fix link to be with the current version
		]
		
		k = 0
		for n in range(len(h3s)):
			i = h3s[n]
			self.assertEqual(i[0], headings[n].text)
			
			if i[1] and i[2]:
				self.assertEqual(i[1], links[k].get_attribute('href'))
				self.assertEqual(i[2], links[k].text)
				k += 1
		
		faq_section = [
			['q1', u'What does Historypin’s partnership with Google consist of?'],
			['q2', 'Does Historypin take ownership of copyright?'],
			['q3', 'How are my images protected?'],
			['q4', 'How are my images credited?'],
			['q5', 'How can users use my content?'],
			['q6', 'How is Historypin moderated?'],
			['q7', 'How can I do a bulk upload?'],
		]
		
		links_faq 	= self.es('.inner.right ul a')
		h4s			= self.es('.inner.right h4')
		
		for n in range(len(faq_section)):
			i = faq_section[n]
			self.assertEqual(URL_BASE + '/community/lams#' + i[0], links_faq[n].get_attribute('href'))
			self.assertEqual(i[1], links_faq[n].text)
			self.assertEqual(i[0], h4s[n].get_attribute('id'))
			self.assertEqual(i[1], h4s[n].text)
	
	@url('/community/lams-involved')
	def test_lams_involved(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		self.assertEqual('Institutions involved', self.e('.right h1').text)
		self.assertEqual('What Institutions are saying about Historypin', self.e('.right h2').text)
		
		li = self.e('.logos-list li')
		self.assertIsInstance(li, WebElement)
		self.assertIsInstance(li.e('a'), WebElement)
		self.assertIsInstance(li.e('img'), WebElement)
	
	@url('/community/howtos')
	def test_how_tos(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		
		link_resources	= '%s://wawwd-resources.s3.amazonaws.com/historypin/' % PROTOCOL
		youtube_link	= 'https://www.youtube.com/'
		
		how_tos = [
			{
				'heading': 'Exploring',
				'items': [
					['{0}HP_GUIDE_2012_Creating%20an%20account%20and%20logging%20in.pdf'.format(link_resources)	, 'How to create an account and log in'],
					['{0}HP_GUIDE_2012_How%20to%20explore%20Historypin.pdf'.format(link_resources)				, 'How to explore Historypin'],
					['{0}HP_GUIDE_2012_Exploring%20Tours%20and%20Collections.pdf'.format(link_resources)		, 'How to explore Tours and Collections'],
					['{0}watch?v=wTXA1iuB1EA'.format(youtube_link), 'Video: How to navigate the map'],
					['{0}watch?v=GA7g7jjCgpo'.format(youtube_link), 'Video: How to look at content and stories'],
					['{0}watch?v=01cO2pS_iF4'.format(youtube_link), 'Video: How to listen to audio clips'],
					['{0}watch?v=URP0BNfuGY8'.format(youtube_link), 'Video: How to navigate Street View'],
					['{0}watch?v=CFDet-0_BOw'.format(youtube_link), 'Video: How to explore a Collection'],
					['{0}watch?v=uDILtzhWNi0'.format(youtube_link), 'Video: How to explore a Tour'],
				]
			},
			
			{
				'heading': 'Adding',
				'items': [
					['{0}HP_GUIDE_2012_Your%20Channel.pdf'.format(link_resources), 'Your Profile'],
					['{0}HP_GUIDE_2012_Pinning.pdf'.format(link_resources), 'How to pin a photo'],
					['{0}watch?v=7RWb7nw2q6w'.format(youtube_link), 'Video: How to pin a photo'],
					['{0}watch?v=v6THvhAERfo'.format(youtube_link), 'Video: How to pin a photo to Street View'],
					['{0}watch?v=EFrBBC9puSs'.format(youtube_link), 'Video: How to create a Historypin account if you already have a Gmail account'],
					['{0}watch?v=eYt0ZYsXP9M'.format(youtube_link), 'Video: How to create a Historypin account if you have a an email account other than Gmail'],
					['{0}watch?v=UOrnhWvvRpk'.format(youtube_link), 'Video: How to create a Historypin account if you don\'t have an email account'],
					['{0}watch?v=6gJ07pY1qus'.format(youtube_link), 'Video: How to add a story to a photo'],
					['{0}watch?v=NmbVYc8cVwM'.format(youtube_link), 'Video: How to add favourites'],
				]
			},
			
			{
				'heading': 'Curating',
				'items': [
					['{0}HP_GUIDE_2012_Creating%20your%20own%20Collection.pdf'.format(link_resources), 'How to Create a Collection'],
					['{0}HP_GUIDE_2012_Creating%20an%20account%20and%20logging%20in.pdf'.format(link_resources), 'How to Create a Tour'],
					['{0}HP_GUIDE_2012_Exploring%20Tours%20and%20Collections.pdf'.format(link_resources), 'How to explore Tours and Collections'],
					['{0}watch?v=rlF6ehpEAZk'.format(youtube_link), 'Video: How to create a tour'],
					['{0}watch?v=0Fs58oGZPLY'.format(youtube_link), 'Video: How to create a Collection'],
					['{0}HP_GUIDE_2012.pdf'.format(link_resources), 'Complete Historypin Guide'],
				]
			},
		]
		
		headings = self.es('.inner.right h2')
		links = self.es('.inner.right ul a')
		
		k = 0
		for n in range(len(how_tos)):
			i = how_tos[n]
			
			self.assertEqual(i['heading'], headings[n].text)
			
			for item in i['items']:
				self.assertEqual(item[0], links[k].get_attribute('href'))
				self.assertEqual(item[1], links[k].text)
				
				k += 1
	
	@url('/community/localprojects-resources')
	def test_projects_resources(self):
		self.assertTitle('Historypin | Community | Local Projects | Resources')
		self.assertEqual('Activities & Downloads for Local Projects', self.e('.right h1').text)
		self.assertEqual('Downloadable Resources', self.e('.right h2').text)
		
		resources = [
			{
				'heading': 'Activity Sheets',
				'items': [
					['Activity Sheet 1: Recording the story behind a photo'	, 'Worksheet_story%20collections.pdf', 'Blank template for recording info gathered in a interview or session'],
					['Activity Sheet 2: Recording the story behind a photo'	, 'historypin/docs/Activity_Sheet_2_Recording_the_story_behind_a_photo.pdf', 'Worksheet with a series of questions guiding you through interview or session'],
					['Activity Sheet 3: Exploring Historypin'				, 'historypin/docs/Activity_Sheet_3_Exploring_Historypin.pdf', 'Worksheet with series of activities of things to find and do on Historypin'],
				],
			},
			{
				'heading': 'Tip Sheets',
				'items': [
					['Tip Sheet 1: Taking a Photo of a Photo'								, 'historypin/docs/Tip_Sheet_1_Taking_a_Photo_of_a_Photo.pdf', 'All you need to know about taking the perfect photo of a photo - the easy way to digitise old photographs'],
					['Tip Sheet 2: Ideas for local projects'								, 'historypin/docs/Tip_Sheet_2_Ideas_for_local_projects.pdf', 'Ideas and examples of the types of local projects you can run (both online and offline events)'],
					['Tip Sheet 3: Tips on Planning your Historypin Local Project'			, 'historypin/docs/Tip_Sheet_3_Tips_on_Planning_your_Historypin_Local_Project.pdf', 'Tips on how to set up and plan your local project (both online and offline events)'],
					['Tip Sheet 4: Tips on the techie parts of running a session or event'	, 'historypin/docs/Tip_Sheet_4_Tips_on_the_techie_parts_of_running_a_session_or_event.pdf', 'Practical advice if you are running online sessions'],
					['Tip Sheet 5: Tip on Interviewing someone'								, 'historypin/docs/Tip_Sheet_5_Tip_on_Interviewing_someone.pdf', 'Things to think about before and during your conversation, plus ideas for questions'],
					['Historypin Presentation template'										, 'historypin/docs/Historypin_Presentation.ppt', 'Powerpoint presentation to introduce Historypin to your school, group or organisation (includes spare slides for adding info about your session or event)'],
				],
			},
			{
				'heading': 'Posters, flyers and certificates',
				'items': [
					['Poster advertising your event or session'	, 'historypin/docs/Poster_advertising_your_event_or_session.pdf', 'With fillable inable gaps for your details'],
					['Flyer advertising your event or session'	, 'historypin/docs/Flyer_advertising_your_event_or_session.pdf', 'With fillable inable gaps for your details'],
					['Invite announcing your event'				, 'historypin/docs/Invite_announcing_your_event.pdf', 'With fillable inable gaps for your details'],
					['Certificate for participants'				, 'historypin/docs/Certificate_for_participants.pdf', 'For awarding to people for their work discovering and sharing history with fillable inable gaps for your details'],
				],
			},
		]
			
		headings		= self.es('.inner.right h3')
		list_items		= self.es('.inner.right ul li')
		links			= self.es('.inner.right ul a')
		
		k = 0
		for n in range(len(resources)):
			i = resources[n]
			
			self.assertEqual(i['heading'], headings[n].text)
			
			for item in i['items']:
				self.assertEqual(item[0] + '\n' + item[2], list_items[k].text)
				self.assertEqual(PROTOCOL + '://wawwd-resources.s3.amazonaws.com/' + item[1], links[k].get_attribute('href'))
				
				k += 1
	
	@url('/community/localprojects-case-studies')
	def test_projects_studies(self):
		self.assertTitle('Historypin | Community | Local Projects Case Studies')
		self.assertEqual('Local Projects Case Studies', self.e('.right h1').text)
		
		studies = [
			['Magic Me, Tower Hamlets, London, UK'	, 'localprojects-case-study-magicme'		, '4c_thumb.jpg', u'A set of inter-generational workshop sessions held at the Sundial Community Centre and in the streets around the area, run in partnership with the UK’s leading provider of intergenerational arts activities.'],
			['Reading, Berkshire, UK'				, 'localprojects-case-study-reading'		, '4a_thumb.jpg', 'A huge community project involving Reading Museum, local schools, care homes, community groups and societies, mapping the history of an entire town.'],
			['San Francisco, USA'					, 'localprojects-case-study-sanfrancisco'	, '4e_thumb.jpg', 'A special exhibition of photos from the San Francisco Transit Authority Archive at the Market Street Railway Museum and bus shelters around the city, allowing for amazing real-life then-and-now comparisons.'],
			['Lighthouse, Brighton, UK'				, 'localprojects-case-study-lighthouse'		, '4b_thumb.jpg', 'An inter-generational project bringing together school students and older residents of Brighton alive during World War 2. Films, an exhibition and Collections on Historypin were created.'],
		]
		
		grid			= self.e('.grid')
		headings		= grid.es('h3 a')
		image_links		= grid.es('.inner > a')
		images			= grid.es('img')
		paragraphs		= grid.es('p')
		
		for n in range(len(studies)):
			i = studies[n]
			self.assertEqual(i[0], headings[n].text)
			self.assertEqual(URL_BASE + '/community/' + i[1], headings[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/community/' + i[1], image_links[n].get_attribute('href'))
			self.assertEqual(PROTOCOL + '://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/' + i[2], images[n].get_attribute('src'))
			self.assertEqual(i[3], paragraphs[n].text)
		
	@url('/community/localprojects-case-study-magicme')
	def test_projects_studies_magicme(self):
		self.assertTitle('Historypin | Community | Local Projects | Magic Me, Tower Hamlets, London, UK')
		self.assertEqual('Magic Me, Tower Hamlets, London, UK', self.e('h1.title').text)
		
		link_imgs = '%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/' % PROTOCOL
		imgs = self.es('.section img')
		
		self.assertEqual('{0}4c_main.jpg'.format(link_imgs)	, imgs[0].get_attribute('src'))
		self.assertEqual('{0}4c_sec.jpg'.format(link_imgs)	, imgs[1].get_attribute('src'))
		self.assertEqual('%s/channels/view/6932562/name/magicme/' % URL_BASE, self.e('.section a').get_attribute('href'))
	
	@url('/community/localprojects-case-study-reading')
	def test_projects_studies_reading(self):
		self.assertTitle('Historypin | Community | Local Projects | Reading, Berkshire, UK')
		self.assertEqual('Reading, Berkshire, UK', self.e('h1.title').text)
		
		link_imgs = '%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/' % PROTOCOL
		imgs = self.es('.section img')
		headings = self.es('.section h3')
		
		self.assertEqual('{0}4a_main.jpg'.format(link_imgs)	, imgs[0].get_attribute('src'))
		self.assertEqual('{0}4a_sec.jpg'.format(link_imgs)	, imgs[1].get_attribute('src'))
		self.assertEqual('%s/community/localprojects-reading/' % URL_BASE, self.e('.section p:nth-of-type(8) a').get_attribute('href'))
		self.assertEqual('What people had to say about it'	, headings[0].text)
		self.assertEqual('What was the impact?'				, headings[1].text)
		self.assertEqual('%s/resources/images/reading_evaluation_infographic.jpg' % URL_BASE			, self.e('.section h3~a').get_attribute('href'))
		self.assertEqual('%s/resources/images/reading_evaluation_infographic_thumb.jpg' % URL_BASE		, self.e('.section a img').get_attribute('src'))
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/Reading_Evaluation%%20Report_Small.pdf' % PROTOCOL, self.e('.section h3~p a:nth-of-type(1)').get_attribute('href'))

	@url('/community/localprojects-reading/')
	def test_community_localprojects_reading(self):
		self.assertTitle('Historypin | Community | Local Projects | Reading')
		self.assertEqual('Reading, UK', self.e('h1.title').text)
		
		headings = self.es('.section h2')
		h2s = [
			u'Pinning Reading’s History',
			'Brilliant Pinners in Reading',
			'Take a Tour round Reading',
			'Great stories and pics pinned in Reading',
			u'See what’s been pinned in Reading',
		]
		
		for n in range(len(h2s)):
			i = h2s[n]
			self.assertEqual(i, headings[n].text)
		
		pinners = [
			['small_1.jpg', '6604879/', 'RG Community'],
			['small_2.jpg', '7012010/', 'Museum of English Rural Life'],
			['small_3.jpg', '6160003/', 'Giles Knapp'],
			['small_4.jpg', '1892068/', 'Reading Museum'],
			['small_5.jpg', '1968007/', 'Malcolm'],
			['small_8.jpg', '5787040/', 'Sitevolunteer'],
		]
		
		pinner_images	= self.es('.col.w2:nth-of-type(1) ul img')
		pinner_links	= self.es('.col.w2:nth-of-type(1) ul a')
		for n in range(len(pinners)):
			i = pinners[n]
			self.assertEqual(URL_BASE + '/resources/images/content/community/reading/' + i[0], pinner_images[n].get_attribute('src'))
			self.assertEqual(URL_BASE + '/channels/view/' + i[1], pinner_links[n].get_attribute('href'))
			self.assertEqual(i[2], pinner_links[n].text)
		
		
		self.assertEqual('{0}/resources/images/content/community/reading/take_a_tour.jpg'.format(URL_BASE)	, self.e('.col.w2:nth-of-type(2) img').get_attribute('src'))
		
		button = self.e('.col.w2:nth-of-type(2) a.button')
		
		self.assertEqual('{0}/tours/view/id/6917547/title/Snapshots%20of%20Reading'.format(URL_BASE)		, button.get_attribute('href'))
		self.assertEqual('Take the Tour', button.text)
		
		pins = [
			['medium_1.jpg', 'geo:51.465794,-0.966198/zoom:15/dialog:1834055/tab:details/'		, 'Floods in Gosbrook Road, Caversham - April 1947'],
			['medium_2.jpg', 'geo:51.455863,-0.990668/zoom:15/dialog:1228008/tab:streetview/'	, 'Traffic on Oxford Road, 1893'],
			['medium_3.jpg', 'geo:51.445213,-1.000692/zoom:15/dialog:5845061/tab:details/'		, 'Silver Jubilee Street Party Vine Crescent Reading, 1977'],
			['medium_4.jpg', 'geo:51.456665,-0.970927/zoom:16/dialog:6610677/tab:streetview/'	, 'Town Hall, Reading,1900'],
			['medium_5.jpg', 'geo:51.44799,-1.023132/zoom:16/dialog:5841163/tab:details/'		, 'Cast of Play in Garden of St. Michael\'s Rectory, 1951 - 1953'],
			['medium_6.jpg', 'geo:51.472803,-0.96989/zoom:14/dialog:6931485/tab:details/'		, 'Bernard Tripp at Bugs Bottom, 1943'],
		]
		
		pin_images	= self.es('.cf img')
		pin_links	= self.es('.cf a')
		for n in range(len(pins)):
			i = pins[n]
			self.assertEqual(URL_BASE + '/resources/images/content/community/reading/' + i[0], pin_images[n].get_attribute('src'))
			self.assertEqual(URL_BASE + '/map/#/' + i[1], pin_links[n].get_attribute('href'))
			self.assertEqual(i[2], pin_links[n].text)
		
		link_imgs = URL_BASE + '/resources/images/'
		images = self.es('h2:last-of-type ~ img')
		self.assertEqual('{0}content/community/reading/pined_on_a_map.jpg'.format(link_imgs), images[0].get_attribute('src'))
		self.assertEqual('{0}hlf_web.jpg'.format(link_imgs), images[1].get_attribute('src'))
		self.assertEqual('{0}gul_web.jpg'.format(link_imgs), images[2].get_attribute('src'))
		
	@url('/community/localprojects-case-study-sanfrancisco')
	def test_projects_studies_sanfrancisco(self):
		self.assertTitle('Historypin | Community | Local Projects | San Francisco, USA')
		self.assertEqual('San Francisco, USA', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4d_main.jpg' % PROTOCOL, self.e('.section img').get_attribute('src'))
		self.assertEqual('{0}/sfmta'.format(URL_BASE), self.e('.section p:nth-of-type(6) a').get_attribute('href'))
		self.assertEqual('SFMTA collection on Historypin', self.e('.section p:nth-of-type(6) a').text)
	
	@url('/community/localprojects-case-study-lighthouse')
	def test_projects_studies_lighthouse(self):
		self.assertTitle('Historypin | Community | Local Projects | Lighthouse, Brighton, UK')
		self.assertEqual('Lighthouse, Brighton, UK', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4b_main.jpg' % PROTOCOL, self.e('.section p img').get_attribute('src'))
	
	@url('/community/topics-to-explore')
	def test_topics_to_explore(self):
		self.assertTitle('Historypin | Community | Topics to Explore')
		self.assertEqual('Topics to Explore', self.e('.right h1').text)
		
		collections = '/collections/view/id/'
		tours = '/tours/view/id/'
		
		thumb_url = '/services/thumb/phid/%d/dim/142x100/crop/1/quality/90'
		thumbs = '/services/thumb/phid/'
		
		topics = [
			{
				'heading': 'Collections',
				'items': [
					['The 1906 San Francisco Earthquake'			, '{0}73/title/The%201906%20San%20Francisco%20Earthqauke'.format(collections)					, thumb_url % 16478	, 'This Collection of photos of San Francisco after the 1906 earthquake and fire gathers photos around a historical event.'],
					['The Facial Hair Through Time Collection'		, '{0}21/title/The%20Facial%20Hair%20Through%20Time%20Collection'.format(collections)			, thumb_url % 9118	, 'This Collection of facial hair from different times and places around the world gathers photos around a particular theme.'],
					['Fabulous Fashion'								, '{0}41/title/Fabulous%20Fashion'.format(collections)											, thumb_url % 21108	, 'This Collection illustrates change over time through photos of fashionable outfits arranged in chronological order.'],
					['Codford Army Camps, Wiltshire, May-June 1919'	, '{0}873/title/Codford%20Army%20Camps,%20Wiltshire,%20May-June%201919'.format(collections)		, thumb_url % 48648	, u'This Collection is of family photos taken by the user’s relative who was in the army and took photos during his postings in the 1919.'],
					['University of Florida Homecoming'				, '{0}480/title/University%20of%20Florida%20Homecoming'.format(collections)						, thumb_url % 36304	, 'This Collection of Homecoming celebrations at the University of Florida gathers photos of an annual event through the years.'],
					['Sport in Reading'								, '{0}559/title/Sport'.format(collections)														, thumb_url % 27152	, 'This Collection was created by a class of 13 year old students who collected photos around the theme of sporting events in their local area.'],
				],
			},
			{
				'heading': 'Tours',
				'items': [
					['New York Immigration'						, '{0}144/title/New%20York%20Immigration'.format(tours)												, thumb_url % 11169	, 'This Tour explores a historical theme and illustrates 19th century immigration to the US with a snapshot of immigrant life in 19th century NYC.'],
					['World War Two'							, '{0}7/title/World%20War%20Two'.format(tours)														, thumb_url % 546	, 'This Tour narrates a historical event and uses photos and audio clips to highlight key events during WWII from 1939-1945.'],
					[u'Tour of Hackney’s Past and Present'		, '{0}705/title/Key%20Stage%20One%20Tour%20of%20Hackney%27s%20Past%20and%20Present'.format(tours)	, thumb_url % 52247	, 'This Tour was created by a teacher and asks questions about historical photos of Hackney, London.'],
					['Queen Elizabeth II'						, '{0}4/title/Queen%20Elizabeth%20II'.format(tours)													, thumb_url % 891	, u'This Tour narrates the biography or a person by highlighting key events of Queen Elizabeth II’s life.'],
					['A historical guided tour of Kew Gardens'	, '{0}19/title/A%20historical%20guided%20tour%20of%20Kew%20Gardens'.format(tours)					, thumb_url % 8374	, 'This Tour takes you on a historical walking Tour around Royal Botanical Gardens at Kew, UK.'],
					['The Grand Tour'							, '{0}77/title/The%20Grand%20Tour'.format(tours)													, thumb_url % 13374	, 'This Tour illustrates a famous route using historical photos.'],
				],
			},
			{
				'heading': 'Photos, Videos and Audio clips',
				'items': [
					[u'Occupy London camp in front of St Paul’s Cathedral, 16 October 2011'		, '/photos/#/geo:51.513745,-0.100594/zoom:15/dialog:42537/tab:stories_tab_content/'													, '{0}42537/dim/142x100/crop/1/quality/90'.format(thumbs), u'This photo captures a modern moment of history, showing the protest occupying St Paul’s Church Yard, London in October 2011.'],
					['Earthquake damage, 25 February 2011'										, '/photos/#/geo:-43.507721,172.729543/zoom:10/sv:24391/heading:-171.09375/pitch:-0.75000/sv_zoom:1.00000/'					, '{0}24391/dim/142x100/crop/1/quality/90'.format(thumbs), 'This photo, overlaid on Street View, shows buildings damaged by the earthquake in Christchurch, New Zealand in February 2011, illustrating the damage done by natural disasters.'],
					['Damage on Piccadilly, 1940 - 1942'										, '/map/#!/geo:51.509108,-0.136672/zoom:20/dialog:60440/tab:stories_tab_content/'													, '{0}60440/dim/142x100/quality/90'.format(thumbs), 'This video clip illustrates bomb damage to Picadilly, London in the early 1940s.'],
					[u'JFK’s Inaugural Speech, 20th January 1961'								, '/map/#!/geo:38.891454,-77.01214/zoom:15/dialog:23468/tab:stories_tab_content/'											, '{0}23468/dim/142x100/quality/90'.format(thumbs), u'This audio clip plays an extract from John F Kennedy’s inaugural speech in 1961.'],
					['Historypin Repeats'														, '/channels/view/571038/', '/channels/img/571038/logo/1/dim/142x100/crop/1/', 'This Profile has got some great Historypin Repeats - modern replicas of historical photos on Historypin, taken by people using the smartphone app.'],
					['Joe Voss, Jefferson Memorial, 1948 - 1952'								, '/photos/#/geo:38.889263,-77.05008/zoom:15/dialog:33892/tab:more_tab_content/'		, '{0}33892/dim/142x100/crop/1/quality/90'.format(thumbs), 'This photo shows a Historypin Repeat. This Historypinner has pinned a photo of his Dad at Jefferson Memorial, Washington DC in the 1950s and used the Historypin app to take a photo of himself in the same spot in 2011.'],
				],
			}
		]
		
		grid				= self.e('.grid')
		headings 			= grid.es('h2')
		subheadings 		= grid.es('h3 a')
		links 				= grid.es('.inner > a')
		images 				= grid.es('img')
		paragraphs 			= grid.es('p')
		
		k = 0
		for n in range(len(topics)):
			i = topics[n]
			
			self.assertEqual(i['heading'], headings[n].text)
			
			for item in i['items']:
				self.assertEqual(item[0], subheadings[k].text)
				self.assertEqual(URL_BASE + item[1], subheadings[k].get_attribute('href'))
				self.assertEqual(URL_BASE + item[1], links[k].get_attribute('href'))
				self.assertEqual(URL_BASE + item[2], images[k].get_attribute('src'))
				self.assertEqual(item[3], paragraphs[k].text)
				
				k += 1
	
	@url('/community/schools-case-studies/')
	def test_schools_studies(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual('Schools Case Studies', self.e('.right h1').text)
		
		studies = [
			['English International College, Marbella, Spain'	, 'schools-eic'			, '6b_thumb.jpg', 'Historypin is used as the theme for Humanities Day and students create an exhibition after parents and locals invited in for Historypin coffee morning.'],
			['Nelson Rural School, New Brunswick, Canada'		, 'schools-nelson'		, '6c_thumb.jpg', 'Students become local historians and archivists, going out into the community to find owners of old photographs and conduct interviews, recording it all on Historypin.'],
			['Billericay, Essex, UK'							, 'schools-billericay'	, '6d_thumb.jpg', '12-13 year old boys plan their own workshop where they meet with 12 senior citizens from the local area.'],
			['Cromer, Norfolk, UK'								, 'schools-cromer'		, '6e_thumb.jpg', 'History students assist at event in community centre where local residents are invited to bring along and upload their old photos and memories of Cromer.'],
			['Newport Primary School, Essex, UK'				, 'schools-newport'		, '6f_thumb.jpg', '9-11 years olds take part in offline activities around photographs and stories, then hold event where older people from local care homes and neighbourhoods share their histories.'],
		]
		
		grid			= self.e('.grid')
		headings		= grid.es('h3 a')
		images			= grid.es('img')
		image_links		= grid.es('.inner > a')
		paragraphs		= grid.es('p')
		
		for n in range(len(studies)):
			i = studies[n]
			self.assertEqual(i[0], headings[n].text)
			self.assertEqual(URL_BASE + '/community/' + i[1], headings[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/community/' + i[1], image_links[n].get_attribute('href'))
			self.assertEqual(PROTOCOL + '://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/' + i[2], images[n].get_attribute('src'))
			self.assertEqual(i[3], paragraphs[n].text)
		
	@url('/community/schools-eic/')
	def test_schools_studies_eic(self):
		self.assertTitle('Historypin | Community | Schools | English International College, Marbella, Spain')
		self.assertEqual('English International College, Marbella, Spain', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_main.jpg' % PROTOCOL, self.e('.section p img').get_attribute('src'))
		self.assertEqual('Amy, Year 9', self.e('h2:nth-of-type(1)').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_fav1.jpg' % PROTOCOL, self.e('.section p:nth-of-type(10) img').get_attribute('src'))
		
	@url('/community/schools-billericay/')
	def test_schools_studies_bill(self):
		self.assertTitle('Historypin | Community | Schools | Billericay School, Essex, UK')
		self.assertEqual('Billericay School, Essex, UK', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_main.jpg' % PROTOCOL, self.e('.section p:nth-of-type(1) img').get_attribute('src'))
		self.assertEqual('http://billericayschool.net/speakup/2011/06/pinning-down-history/', self.e('.section p:nth-of-type(12) a').get_attribute('href'))
		self.assertEqual('Read more about the project on their blog.', self.e('.section p:nth-of-type(12) a').text)
		self.assertEqual('Video made by Billericay School for the day', self.e('h3:nth-of-type(1)').text)
		self.assertEqual('Feature on Radio Essex about the Billericay Historypin project', self.e('h3:nth-of-type(2)').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_sec.jpg' % PROTOCOL, self.e('.section p:nth-of-type(14) img').get_attribute('src'))
	
	@url('/community/schools-cromer/')
	def test_schools_studies_cromer(self):
		self.assertTitle('Historypin | Community | Schools | Cromer, Norfolk, UK')
		self.assertEqual('Cromer, Norfolk, UK', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6e_main.jpg' % PROTOCOL, self.e('.section p:nth-of-type(1) img').get_attribute('src'))
	
	@url('/community/schools-nelson/')
	def test_schools_studies_nelson(self):
		self.assertTitle('Historypin | Community | Schools | Nelson Rural School, New Brunswick, Canada')
		self.assertEqual('Nelson Rural School, New Brunswick, Canada', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6c_main.jpg' % PROTOCOL, self.e('.section img').get_attribute('src'))
		self.assertEqual('%s/channels/view/8817007/name/nelsonrural7k/' % URL_BASE, self.e('.section p:nth-of-type(8) a').get_attribute('href'))
		self.assertEqual(u'Nelson School’s Historypin Profile', self.e('.section p:nth-of-type(8) a').text)
		
	@url('/community/schools-newport/')
	def test_schools_studies_newport(self):
		self.assertTitle('Historypin | Community | Schools | Newport Primary School, Essex, UK')
		self.assertEqual('Newport Primary School, Essex, UK', self.e('h1.title').text)
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6f_main.jpg' % PROTOCOL	, self.e('.section p:nth-of-type(1) img').get_attribute('src'))
		self.assertEqual('%s://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4f_sec.jpg' % PROTOCOL	, self.e('.section p:nth-of-type(7) img').get_attribute('src'))
		
	@url('/community/schools-resources/')
	def test_schools_resources(self):
		self.assertTitle('Historypin | Community | Schools | Activities and Downloadable Resources')
		self.assertEqual('Activities & Downloads for Schools', self.e('h1.title').text)
		self.assertEqual('Downloadable Resources', self.e('h2:nth-of-type(1)').text)
		
		link = 'historypin/docs/'
		
		resources = [
			{
				'heading': 'Activity Sheets',
				'items': [
					['Activity Sheet 1: Recording the story behind a photo'	, 'Worksheet_story%20collections.pdf', 'Blank template for recording info gathered in a interview or session'],
					['Activity Sheet 2: Recording the story behind a photo'	, '%sActivity_Sheet_2_Recording_the_story_behind_a_photo.pdf' % link, 'Worksheet with a series of questions guiding you through interview or session'],
					['Activity Sheet 3: Exploring Historypin'				, '%sActivity_Sheet_3_Exploring_Historypin.pdf' % link, 'Worksheet with series of activities of things to find and do on Historypin'],
				],
			},
			{
				'heading': 'Tip Sheets',
				'items': [
					['Tip Sheet 1: Taking a Photo of a Photo'								, '%sTip_Sheet_1_Taking_a_Photo_of_a_Photo.pdf' % link, 'All you need to know about taking the perfect photo of a photo - the easy way to digitise old photographs'],
					['Tip Sheet 2: Ideas for local projects'								, '%sTip_Sheet_2_Ideas_for_local_projects.pdf' % link, 'Ideas and examples of the types of local projects you can run (both online and offline events)'],
					['Tip Sheet 3: Tips on Planning your Historypin Local Project'			, '%sTip_Sheet_3_Tips_on_Planning_your_Historypin_Local_Project.pdf' % link, 'Tips on how to set up and plan your local project (both online and offline events)'],
					['Tip Sheet 4: Tips on the techie parts of running a session or event'	, '%sTip_Sheet_4_Tips_on_the_techie_parts_of_running_a_session_or_event.pdf' % link, 'Practical advice if you are running online sessions'],
					['Tip Sheet 5: Tip on Interviewing someone'								, '%sTip_Sheet_5_Tip_on_Interviewing_someone.pdf' % link, 'Things to think about before and during your conversation, plus ideas for questions'],
					['Historypin Presentation template'										, '%sHistorypin_Presentation.ppt' % link, 'Powerpoint presentation to introduce Historypin to your school, group or organisation (includes spare slides for adding info about your session or event)'],
				],
			},
			{
				'heading': 'Posters, flyers and certificates',
				'items': [
					['Poster advertising your event or session'								, '%sPoster_advertising_your_event_or_session.pdf' % link, 'With fillable inable gaps for your details'],
					['Flyer advertising your event or session'								, '%sFlyer_advertising_your_event_or_session.pdf' % link, 'With fillable inable gaps for your details'],
					['Invite announcing your event'											, '%sInvite_announcing_your_event.pdf' % link, 'With fillable inable gaps for your details'],
					['Certificate for participants'											, '%sCertificate_for_participants.pdf' % link, 'For awarding to people for their work discovering and sharing history with fillable inable gaps for your details'],
				],
			},
		]
		
		headings 	= self.es('.inner.right h3')
		list_items	= self.es('.inner.right ul li')
		links		= self.es('.inner.right ul a')
		
		k = 0
		for n in range(len(resources)):
			i = resources[n]
			
			self.assertEqual(i['heading'], headings[n].text)
			
			for item in i['items']:
				self.assertEqual(item[0] + '\n' + item[2], list_items[k].text)
				self.assertEqual(PROTOCOL + '://wawwd-resources.s3.amazonaws.com/' + item[1], links[k].get_attribute('href'))
				
				k += 1
		
		self.assertEqual('Activities by subject', self.e('h2:nth-of-type(2)').text)
		
		activities = [
			['History', 'Students explore the map between particular dates as an introduction to that period of history to see what photos, videos or audio they can find.'],
			['ICT', 'Students search Historypin by location, by key word and by date to find information about particular locations at particular times in order to answer questions. They compare the information from different photos, videos and stories and decide which are most useful and reliable.'],
			['Geography', 'Students pin photos onto the Historypin map using an address and then pin them to Street View using recognisable features to determine the angle at which a photo was taken.'],
			['English', 'Students use photos, video or audio content from the site as an inspiration to write a short story, play or poem.'],
			['Citizenship', 'Historypin can be used to develop an understanding of community cohesion.'],
			['Further educational links', 'Historypin supports a wide range of educational agendas and can be used to support activities around community cohesion, cultural diversity, embedding IT in the curriculum, cross-curricular activities, identity and cultural diversity, and wider participation.'],
		]
		
		headings = self.es('h2:nth-of-type(2) ~ h3')
		paragraphs = self.es('.inner.right h3 + p')
		for n in range(len(activities)):
			i = activities[n]
			self.assertEqual(i[0], headings[n].text)
			self.assertEqual(i[1], paragraphs[n].text)
