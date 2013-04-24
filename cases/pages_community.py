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

	@unittest.skip("TODO")
	@url('/community/lams')
	def test_home_lams(self):
		# TODO
		# assert title
		# assert heading
		# assert image
		# get started heading
		# link and text(Getting started guide)
		# institutions involved heading
		# - link and text
		# bulk upload link and text
		pass

	@unittest.skip("TODO")
	@url('/')
	def test_lams_involved(self):
		# TODO
		# assert title
		# assert heading
		# assert one image
		# assert one link
		# What institutions say about HP heading 
		pass

	@unittest.skip("TODO")
	@url('/community/howtos')
	def test_how_tos(self):
		# TODO
		# assert title 
		# assert heading
		# assert all sub-headings
		#  - assert all links and text 
		pass
	
	@unittest.skip("TODO")
	@url('/community/localprojects-resources')
	def test_projects_resources(self):
		# TODO
		# assert title
		# assert heading
		# Downloadable Resources heading 
		# Activity Sheets/Tip Sheets/Posters, flyers and certificates headings
		# - assert all links 
		# - assert all texts
		# - assert all texts under the link
		pass
	
	@unittest.skip("TODO")
	@url('/community/localprojects-case-studies')
	def test_projects_studies(self):
		# TODO
		# assert title
		# assert heading
		# assert subheadings 
		# - assert links and links texts
		# - assert images
		pass

	@unittest.skip("TODO")
	@url('/community/localprojects-case-study-magicme')
	def test_projects_studies_magicme(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		# assert channel link
		pass

	@unittest.skip("TODO")
	@url('/community/localprojects-case-study-reading')
	def test_projects_studies_reading(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		# assert channel link
		pass

	@unittest.skip("TODO")
	@url('/community/localprojects-case-study-sanfrancisco')
	def test_projects_studies_sanfrancisco(self):
		# TODO
		# assert title
		# assert heading
		# assert image
		# assert channel link
		pass

	@unittest.skip("TODO")
	@url('/community/localprojects-case-study-lighthouse')
	def test_projects_studies_lighthouse(self):
		# TODO
		# assert title
		# assert heading
		# assert image
		# assert channel link
		pass

	@unittest.skip("TODO")
	@url('/community/topics-to-explore')
	def test_topics_to_explore(self):
		# TODO
		# assert title
		# assert heading
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
		# TODO
		# assert title
		# assert heading
		# assert text
		# assert all subheadings
		# assert all text
		# assert all hrefs
		# assert all images
		#check sidebar
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-eic/')
	def test_schools_studies_eic(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		# assert channel link
		# assert images
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-billericay/')
	def test_schools_studies_bill(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		# assert blog link
		# assert video made by..heading
		# assert feature on radio essex heading
		# assert image
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-cromer/')
	def test_schools_studies_cromer(self):
		# TODO
		# assert title
		# assert heading
		# assert image
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-nelson/')
	def test_schools_studies_nelson(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		# assert photo link and text
		# assert channel link and text
		pass
		
	@unittest.skip("TODO")
	@url('/community/schools-newport/')
	def test_schools_studies_newport(self):
		# TODO
		# assert title
		# assert heading
		# assert images
		pass
		
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

