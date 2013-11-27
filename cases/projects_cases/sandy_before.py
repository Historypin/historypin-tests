# -*- coding: utf-8 -*-

from base import *
from sandy import Project_Sandy

class Project_Before_Sandy(Project_Sandy):
	
	PROJECT_URL = '/project/27-before-sandy'
	
	ATTACH_TABS = [
		['%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/gallery/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/stories/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/slideshow/' % (URL_BASE, PROJECT_URL)]
	]
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Before Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy/' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('Before Sandy'									, tout.e('h2').text)
		self.assertIn('What did neighborhoods look like before Sandy?'	, tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/projects/?subproject=27' % URL_BASE	, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'								, button_upload.e('span').text)
		
		self.assertEqual('%s/projects/img/pid/27/type/project_image/dim/980x411/crop/1/' % URL_BASE, site_cnt.e('.main-image img').get_attribute('src'))
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['During Sandy'		, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
			['After Sandy'		, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
			['Hurricane Sandy'	, '26-sandy/'		, 'How have communities and neighborhoods in the Caribbean'								, '26'],
		]
		
		h2s			= projects.es('h2')
		h2s_links	= projects.es('h2 a')
		texts		= projects.es('p')
		img_links	= projects.es('p + a')
		imgs		= projects.es('img')
		
		for n in range(len(projects_items)):
			i = projects_items[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertIn(i[2], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3] + '/type/banner,project_image,logo/dim/313x214/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach%s/photos/gallery/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		