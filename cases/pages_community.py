# -*- coding: utf-8 -*-

from base import *

class Community(HPTestCase):
	@unittest.skip("TODO")
	@url('/community/')
	def test_home(self):
		self.assertTitle('Historypin | Community Homepage')
		self.assertEqual(self.e('.info h1').text, 'Get Involved')
		self.assertEqual(self.e('.main-image img').get_attribute('src'), URL_BASE + '/resources/images/channels/channels_home_promo_image.jpg')
		self.assertEqual(self.e('.info p').text, 'Welcome to the Historypin community, made up of people, groups and organisations working together to unearth and pin as much history as possible from all over the world - from within archives, in attics, and saved up in wise old heads.')
		
		sel = '#schools_section a'
		self.assertEqual(self.e(sel).get_attribute('href'), URL_BASE + '/community/schools')
		self.assertEqual(self.e(sel).text, 'Schools')

		sel = '#localprojects_section a'
		self.assertEqual(self.e(sel).get_attribute('href'), URL_BASE + '/community/localprojects')
		self.assertEqual(self.e(sel).text, 'Local projects')

		sel = '#lams_section a'
		self.assertEqual(self.e(sel).get_attribute('href'), URL_BASE + '/community/lams')
		self.assertEqual(self.e(sel).text, 'Libraries, Archives\n and Museums')

		self.assertEqual(self.e('.grid h2:nth-child(1)').text, 'Latest News')

		self.assertEqual(self.e('h2:nth-of-type(2)').text, 'Challenges')
		# TODO fix HTML first

		# TODO
		# assert title done 
		# assert heading done
		# assert text done
		# assert image done
		# assert schools linka and text done
		# assert local projects link and text done
		# LAMs link and text done
		# latest news heading done
		# verify elements present LATER
		# challenges title done
		# sub-titles 
		# links
		# text
		# images
		# get involved title
		# sub-headings
		# images
		# link
		# text

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
			['Support Us', 'http://www.historypin.com/donate/', u'Donate to Friends of Historypin and you’ll be helping support Historypin Community and Education Programmes.\n\nRegistered Charity Number 1134546'],
			['Blog', 'http://blog.historypin.com/', 'Find out the latest community, site development, partnership and Challenges news'],
			['Contact', URL_BASE + '/contact-us', 'For more information contact Rebekkah Abraham, Historypin Content Manager on rebekkah.abraham@wearewhatwedo.org.'],
		]
		
		headings = self.es('.sidebar .inner h4')
		paragraphs = self.es('.sidebar .inner p')
		for n in (range(len(sidebar))):
			i = sidebar[n]
			self.assertEqual(headings[n].text, i[0])
			self.assertEqual(headings[n].e('a').get_attribute('href'), i[1])
			self.assertEqual(paragraphs[n].text, i[2])
			
		self.assertEqual(self.e('.sidebar .inner p:last-of-type a').get_attribute('href'), 'mailto:rebekkah.abraham@wearewhatwedo.org')
	
	@url('/community/schools')
	def test_home_schools(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual(self.e('h1.title').text, 'Schools')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/schools_main.jpg')
		
		questions = [
			['Why use Historypin in schools?', '', ''],
			['How can I use it?', URL_BASE + '/community/howtos', 'Have a look at our How to Guides for more help'],
			['How are other schools using it?', URL_BASE + '/community/schools-case-studies', 'Have a look at our Case Studies for some ideas'],
			['What are the best things to look at in the classroom?', URL_BASE + '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', URL_BASE + '/community/schools-resources', 'See our Activities and Downloadables'],
		]
		
		headings = self.es('.section h3')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(paragraphs[k].get_attribute('href'), i[1])
				self.assertEqual(paragraphs[k].text, i[2])
				
				k += 1
		
	@url('/community/localprojects')
	def test_home_projects(self):
		self.assertTitle('Historypin | Community | Local Projects')
		self.assertEqual(self.e('h1.title').text, 'Local Projects')
		self.assertEqual(self.e('.section img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/localprojects_main.jpg')
		
		questions = [
			['Why use Historypin in local projects?', '', ''],
			['How can I use it?', URL_BASE + '/community/howtos', 'Have a look at our How to Guides for more help'],
			['How are other local projects using it?', URL_BASE + '/community/localprojects-case-studies', 'Have a look at our Local Projects Case Studies for some ideas'],
			['What are the best things to look at?', URL_BASE + '/community/topics-to-explore', 'Have a look at our Topics to Explore for some ideas'],
			['What activity ideas and resources do you have?', URL_BASE + '/community/localprojects-resources', 'See our Activites and Downloadables for Local Projects'],
		]
		
		headings = self.es('.section h2')
		paragraphs = self.es('.section p a')
		k = 0
		for n in (range(len(questions))):
			i = questions[n]
			self.assertEqual(headings[n].text, i[0])
			
			if i[1] and i[2]:
				self.assertEqual(paragraphs[k].get_attribute('href'), i[1])
				self.assertEqual(paragraphs[k].text, i[2])
				
				k += 1

	@url('/community/lams')
	def test_home_lams(self):
		self.assertTitle('Historypin | Community | Libraries, Archives & Museums')
		self.assertEqual(self.e('.right h1').text, 'Libraries, Archives and Museums homepage')
		self.assertEqual(self.e('.right img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/lams_main.jpg')
		
		# TODO
		# get started heading
		# link and text(Getting started guide)
		# institutions involved heading
		# - link and text
		# bulk upload link and text

	@url('/community/lams-involved')
	def test_lams_involved(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		self.assertEqual(self.e('.right h1').text, 'Institutions involved')
		self.assertEqual(self.e('.right h2').text, 'What Institutions are saying about Historypin')
		
	@unittest.skip("TODO")
	@url('/community/howtos')
	def test_how_tos(self):
		self.assertTitle('Historypin | Community | Schools | Historypin in the Classroom')
		self.assertEqual(self.e('h2:nth-of-type(1)').text, 'Exploring')
		self.assertEqual(self.e('h2:nth-of-type(2)').text, 'Adding')
		self.assertEqual(self.e('h2:nth-of-type(3)').text, 'Curating')
		how_tos = [
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Creating%20an%20account%20and%20logging%20in.pdf', 'How to create an account and log in'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_How%20to%20explore%20Historypin.pdf', 'How to explore Historypin'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Exploring%20Tours%20and%20Collections.pdf', 'How to explore Tours and Collections'],
			['https://www.youtube.com/watch?v=wTXA1iuB1EA', 'Video: How to navigate the map'],
			['https://www.youtube.com/watch?v=GA7g7jjCgpo', 'Video: How to look at content and stories'],
			['https://www.youtube.com/watch?v=01cO2pS_iF4', 'Video: How to listen to audio clips'],
			['https://www.youtube.com/watch?v=URP0BNfuGY8', 'Video: How to navigate Street View'],
			['https://www.youtube.com/watch?v=CFDet-0_BOw', 'Video: How to explore a Collection'],
			['https://www.youtube.com/watch?v=uDILtzhWNi0', 'Video: How to explore a Tour'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Your%20Channel.pdfhttp://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Pinning.pdf', 'Your Channel'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Pinning.pdf', 'How to pin a photo'],
			['https://www.youtube.com/watch?v=7RWb7nw2q6w', 'Video: How to pin a photo'],
			['https://www.youtube.com/watch?v=v6THvhAERfo', 'Video: How to pin a photo to Street View'],
			['https://www.youtube.com/watch?v=EFrBBC9puSs', 'Video: How to create a Historypin account if you already have a Gmail account'],
			['https://www.youtube.com/watch?v=eYt0ZYsXP9M', 'Video: How to create a Historypin account if you have a an email account other than Gmail'],
			['https://www.youtube.com/watch?v=UOrnhWvvRpk', 'Video: How to create a Historypin account if you don\'t have an email account'],
			['https://www.youtube.com/watch?v=6gJ07pY1qus', 'Video: How to add a story to a photo'],
			['https://www.youtube.com/watch?v=NmbVYc8cVwM', 'Video: How to add favourites'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Creating%20your%20own%20Collection.pdf', 'How to Create a Collection'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Creating%20an%20account%20and%20logging%20in.pdf', 'How to Create a Tour'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012_Exploring%20Tours%20and%20Collections.pdf', 'How to explore Tours and Collections'],
			['https://www.youtube.com/watch?v=rlF6ehpEAZk', 'Video: How to create a tour'],
			['https://www.youtube.com/watch?v=0Fs58oGZPLY', 'Video: How to create a Collection'],
			['http://wawwd-resources.s3.amazonaws.com/historypin/HP_GUIDE_2012.pdf', 'Complete Historypin Guide'],
		]
		
		# heading link text link
		#  - assert all links and text 
		#k = 0
		#for n in range(len(how_tos)):
		#	
		#	i = how_tos[n]
		#	self.assertEqual(self.e('.inner.right ul:nth-of-type(%d) li:nth-of-type(%d) a' % (n+1, k+1)).get_attribute('href'), i[0])
		#	self.assertEqual(self.e('.inner.right ul:nth-of-type(%d) li:nth-of-type(%d) a' % (n+1, k+1)).text, i[1])
		pass
			
	@unittest.skip("TODO")
	@url('/community/localprojects-resources')
	def test_projects_resources(self):
		self.assertTitle('Historypin | Community | Local Projects | Resources')
		self.assertEqual(self.e('.right h1').text, 'Activities & Downloads for Local Projects')
		self.assertEqual(self.e('.right h2').text, 'Downloadable Resources')
		
		
		# TODO
		# Activity Sheets/Tip Sheets/Posters, flyers and certificates headings
		# - assert all links 
		# - assert all texts
		# - assert all texts under the link
		pass
	
	@unittest.skip("TODO")
	@url('/community/localprojects-case-studies')
	def test_projects_studies(self):
		self.assertTitle('Historypin | Community | Local Projects Case Studies')
		self.assertEqual(self.e('.right h1').text, 'Local Projects Case Studies')
		
		#studies = [
		#	['Magic Me, Tower Hamlets, London, UK', URL_BASE + '/community/localprojects-case-study-magicme', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_thumb.jpg', 'A set of inter-generational workshop sessions held at the Sundial Community Centre and in the streets around the area,  run in partnership with the UK’s leading provider of intergenerational arts\nactivities.'],
		#	['Reading, Berkshire, UK', URL_BASE + '/community/localprojects-case-study-reading', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_thumb.jpg', 'A huge community project involving Reading Museum, local schools, care homes, community groups and societies, mapping the history of an entire town.'],
		#	['San Francisco, USA', URL_BASE + '/community/localprojects-case-study-sanfrancisco', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4e_thumb.jpg', 'A special exhibition of photos from the San Francisco Transit Authority Archive at the Market Street Railway Museum and bus shelters around the city, allowing for amazing real-life then-and-now\ncomparisons.'],
		#	['Lighthouse, Brighton, UK', URL_BASE + '/community/localprojects-case-study-lighthouse', 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4b_thumb.jpg', 'An inter-generational project bringing together school students and older residents of Brighton alive during World War 2. Films, an exhibition and Collections on Historypin were created.'],
		#]
		# %d, (n+1) ?
		#for n in (range(len(studies))):
		#	i = studies[n]
		#	self.assertEqual(self.e('.col .w2:nth-child(1) h3').text, i[0])
		#	self.assertEqual(self.e('.col .w2:nth-child(2) h3').text, i[0])
		#	self.assertEqual(self.e('.col .w2:nth-child(4) h3').text, i[0])
		#	self.assertEqual(self.e('.col .w2:nth-child(5) h3').text, i[0])
		#	
		#	self.assertEqual(self.e('.col .w2:nth-child(1) h3 a').get_attribute('href'), i[1])
		#	self.assertEqual(self.e('.col .w2:nth-child(2) h3 a').get_attribute('href'), i[1])
		#	self.assertEqual(self.e('.col .w2:nth-child(4) h3 a').get_attribute('href'), i[1])
		#	self.assertEqual(self.e('.col .w2:nth-child(5) h3 a').get_attribute('href'), i[1])
		#	
		#	self.assertEqual(self.e('.col .w2:nth-child(1) img').get_attribute('src'), i[2])
		#	self.assertEqual(self.e('.col .w2:nth-child(2) img').get_attribute('src'), i[2])
		#	self.assertEqual(self.e('.col .w2:nth-child(4) img').get_attribute('src'), i[2])
		#	self.assertEqual(self.e('.col .w2:nth-child(5) img').get_attribute('src'), i[2])
		#	
		#	self.assertEqual(self.e('.col .w2:nth-child(1) p').text, i[3])
		#	self.assertEqual(self.e('.col .w2:nth-child(2) p').text, i[3])
		#	self.assertEqual(self.e('.col .w2:nth-child(4) p').text, i[3])
		#	self.assertEqual(self.e('.col .w2:nth-child(5) p').text, i[3])
		
		pass
	@url('/community/localprojects-case-study-magicme')
	def test_projects_studies_magicme(self):
		self.assertTitle('Historypin | Community | Local Projects | Magic Me, Tower Hamlets, London, UK')
		self.assertEqual(self.e('h1.title').text, 'Magic Me, Tower Hamlets, London, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(9) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4c_sec.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(4) a').get_attribute('href'), URL_BASE + '/channels/view/6932562/name/magicme/')

	@url('/community/localprojects-case-study-reading')
	def test_projects_studies_reading(self):
		self.assertTitle('Historypin | Community | Local Projects | Reading, Berkshire, UK')
		self.assertEqual(self.e('h1.title').text, 'Reading, Berkshire, UK')
		self.assertEqual(self.e('.section p:nth-of-type(1) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(5) img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4a_sec.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(8) a').get_attribute('href'), 'http://historypin.com/community-localprojects-reading/') #check this link
		self.assertEqual(self.e('h3:nth-of-type(1)').text, 'What people had to say about it')
		self.assertEqual(self.e('h3:nth-of-type(2)').text, 'What was the impact?')
		# TODO
		# another test case with this page/community-localprojects-reading/

	@url('/community/localprojects-case-study-sanfrancisco')
	def test_projects_studies_sanfrancisco(self):
		self.assertTitle('Historypin | Community | Local Projects | San Francisco, USA')
		self.assertEqual(self.e('h1.title').text, 'San Francisco, USA')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4d_main.jpg')
		self.assertEqual(self.e('.section p:nth-of-type(6) a').get_attribute('href'),'http://historypin.com/sfmta') #check this link
		self.assertEqual(self.e('.section p:nth-of-type(6) a').text, 'SFMTA collection on Historypin')

	@url('/community/localprojects-case-study-lighthouse')
	def test_projects_studies_lighthouse(self):
		self.assertTitle('Historypin | Community | Local Projects | Lighthouse, Brighton, UK')
		self.assertEqual(self.e('h1.title').text, 'Lighthouse, Brighton, UK')
		self.assertEqual(self.e('.section p img').get_attribute('src'), 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/casestudies/4b_main.jpg')

	@unittest.skip("TODO")
	@url('/community/topics-to-explore')
	def test_topics_to_explore(self):
		self.assertTitle('Historypin | Community | Topics to Explore')
		self.assertEqual(self.e('.right h1').text, 'Topics to Explore')
		
		topics = [
				{
					'heading': 'Collection',
					'items': [
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
					],
				},
				{
					'heading': 'Tours',
					'items': [
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
					],
				},
				{
					'heading': 'Photos, Videos and Audio clips',
					'items': [
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
						['', '', ''],
					],
				
				}
			]
		#title text, title link, img src, p
		
		# TODO
		# assert Collection subheading ('s' should be added)
		# - all links
		# - all texts
		# - all all images
		# assert Tours subheading
		# - all links
		# - all texts
		# - all all images
		# assert Photos, Videos and Audio clips subheading
		# - all links
		# - all texts
		# - all all images
		pass

	@unittest.skip("TODO")
	@url('/community/schools-case-studies/')
	def test_schools_studies(self):
		self.assertTitle('Historypin | Community | Schools')
		self.assertEqual(self.e('.right h1').text, 'Schools Case Studies')
		# TODO
		# assert all subheadings
		# assert all text
		# assert all hrefs
		# assert all images
		pass
		
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
		
	@unittest.skip("TODO")
	@url('/community/schools-resources/')
	def test_schools_resources(self):
		# TODO
		# assert title
		# assert heading
		# assert "Downloadable Resources" text
		# assert Activity Sheets/Tip Sheets/Posters, flyers and certificates
		# - assert all bullets links and text
		# - assert all texts under the bullets
		# assert Activities by subject
		# assert all h3s
		pass

