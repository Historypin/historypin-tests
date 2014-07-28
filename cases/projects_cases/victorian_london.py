# -*- coding: utf-8 -*-

from base import *
import os, sys

class Project_VictorianLondon(HPTestCase):
	
	PROJECT_URL = '/en/explore/victorian-london'
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		project_cnt = self.e('.landing-cnt')
		
		self.assertEqual('Mapping emotions in Victorian London', project_cnt.e('h2').text)
		self.assertIn('Mapping the Emotions of London is a unique crowdsourcing experiment', project_cnt.e('.desc').text)
		
		
		projects_items = [
				['Dreadful London'						, '/dreadful-london/'],
				['London in the light'					, '/london-in-the-light/'],
				['A day in the life of the old London'	, '/old-london/'],
		]
		
		project_section	= project_cnt.e('section')
		h4s				= project_section.es('.item h4')
		link_pr			= project_section.es('.item a')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h4s[n].text)
			self.assertEqual(URL_BASE + self.PROJECT_URL + i[1], link_pr[n].get_attribute('href'))
		
		self.assertEqual('The Andrew W. Mellon Foundation', self.e('.partnership a').text)
		
		# TODO refactor this when there is text and links
		
	
	def test_about(self):
		self.go(self.PROJECT_URL)
		
		self.e('.desc a').click()
		
		self.assertEqual('About', self.e('.about h3').text)
		
		self.e('.about a').click()
		
		self.assertTrue(self.e('.desc a'), WebElement)
	