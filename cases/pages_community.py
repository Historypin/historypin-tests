# -*- coding: utf-8 -*-

from base import *
import logging
class Community(HPTestCase):
	
	@url('/community/')
	def test_home(self):
		self.assertTitle('Historypin | Community Homepage')
		self.assertEqual(self.e('.info h1').text, 'Get Involved')
		self.assertEqual(self.e('.main-image').get_attribute('src'), URL_BASE + '/resources/images/channels/channels_home_promo_image.jpg')
		self.assertEqual(self.e('.info p').text, 'Welcome to the Historypin community, made up of people, groups and organisations working together to unearth and pin as much history as possible from all over the world - from within archives, in attics, and saved up in wise old heads.')
		
		mods = [
			['Schools', '/community/schools'],
			['Local projects', '/community/localprojects'],
			['Libraries, Archives and Museums', '/community/lams'],
		]
		
		links = self.es('.inner.mod a')
		for n in range(len(mods)):
			i = mods[n]
			self.assertEqual(links[n].text, i[0])
			self.assertEqual(links[n].get_attribute('href'), URL_BASE + i[1])
		
		headings = ['Latest News', 'Challenges', 'Get Involved']
		h2s = self.es('.grid h2')
		for n in range(len(headings)):
			self.assertEqual(h2s[n].text, headings[n])
		
		groups = [
			['Pinning The Queen\'s History', 'What pics and stories do you have of the Queen\'s visits and Jubilee celebrations?', 'http://wearewhatwedo.org/queen.jpg', u'View The Queen’s Collection', URL_BASE + '/DiamondJubilee/'],
			['The Chevy Centenary', u'We’re looking for pics and stories of each of the Chevy models created over the last 100 years.', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/chevy_img.png', 'View Chevy Collection', URL_BASE + '/chevy/'],
			['Life Story Challenge', 'Create a Life Story about someone you know with photos and memories telling the story of their life.', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/icon_life_stories.png', 'View Life Stories Challenge', 'http://www.11492009-gats.historypin.com/en/page/life-stories/'],
			['Google Groups', u'Talk to other users, learn from each other’s experience, plus give us feedback as we experiment with new features.', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/icon_google_groups.png', 'Visit the Group', 'https://groups.google.com/forum/?fromgroups#!forum/historypin'],
			['Meet the team', 'Check out the people working away to bring you Historypin.', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/theteam.jpg', 'Meet the team', URL_BASE + '/team'],
			['The Foundation', 'Find out about our Charitable Foundation which works on the ground in local communities and education.', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/friends_of_historypin.jpg', 'Read more', URL_BASE + '/Friends-Of-Historypin/'],
		]
		
		headings	= self.es('.group ~ .group .col h3')
		paragraphs	= self.es('.group ~ .group .col p')
		images		= self.es('.group ~ .group .col img')
		links		= self.es('.group ~ .group .col a')
		
		for n in range(len(groups)):
			i = groups[n]
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(paragraphs[n].text, i[1])
			self.assertEqual(images[n].get_attribute('src'), i[2])
			self.assertEqual(links[2 * n].get_attribute('href'), i[4])
			self.assertEqual(links[2 * n + 1].get_attribute('href'), i[4])
			self.assertEqual(links[2 * n + 1].text, i[3])
		
		self.assertEqual(len(self.es('.group:nth-of-type(1) .col')), 3)
	
	@url('/community/schools')
	def test_sidebar(self):
		sidebar = [
			['Community Homepage', URL_BASE + '/community', 'Lots of news, ideas, and info for Historypinners round the world'],
			['Schools Homepage', URL_BASE + '/community/schools', 'Want to run a Historypin session or event in your school?'],
			['Local Projects Homepage', URL_BASE + '/community/localprojects', 'Want to run a Historypin session or event with your group?'],
			['Libraries, Archives and Museums Homepage', URL_BASE + '/community/lams', 'Want to get your institution involved?'],
			['Libraries, Archives and Museums Involved', URL_BASE + '/community/lams-involved', 'Find out the institutions that are already sharing their history on Historypin.'],
			['How To Guides', URL_BASE + '/community/howtos', 'Downloadable pdfs and videos to explain how to do everything'],
			['Activities & Downloadables for schools', URL_BASE + '/community/schools-resources', 'Resources to make running sessions and events easier.'],
			['Activities & Downloadables for projects', URL_BASE + '/community/localprojects-resources', 'Resources to make running sessions and events easier.'],
			['Topics to Explore', URL_BASE + '/community/topics-to-explore', 'Some of the most interesting photos, Tours and Collections to explore in sessions.'],
			['School Case Studies', URL_BASE + '/community/schools-case-studies', 'Some examples of schools around the word using Historypin'],
			['Local Project Case Studies', URL_BASE + '/community/localprojects-case-studies', 'Some examples of local projects around the world using Historypin'],
			['Support Us', URL_BASE + '/donate/', u'Donate to Friends of Historypin and you’ll be helping support Historypin Community and Education Programmes.\n\nRegistered Charity Number 1134546'],
			['Blog', 'http://blog.historypin.com/', 'Find out the latest community, site development, partnership and Challenges news'],
			['Contact', URL_BASE + '/contact-us', 'For more information contact Rebekkah Abraham, Historypin Content Manager on rebekkah.abraham@wearewhatwedo.org.'],
		]
		
		headings	= self.es('.sidebar .inner h4')
		links		= self.es('.sidebar .inner h4 a')
		paragraphs	= self.es('.sidebar .inner p')
		
		for n in (range(len(sidebar))):
			i = sidebar[n]
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(links[n].get_attribute('href'), i[1])
			self.assertEqual(paragraphs[n].text, i[2])
			
		self.assertEqual(self.e('.sidebar .inner p:last-of-type a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
	
	@url('/community/schools')
	def test_home_schools(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual(self.e('h1.title').text, 'Schools')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/schools_main.jpg')
		
		questions = [
			['Why use Historypin in schools?', '', ''],
			['How can I use it?', '/community/howtos', 'Have a look at our How to Guides for more help'],
			['How are other schools using it?', '/community/schools-case-studies', 'Have a look at our Case Studies for some ideas'],
			['What are the best things to look at in the classroom?', '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', '/community/schools-resources', 'See our Activities and Downloadables'],
		]
		
		headings = self.es('.section h3')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(paragraphs[k].get_attribute('href'), URL_BASE + i[1])
				self.assertEqual(paragraphs[k].text, i[2])
				
				k += 1
		
	@url('/community/localprojects')
	def test_home_projects(self):
		self.assertTitle('Historypin | Community | Local Projects')
		self.assertEqual(self.e('h1.title').text, 'Local Projects')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/localprojects_main.jpg')
		
		questions = [
			['Why use Historypin in local projects?', '', ''],
			['How can I use it?', '/community/howtos', 'Have a look at our How to Guides for more help'],
			['How are other local projects using it?', '/community/localprojects-case-studies', 'Have a look at our Local Projects Case Studies for some ideas'],
			['What are the best things to look at?', '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', '/community/localprojects-resources', 'See our Activites and Downloadables for Local Projects'],
		]
		
		headings = self.es('.section h2')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(paragraphs[k].get_attribute('href'), URL_BASE + i[1])
				self.assertEqual(paragraphs[k].text, i[2])
				
				k += 1
	
	@url('/community/lams')
	def test_home_lams(self):
		self.assertTitle('Historypin | Community | Libraries, Archives & Museums')
		self.assertEqual(self.e('.right h1').text, 'Libraries, Archives and Museums homepage')
		self.assertEqual(self.e('.right img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/lams_main.jpg')
		
		headings = self.es('.inner.right h3')
		links	 = self.es('.inner.right h3+p a')
		
		h3s = [
			['Get Started', 'http://wawwd-resources.s3.amazonaws.com/Getting%20Started%20on%20Historypin.pdf', 'Getting Started Guide'],
			['Institutions Involved', URL_BASE +'/community/lams-involved', u'See what other institutions are already involved and what they’re saying about Historypin.'],
			['10 reasons to get Involved', '', ''],
			['Frequently Asked Questions', 'http://www.historypin.com/faq/', 'FAQ section'], #fix link to be with the current version
		]
		
		k = 0
		for n in range(len(h3s)):
			i = h3s[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(links[k].get_attribute('href'), i[1])
				self.assertEqual(links[k].text, i[2])
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
			self.assertEqual(links_faq[n].get_attribute('href'), URL_BASE + '/community/lams#' + i[0])
			self.assertEqual(links_faq[n].text, i[1])
			self.assertEqual(h4s[n].get_attribute('id'), i[0])
			self.assertEqual(h4s[n].text, i[1])
	
	@url('/community/lams-involved')
	def test_lams_involved(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		self.assertEqual(self.e('.right h1').text, 'Institutions involved')
		self.assertEqual(self.e('.right h2').text, 'What Institutions are saying about Historypin')
		
		# TODO check for the firs list item
		# - ancor exists ancor
		# - image
	
	@url('/community/howtos')
	def test_how_tos(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		
		how_tos = [
			{
				'heading': 'Exploring',
				'items': [
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Creating%20an%20account%20and%20logging%20in.pdf', 'How to create an account and log in'],
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_How%20to%20explore%20Historypin.pdf', 'How to explore Historypin'],
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Exploring%20Tours%20and%20Collections.pdf', 'How to explore Tours and Collections'],
					['https://www.youtube.com/watch?v=wTXA1iuB1EA', 'Video: How to navigate the map'],
					['https://www.youtube.com/watch?v=GA7g7jjCgpo', 'Video: How to look at content and stories'],
					['https://www.youtube.com/watch?v=01cO2pS_iF4', 'Video: How to listen to audio clips'],
					['https://www.youtube.com/watch?v=URP0BNfuGY8', 'Video: How to navigate Street View'],
					['https://www.youtube.com/watch?v=CFDet-0_BOw', 'Video: How to explore a Collection'],
					['https://www.youtube.com/watch?v=uDILtzhWNi0', 'Video: How to explore a Tour'],
				]
			},
			
			{
				'heading': 'Adding',
				'items': [
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Your%20Channel.pdf', 'Your Channel'],
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Pinning.pdf', 'How to pin a photo'],
					['https://www.youtube.com/watch?v=7RWb7nw2q6w', 'Video: How to pin a photo'],
					['https://www.youtube.com/watch?v=v6THvhAERfo', 'Video: How to pin a photo to Street View'],
					['https://www.youtube.com/watch?v=EFrBBC9puSs', 'Video: How to create a Historypin account if you already have a Gmail account'],
					['https://www.youtube.com/watch?v=eYt0ZYsXP9M', 'Video: How to create a Historypin account if you have a an email account other than Gmail'],
					['https://www.youtube.com/watch?v=UOrnhWvvRpk', 'Video: How to create a Historypin account if you don\'t have an email account'],
					['https://www.youtube.com/watch?v=6gJ07pY1qus', 'Video: How to add a story to a photo'],
					['https://www.youtube.com/watch?v=NmbVYc8cVwM', 'Video: How to add favourites'],
				]
			},
			
			{
				'heading': 'Curating',
				'items': [
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Creating%20your%20own%20Collection.pdf', 'How to Create a Collection'],
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Creating%20an%20account%20and%20logging%20in.pdf', 'How to Create a Tour'],
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Exploring%20Tours%20and%20Collections.pdf', 'How to explore Tours and Collections'],
					['https://www.youtube.com/watch?v=rlF6ehpEAZk', 'Video: How to create a tour'],
					['https://www.youtube.com/watch?v=0Fs58oGZPLY', 'Video: How to create a Collection'],
					['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012.pdf', 'Complete Historypin Guide'],
				]
			},
		]
		
		headings = self.es('.inner.right h2')
		uls = self.es('.inner.right ul')
		
		# TODO move links outside of the for
		for n in range(len(how_tos)):
			i = how_tos[n]
			
			self.assertEqual(headings[n].text, i['heading'])
			
			links = uls[n].es('a')
			for k in range(len(i['items'])):
				link = i['items'][k]
				self.assertEqual(links[k].get_attribute('href'), link[0])
				self.assertEqual(links[k].text, link[1])
	
	@url('/community/localprojects-resources')
	def test_projects_resources(self):
		self.assertTitle('Historypin | Community | Local Projects | Resources')
		self.assertEqual(self.e('.right h1').text, 'Activities & Downloads for Local Projects')
		self.assertEqual(self.e('.right h2').text, 'Downloadable Resources')
		
		resources = [
			{
				'heading': 'Activity Sheets',
				'items': [
					['Activity Sheet 1: Recording the story behind a photo', 'http://wawwd-resources.s3.amazonaws.com/Worksheet_story%20collections.pdf', 'Blank template for recording info gathered in a interview or session'],
					['Activity Sheet 2: Recording the story behind a photo', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Activity_Sheet_2_Recording_the_story_behind_a_photo.pdf', 'Worksheet with a series of questions guiding you through interview or session'],
					['Activity Sheet 3: Exploring Historypin', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Activity_Sheet_3_Exploring_Historypin.pdf', 'Worksheet with series of activities of things to find and do on Historypin'],
				],
			},
			{
				'heading': 'Tip Sheets',
				'items': [
					['Tip Sheet 1: Taking a Photo of a Photo', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_1_Taking_a_Photo_of_a_Photo.pdf', 'All you need to know about taking the perfect photo of a photo - the easy way to digitise old photographs'],
					['Tip Sheet 2: Ideas for local projects', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_2_Ideas_for_local_projects.pdf', 'Ideas and examples of the types of local projects you can run (both online and offline events)'],
					['Tip Sheet 3: Tips on Planning your Historypin Local Project', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_3_Tips_on_Planning_your_Historypin_Local_Project.pdf', 'Tips on how to set up and plan your local project (both online and offline events)'],
					['Tip Sheet 4: Tips on the techie parts of running a session or event', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_4_Tips_on_the_techie_parts_of_running_a_session_or_event.pdf', 'Practical advice if you are running online sessions'],
					['Tip Sheet 5: Tip on Interviewing someone', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_5_Tip_on_Interviewing_someone.pdf', 'Things to think about before and during your conversation, plus ideas for questions'],
					['Historypin Presentation template', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Historypin_Presentation.ppt', 'Powerpoint presentation to introduce Historypin to your school, group or organisation (includes spare slides for adding info about your session or event)'],
				],
			},
			{
				'heading': 'Posters, flyers and certificates',
				'items': [
					['Poster advertising your event or session', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Poster_advertising_your_event_or_session.pdf', 'With fillable inable gaps for your details'],
					['Flyer advertising your event or session', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Flyer_advertising_your_event_or_session.pdf', 'With fillable inable gaps for your details'],
					['Invite announcing your event', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Invite_announcing_your_event.pdf', 'With fillable inable gaps for your details'],
					['Certificate for participants', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Certificate_for_participants.pdf', 'For awarding to people for their work discovering and sharing history with fillable inable gaps for your details'],
				],
			},
		]
			
		headings		= self.es('.inner.right h3')
		list_items		= self.es('.inner.right ul li')
		links			= self.es('.inner.right ul a')
		
		k = 0
		for n in range(len(resources)):
			i = resources[n]
			
			self.assertEqual(headings[n].text, i['heading'])
			
			for item in i['items']:
				self.assertEqual(list_items[k].text, item[0] + '\n' + item[2])
				self.assertEqual(links[k].get_attribute('href'), item[1])
				
				k += 1
	
	@url('/community/localprojects-case-studies')
	def test_projects_studies(self):
		self.assertTitle('Historypin | Community | Local Projects Case Studies')
		self.assertEqual(self.e('.right h1').text, 'Local Projects Case Studies')
		
		studies = [
			['Magic Me, Tower Hamlets, London, UK', '/community/localprojects-case-study-magicme', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_thumb.jpg', u'A set of inter-generational workshop sessions held at the Sundial Community Centre and in the streets around the area, run in partnership with the UK’s leading provider of intergenerational arts activities.'],
			['Reading, Berkshire, UK', '/community/localprojects-case-study-reading', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_thumb.jpg', 'A huge community project involving Reading Museum, local schools, care homes, community groups and societies, mapping the history of an entire town.'],
			['San Francisco, USA', '/community/localprojects-case-study-sanfrancisco', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4e_thumb.jpg', 'A special exhibition of photos from the San Francisco Transit Authority Archive at the Market Street Railway Museum and bus shelters around the city, allowing for amazing real-life then-and-now comparisons.'],
			['Lighthouse, Brighton, UK', '/community/localprojects-case-study-lighthouse', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4b_thumb.jpg', 'An inter-generational project bringing together school students and older residents of Brighton alive during World War 2. Films, an exhibition and Collections on Historypin were created.'],
		]
		
		grid			= self.e('.grid')
		headings		= grid.es('h3')
		headings_links	= grid.es('h3 a')
		images			= grid.es('a img')
		# TODO image_links		= grid.es('a img')
		paragraphs		= grid.es('p')
		
		for n in range(len(studies)):
			i = studies[n]
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(headings_links[n].get_attribute('href'), URL_BASE + i[1])
			self.assertEqual(images[n].get_attribute('src'), i[2])
			self.assertEqual(paragraphs[n].text, i[3])
		
	@url('/community/localprojects-case-study-magicme')
	def test_projects_studies_magicme(self):
		self.assertTitle('Historypin | Community | Local Projects | Magic Me, Tower Hamlets, London, UK')
		self.assertEqual(self.e('h1.title').text, 'Magic Me, Tower Hamlets, London, UK')
		
		imgs = self.es('.section img')
		self.assertEqual(imgs[0].get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_main.jpg')
		self.assertEqual(imgs[1].get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_sec.jpg')
		self.assertEqual(self.e('.section a').get_attribute('href'), URL_BASE + '/channels/view/6932562/name/magicme/')
	
	@url('/community/localprojects-case-study-reading')
	def test_projects_studies_reading(self):
		self.assertTitle('Historypin | Community | Local Projects | Reading, Berkshire, UK')
		self.assertEqual(self.e('h1.title').text, 'Reading, Berkshire, UK')
		
		imgs = self.es('.section img')
		headings = self.es('.section h3')
		self.assertEqual(imgs[0].get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_main.jpg')
		self.assertEqual(imgs[1].get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_sec.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(8) a').get_attribute('href'), URL_BASE + '/community/localprojects-reading/')
		self.assertEqual(headings[0].text, 'What people had to say about it')
		self.assertEqual(headings[1].text, 'What was the impact?')
		self.assertEqual(self.e('.section h3~a').get_attribute('href'), URL_BASE + '/resources/images/reading_evaluation_infographic.jpg')
		self.assertEqual(self.e('.section a img').get_attribute('src'), URL_BASE + '/resources/images/reading_evaluation_infographic_thumb.jpg')
		self.assertEqual(self.e('.section h3~p a:nth-of-type(1)').get_attribute('href'), 'http://wawwd-resources.s3.amazonaws.com/Reading_Evaluation%20Report_Small.pdf')

	@url('/community/localprojects-reading/')
	def test_community_localprojects_reading(self):
		self.assertTitle('Historypin | Community | Local Projects | Reading')
		self.assertEqual(self.e('h1.title').text, 'Reading, UK')
		
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
			self.assertEqual(headings[n].text, i)
			
		list_images = [
			['/resources/images/content/community/reading/small_1.jpg', '/channels/view/id/6604879/', 'RG Community'],
			['/resources/images/content/community/reading/small_2.jpg', '/channels/view/id/7012010/', 'Museum of English Rural Life'],
			['/resources/images/content/community/reading/small_3.jpg', '/channels/view/id/6160003/', 'Giles Knapp'],
			['/resources/images/content/community/reading/small_4.jpg', '/channels/view/id/1892068/', 'Reading Museum'],
			['/resources/images/content/community/reading/small_5.jpg', '/channels/view/id/1968007/', 'Malcolm'],
			['/resources/images/content/community/reading/small_8.jpg', '/channels/view/id/5787040/', 'Sitevolunteer'],
		]
		
		# TODO Refac selector
		images			= self.es('.col.w2:nth-of-type(1) ul img')
		pinners_links	= self.es('.col.w2:nth-of-type(1) ul a')
		
		for n in range(len(list_images)):
			i = list_images[n]
			self.assertEqual(images[n].get_attribute('src'), URL_BASE + i[0])
			self.assertEqual(pinners_links[n].get_attribute('href'), URL_BASE + i[1])
			self.assertEqual(pinners_links[n].text, i[2])
		
		self.assertEqual(self.e('.col.w2:nth-of-type(2) img').get_attribute('src'), URL_BASE + '/resources/images/content/community/reading/take_a_tour.jpg')
		self.assertEqual(self.e('a.button').get_attribute('href'), URL_BASE + '/tours/view/id/6917547/title/Snapshots%20of%20Reading')
		self.assertEqual(self.e('a.button span').text, 'Take the Tour')
		
		pinners = [
			['/resources/images/content/community/reading/medium_1.jpg', '/map/#/geo:51.465794,-0.966198/zoom:15/dialog:1834055/tab:details/', 'Floods in Gosbrook Road, Caversham - April 1947'],
			['/resources/images/content/community/reading/medium_2.jpg', '/map/#/geo:51.455863,-0.990668/zoom:15/dialog:1228008/tab:streetview/', 'Traffic on Oxford Road, 1893'],
			['/resources/images/content/community/reading/medium_3.jpg', '/map/#/geo:51.445213,-1.000692/zoom:15/dialog:5845061/tab:details/', 'Silver Jubilee Street Party Vine Crescent Reading, 1977'],
			['/resources/images/content/community/reading/medium_4.jpg', '/map/#/geo:51.456665,-0.970927/zoom:16/dialog:6610677/tab:streetview/', 'Town Hall, Reading,1900'],
			['/resources/images/content/community/reading/medium_5.jpg', '/map/#/geo:51.44799,-1.023132/zoom:16/dialog:5841163/tab:details/', 'Cast of Play in Garden of St. Michael\'s Rectory, 1951 - 1953'],
			['/resources/images/content/community/reading/medium_6.jpg', '/map/#/geo:51.472803,-0.96989/zoom:14/dialog:6931485/tab:details/', 'Bernard Tripp at Bugs Bottom, 1943'],
		]
		
		images	= self.es('.cf img')
		links	= self.es('.cf a')
		for n in range(len(pinners)):
			i = pinners[n]
			self.assertEqual(images[n].get_attribute('src'), URL_BASE + i[0])
			self.assertEqual(links[n].get_attribute('href'), URL_BASE + i[1])
			self.assertEqual(links[n].text, i[2])
			
		
		images = self.es('h2 ~ img')
		self.assertEqual(images[0].get_attribute('src'), URL_BASE + '/resources/images/content/community/reading/pined_on_a_map.jpg')
		self.assertEqual(images[1].get_attribute('src'), URL_BASE + '/resources/images/hlf_web.jpg')
		self.assertEqual(images[2].get_attribute('src'), URL_BASE + '/resources/images/gul_web.jpg')
		
	@url('/community/localprojects-case-study-sanfrancisco')
	def test_projects_studies_sanfrancisco(self):
		self.assertTitle('Historypin | Community | Local Projects | San Francisco, USA')
		self.assertEqual(self.e('h1.title').text, 'San Francisco, USA')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4d_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(6) a').get_attribute('href'), URL_BASE + '/sfmta')
		self.assertEqual(self.e('.section p:nth-of-type(6) a').text, 'SFMTA collection on Historypin')
	
	@url('/community/localprojects-case-study-lighthouse')
	def test_projects_studies_lighthouse(self):
		self.assertTitle('Historypin | Community | Local Projects | Lighthouse, Brighton, UK')
		self.assertEqual(self.e('h1.title').text, 'Lighthouse, Brighton, UK')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4b_main.jpg')
	
	@url('/community/topics-to-explore')
	def test_topics_to_explore(self):
		self.assertTitle('Historypin | Community | Topics to Explore')
		self.assertEqual(self.e('.right h1').text, 'Topics to Explore')
		
		topics = [
			{
				'heading': 'Collections',
				'items': [
					['The 1906 San Francisco Earthquake', '/collections/view/id/6621364/title/The%201906%20San%20Francisco%20Earthqauke', '/services/thumb/phid/5947051/dim/142x100/crop/1/quality/90', 'This Collection of photos of San Francisco after the 1906 earthquake and fire gathers photos around a historical event.'],
					['The Facial Hair Through Time Collection', '/collections/view/id/3762008/title/The%20Facial%20Hair%20Through%20Time%20Collection', '/services/thumb/phid/2438073/dim/142x100/crop/1/quality/90', 'This Collection of facial hair from different times and places around the world gathers photos around a particular theme.'],
					['Fabulous Fashion', '/collections/view/id/6593909/title/Fabulous%20Fashion', '/services/thumb/phid/6160458/dim/142x100/crop/1/quality/90', 'This Collection illustrates change over time through photos of fashionable outfits arranged in chronological order.'],
					['Codford Army Camps, Wiltshire, May-June 1919', '/collections/view/id/8237152/title/Codford%20Army%20Camps,%20Wiltshire,%20May-June%201919', '/services/thumb/phid/8230049/dim/142x100/crop/1/quality/90', u'This Collection is of family photos taken by the user’s relative who was in the army and took photos during his postings in the 1919.'],
					['University of Florida Homecoming', '/collections/view/id/7604020/title/University%20of%20Florida%20Homecoming', '/services/thumb/phid/7447179/dim/142x100/crop/1/quality/90', 'This Collection of Homecoming celebrations at the University of Florida gathers photos of an annual event through the years.'],
					['Sport in Reading', '/collections/view/id/7763032/title/Sport', '/services/thumb/phid/6926137/dim/142x100/crop/1/quality/90', 'This Collection was created by a class of 13 year old students who collected photos around the theme of sporting events in their local area.'],
				],
			},
			{
				'heading': 'Tours',
				'items': [
					['New York Immigration', '/tours/view/id/7188013/title/New%20York%20Immigration', '/services/thumb/phid/3226006/dim/142x100/crop/1/quality/90', 'This Tour explores a historical theme and illustrates 19th century immigration to the US with a snapshot of immigrant life in 19th century NYC.'],
					['World War Two', '/tours/view/id/6618250/title/World%20War%20Two', '/services/thumb/phid/1019016/dim/142x100/crop/1/quality/90', 'This Tour narrates a historical event and uses photos and audio clips to highlight key events during WWII from 1939-1945.'],
					[u'Tour of Hackney’s Past and Present', '/tours/view/id/9353267/title/Key%20Stage%20One%20Tour%20of%20Hackney%27s%20Past%20and%20Present', '/services/thumb/phid/8344085/dim/142x100/crop/1/quality/90', 'This Tour was created by a teacher and asks questions about historical photos of Hackney, London.'],
					['Queen Elizabeth II', '/tours/view/id/6605903/title/Queen%20Elizabeth%20II', '/services/thumb/phid/1046016/dim/142x100/crop/1/quality/90', u'This Tour narrates the biography or a person by highlighting key events of Queen Elizabeth II’s life.'],
					['A historical guided tour of Kew Gardens', '/tours/view/id/6631649/title/A%20historical%20guided%20tour%20of%20Kew%20Gardens', '/services/thumb/phid/2238024/dim/142x100/crop/1/quality/90', 'This Tour takes you on a historical walking Tour around Royal Botanical Gardens at Kew, UK.'],
					['The Grand Tour', '/tours/view/id/6921045/title/The%20Grand%20Tour', '/services/thumb/phid/4873006/dim/142x100/crop/1/quality/90', 'This Tour illustrates a famous route using historical photos.'],
				],
			},
			{
				'heading': 'Photos, Videos and Audio clips',
				'items': [
					[u'Occupy London camp in front of St Paul’s Cathedral, 16 October 2011', '/photos/#/geo:51.513745,-0.100594/zoom:15/date_from:1840-01-01/date_to:2011-11-11/dialog:7903122/tab:stories_tab_content/', '/services/thumb/phid/7903122/dim/142x100/crop/1/quality/90', u'This photo captures a modern moment of history, showing the protest occupying St Paul’s Church Yard, London in October 2011.'],
					['Earthquake damage, 25 February 2011', '/photos/#/geo:-43.507721,172.729543/zoom:10/sv:6657335/heading:-171.09375/pitch:-0.75000/sv_zoom:1.00000/', '/services/thumb/phid/6657335/dim/142x100/crop/1/quality/90', 'This photo, overlaid on Street View, shows buildings damaged by the earthquake in Christchurch, New Zealand in February 2011, illustrating the damage done by natural disasters.'],
					['Damage on Piccadilly, 1940 - 1942', '/map/#!/geo:51.509108,-0.136672/zoom:20/dialog:9547184/tab:stories_tab_content/', '/services/thumb/phid/9547184/dim/142x100/quality/90', 'This video clip illustrates bomb damage to Picadilly, London in the early 1940s.'],
					[u'JFK’s Inaugural Speech, 20th January 1961', '/map/#!/geo:38.891454,-77.01214/zoom:15/dialog:6607380/tab:stories_tab_content/', '/services/thumb/phid/6607380/dim/142x100/quality/90', u'This audio clip plays an extract from John F Kennedy’s inaugural speech in 1961.'],
					['Historypin Repeats', '/channels/view/id/571038/', '/channels/img/571038/logo/1/dim/142x100/crop/1/', 'This Channel has got some great Historypin Repeats - modern replicas of historical photos on Historypin, taken by people using the smartphone app.'],
					['Joe Voss, Jefferson Memorial, 1948 - 1952', '/photos/#/geo:38.889263,-77.05008/zoom:15/date_from:1840-01-01/date_to:2011-11-11/dialog:7205444/tab:more_tab_content/', '/services/thumb/phid/7205444/dim/142x100/crop/1/quality/90', 'This photo shows a Historypin Repeat. This Historypinner has pinned a photo of his Dad at Jefferson Memorial, Washington DC in the 1950s and used the Historypin app to take a photo of himself in the same spot in 2011.'],
				],
			}
		]
		
		grid				= self.e('.grid')
		headings 			= grid.es('h2')
		subheadings 		= grid.es('h3 a')
		links 				= grid.es('.inner > a')
		images 				= grid.es('a img')
		paragraphs 			= grid.es('p')
		
		k = 0
		for n in range(len(topics)):
			i = topics[n]
			
			self.assertEqual(headings[n].text, i['heading'])
			
			for item in i['items']:
				self.assertEqual(subheadings[k].text, item[0])
				self.assertEqual(subheadings[k].get_attribute('href'), URL_BASE + item[1])
				self.assertEqual(links[k].get_attribute('href'), URL_BASE + item[1])
				self.assertEqual(images[k].get_attribute('src'), URL_BASE + item[2])
				self.assertEqual(paragraphs[k].text, item[3])
				
				k += 1
	
	@url('/community/schools-case-studies/')
	def test_schools_studies(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual(self.e('.right h1').text, 'Schools Case Studies')
		
		studies = [
			['English International College, Marbella, Spain', '/community/schools-eic', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_thumb.jpg', 'Historypin is used as the theme for Humanities Day and students create an exhibition after parents and locals invited in for Historypin coffee morning.'],
			['Nelson Rural School, New Brunswick, Canada', '/community/schools-nelson', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6c_thumb.jpg', 'Students become local historians and archivists, going out into the community to find owners of old photographs and conduct interviews, recording it all on Historypin.'],
			['Billericay, Essex, UK', '/community/schools-billericay', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_thumb.jpg', '12-13 year old boys plan their own workshop where they meet with 12 senior citizens from the local area.'],
			['Cromer, Norfolk, UK', '/community/schools-cromer', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6e_thumb.jpg', 'History students assist at event in community centre where local residents are invited to bring along and upload their old photos and memories of Cromer.'],
			['Newport Primary School, Essex, UK', '/community/schools-newport', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6f_thumb.jpg', '9-11 years olds take part in offline activities around photographs and stories, then hold event where older people from local care homes and neighbourhoods share their histories.'],
		]
		
		grid			= self.e('.grid')
		headings		= grid.es('h3')
		headings_links	= grid.es('h3 a')
		images			= grid.es('a img')
		# TODO image_links		= grid.es('a img')
		paragraphs		= grid.es('p')
		
		for n in range(len(studies)):
			i = studies[n]
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(headings_links[n].get_attribute('href'), URL_BASE + i[1])
			self.assertEqual(images[n].get_attribute('src'), i[2])
			self.assertEqual(paragraphs[n].text, i[3])
		
	@url('/community/schools-eic/')
	def test_schools_studies_eic(self):
		self.assertTitle('Historypin | Community | Schools | English International College, Marbella, Spain')
		self.assertEqual(self.e('h1.title').text, 'English International College, Marbella, Spain')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_main.jpg')
		self.assertEqual(self.e('h2:nth-of-type(1)').text, 'Amy, Year 9')
		self.assertEqual(self.e('.section p:nth-of-type(10) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6b_fav1.jpg')
		
	@url('/community/schools-billericay/')
	def test_schools_studies_bill(self):
		self.assertTitle('Historypin | Community | Schools | Billericay School, Essex, UK')
		self.assertEqual(self.e('h1.title').text, 'Billericay School, Essex, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(12) a').get_attribute('href'),'http://billericayschool.net/speakup/2011/06/pinning-down-history/')
		self.assertEqual(self.e('.section p:nth-of-type(12) a').text,'Read more about the project on their blog.')
		self.assertEqual(self.e('h3:nth-of-type(1)').text, 'Video made by Billericay School for the day')
		self.assertEqual(self.e('h3:nth-of-type(2)').text, 'Feature on Radio Essex about the Billericay Historypin project')
		self.assertEqual(self.e('.section p:nth-of-type(14) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6d_sec.jpg')
	 
	@url('/community/schools-cromer/')
	def test_schools_studies_cromer(self):
		self.assertTitle('Historypin | Community | Schools | Cromer, Norfolk, UK')
		self.assertEqual(self.e('h1.title').text, 'Cromer, Norfolk, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6e_main.jpg')
	
	@url('/community/schools-nelson/')
	def test_schools_studies_nelson(self):
		self.assertTitle('Historypin | Community | Schools | Nelson Rural School, New Brunswick, Canada')
		self.assertEqual(self.e('h1.title').text, 'Nelson Rural School, New Brunswick, Canada')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6c_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(8) a').get_attribute('href'), URL_BASE + '/channels/view/8817007/name/nelsonrural7k/')
		self.assertEqual(self.e('.section p:nth-of-type(8) a').text, u'Nelson School’s Historypin Channel')
		
	@url('/community/schools-newport/')
	def test_schools_studies_newport(self):
		self.assertTitle('Historypin | Community | Schools | Newport Primary School, Essex, UK')
		self.assertEqual(self.e('h1.title').text, 'Newport Primary School, Essex, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/6f_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(7) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4f_sec.jpg')
		
	@url('/community/schools-resources/')
	def test_schools_resources(self):
		self.assertTitle('Historypin | Community | Schools | Activities and Downloadable Resources')
		self.assertEqual(self.e('h1.title').text, 'Activities & Downloads for Schools')
		self.assertEqual(self.e('h2:nth-of-type(1)').text, 'Downloadable Resources')
		
		resources = [
			{
				'heading': 'Activity Sheets',
				'items': [
					['Activity Sheet 1: Recording the story behind a photo', 'http://wawwd-resources.s3.amazonaws.com/Worksheet_story%20collections.pdf', 'Blank template for recording info gathered in a interview or session'],
					['Activity Sheet 2: Recording the story behind a photo', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Activity_Sheet_2_Recording_the_story_behind_a_photo.pdf', 'Worksheet with a series of questions guiding you through interview or session'],
					['Activity Sheet 3: Exploring Historypin', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Activity_Sheet_3_Exploring_Historypin.pdf', 'Worksheet with series of activities of things to find and do on Historypin'],
				],
			},
			{
				'heading': 'Tip Sheets',
				'items': [
					['Tip Sheet 1: Taking a Photo of a Photo', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_1_Taking_a_Photo_of_a_Photo.pdf', 'All you need to know about taking the perfect photo of a photo - the easy way to digitise old photographs'],
					['Tip Sheet 2: Ideas for local projects', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_2_Ideas_for_local_projects.pdf', 'Ideas and examples of the types of local projects you can run (both online and offline events)'],
					['Tip Sheet 3: Tips on Planning your Historypin Local Project', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_3_Tips_on_Planning_your_Historypin_Local_Project.pdf', 'Tips on how to set up and plan your local project (both online and offline events)'],
					['Tip Sheet 4: Tips on the techie parts of running a session or event', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_4_Tips_on_the_techie_parts_of_running_a_session_or_event.pdf', 'Practical advice if you are running online sessions'],
					['Tip Sheet 5: Tip on Interviewing someone', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Tip_Sheet_5_Tip_on_Interviewing_someone.pdf', 'Things to think about before and during your conversation, plus ideas for questions'],
					['Historypin Presentation template', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Historypin_Presentation.ppt', 'Powerpoint presentation to introduce Historypin to your school, group or organisation (includes spare slides for adding info about your session or event)'],
				],
			},
			{
				'heading': 'Posters, flyers and certificates',
				'items': [
					['Poster advertising your event or session', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Poster_advertising_your_event_or_session.pdf', 'With fillable inable gaps for your details'],
					['Flyer advertising your event or session', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Flyer_advertising_your_event_or_session.pdf', 'With fillable inable gaps for your details'],
					['Invite announcing your event', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Invite_announcing_your_event.pdf', 'With fillable inable gaps for your details'],
					['Certificate for participants', 'http://wawwd-resources.s3.amazonaws.com/historypin/docs/Certificate_for_participants.pdf', 'For awarding to people for their work discovering and sharing history with fillable inable gaps for your details'],
				],
			},
		]
		
		headings 	= self.es('.inner.right h3')
		list_items	= self.es('.inner.right ul li')
		links		= self.es('.inner.right ul a')
		
		k = 0
		for n in range(len(resources)):
			i = resources[n]
			
			self.assertEqual(headings[n].text, i['heading'])
			
			for item in i['items']:
				self.assertEqual(list_items[k].text, item[0] + '\n' + item[2])
				self.assertEqual(links[k].get_attribute('href'), item[1])
				
				k += 1
		
		self.assertEqual(self.e('h2:nth-of-type(2)').text, 'Activities by subject')
		
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
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(paragraphs[n].text, i[1])
