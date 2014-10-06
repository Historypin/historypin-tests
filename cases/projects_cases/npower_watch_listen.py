# -*- coding: utf-8 -*-

from base import *
from npower import Project_NPower

class Project_NPower_Watch_Listen(Project_NPower):
	
	PROJECT_URL = '/project/23-remember-watch-and-listen'
	
	ATTACH_TABS = [
		'{0}/attach{1}/map/index/'		.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/gallery/'	.format(URL_BASE, PROJECT_URL),
		'{0}/attach{1}/photos/stories/'	.format(URL_BASE, PROJECT_URL),
	]
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Watch and Listen | Home')
		
		site_cnt = self.e('#site-content')
		desc = site_cnt.e('.right > a')
		
		self.assertEqual('{0}/project/15-remember/'.format(URL_BASE)						, desc.get_attribute('href'))
		self.assertEqual('{0}/projects/img/pid/23/type/logo/dim/600x120/'.format(URL_BASE)	, desc.e('img').get_attribute('src'))
		
		self.assertEqual('Bigger and boxier! Enormous tellies, impressive vinyl collections, the original home videos and technological classics.', site_cnt.e('.right p').text)
		
		button_upload = site_cnt.e('.left a')
		
		self.assertEqual('{0}/project/15-remember/upload/projects/bridge/1/?subproject=23'.format(URL_BASE), button_upload.get_attribute('href'))
		self.assertEqual('Pin your memories'														, button_upload.e('span').text)
		
		projects = [
			['Keep Warm'		, '16-remember-keep-warm/'			, '16'],
			['Play'				, '18-remember-play/'				, '18'],
			['Cook and Clean'	, '19-remember-cook-and-clean/'		, '19'],
			['Celebrate'		, '21-remember-celebrate/'			, '21'],
			['Work'				, '24-remember-work/'				, '24'],
		]
		
		h2s			= self.es('.w5 h2')
		h2s_links	= self.es('.w5 h2 a')
		img_links	= self.es('.w5 a:nth-child(2)')
		imgs		= self.es('.w5 a:nth-child(2) img')
		
		for n in range(len(projects)):
			i = projects[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual('{0}/project/{1}'.format(URL_BASE, i[1]), h2s_links[n].get_attribute('href'))
			self.assertEqual('{0}/project/{1}'.format(URL_BASE, i[1]), img_links[n].get_attribute('href'))
			self.assertEqual('{0}/projects/img/pid/{1}/type/project_image,banner_image/dim/320x144/crop/1/'.format(URL_BASE, i[2]), imgs[n].get_attribute('src'))
		
		self.assertEqual('{0}/attach{1}/photos/gallery/'.format(URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
