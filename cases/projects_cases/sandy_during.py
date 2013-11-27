# -*- coding: utf-8 -*-

from base import *
from sandy import Project_Sandy

class Project_During_Sandy(Project_Sandy):
	
	PROJECT_URL = '/project/29-during-sandy'
	
	ATTACH_TABS = [
		['%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/gallery/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/stories/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/slideshow/' % (URL_BASE, PROJECT_URL)]
	]
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('During Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy/' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('During Sandy'																			, tout.e('h2').text)
		self.assertEqual('Memories and materials from when Sandy passed through communities and neighborhoods.'	, tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/projects/?subproject=29' % URL_BASE, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'													, button_upload.e('span').text)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'		, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['After Sandy'		, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
			['Hurricane Sandy'	, '26-sandy/'		, 'How have communities and neighborhoods in the Caribbean and United States been affected by Sandy?', '26'],
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
		