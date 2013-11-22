# -*- coding: utf-8 -*-

from base import *
from npower import Project_NPower

class Project_NPower_KeepWarm(Project_NPower):
	
	PROJECT_URL = '/project/16-remember-keep-warm'
	
	ATTACH_TABS = [
		['%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/gallery/' % (URL_BASE, PROJECT_URL), '%s/attach%s/photos/stories/' % (URL_BASE, PROJECT_URL)],
	]
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Keep Warm | Home')
		
		site_cnt = self.e('#site-content')
		desc = site_cnt.e('.right > a')
		
		self.assertEqual('%s/project/15-remember/' % URL_BASE, desc.get_attribute('href'))
		self.assertEqual('%s/projects/img/pid/16/type/logo/dim/600x120/' % URL_BASE	, desc.e('img').get_attribute('src'))
		
		self.assertEqual('Curled up by the hearth with the dog, terrible Christmas jumpers, bedtime stories, coal fires, agas, cocoa and bed warmers galore!', site_cnt.e('.right p').text)
		
		button_upload = site_cnt.e('.left a')
		
		self.assertEqual('%s/project/15-remember/upload/projects/bridge/1/?subproject=16' % URL_BASE, button_upload.get_attribute('href'))
		self.assertEqual('Pin your memories'													, button_upload.e('span').text)
		
		self.assertEqual('Explore more', site_cnt.e('.cf h3').text)
		
		projects = [
			['Play'				, '18-remember-play/'				, '18'],
			['Cook and Clean'	, '19-remember-cook-and-clean/'		, '19'],
			['Celebrate'		, '21-remember-celebrate/'			, '21'],
			['Watch and Listen'	, '23-remember-watch-and-listen/'	, '23'],
			['Work'				, '24-remember-work/'				, '24'],
		]
		
		h2s = self.es('.w5 h2')
		h2s_links = self.es('.w5 h2 a')
		img_links = self.es('.w5 a:nth-child(2)')
		imgs = self.es('.w5 a:nth-child(2) img')
		
		for n in range(len(projects)):
			i = projects[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[2] + '/type/project_image,banner_image/dim/320x144/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach%s/photos/gallery/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
