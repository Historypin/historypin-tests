# -*- coding: utf-8 -*-

from base import *
from sandy import Project_Sandy

class Project_After_Sandy(Project_Sandy):
	
	PROJECT_URL = '/project/28-after-sandy'
	
	ATTACH_TABS = [
		'{0}/attach{1}/map/index/'			.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/gallery/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/stories/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/slideshow/'	.format(URL_BASE, PROJECT_URL),
	]
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('After Sandy | Home')
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('{0}/project/26-sandy/'.format(URL_BASE)		, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('After Sandy'																, tout.e('h2').text)
		self.assertEqual('Explore how people are starting to rebuild their homes and communities.'	, tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('{0}/project/26-sandy/upload/projects/?subproject=28'.format(URL_BASE), button_upload.get_attribute('href'))
		self.assertEqual('Contribute'													, button_upload.e('span').text)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'		, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['During Sandy'		, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
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
			self.assertEqual('{0}/project/{1}'.format(URL_BASE, i[1]), h2s_links[n].get_attribute('href'))
			self.assertEqual('{0}/project/{1}'.format(URL_BASE, i[1]), img_links[n].get_attribute('href'))
			self.assertIn(i[2], texts[n].text)
			self.assertEqual('{0}/projects/img/pid/{1}/type/banner,project_image,logo/dim/313x214/crop/1/'.format(URL_BASE, i[3]), imgs[n].get_attribute('src'))
		
		self.assertEqual('{0}/attach{1}/photos/gallery/'.format(URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		