# -*- coding: utf-8 -*-

from base import *
from npower import Project_NPower

class Project_NPower_Celebrate(Project_NPower):
	
	PROJECT_URL = '/project/21-remember-celebrate'
	
	ATTACH_TABS = [
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/stories/'	% (URL_BASE, PROJECT_URL)
	]
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Celebrate | Home')
		
		site_cnt = self.e('#site-content')
		desc = site_cnt.e('.right > a')
		
		self.assertEqual('%s/project/15-remember/' % URL_BASE						, desc.get_attribute('href'))
		self.assertEqual('%s/projects/img/pid/21/type/logo/dim/600x120/' % URL_BASE	, desc.e('img').get_attribute('src'))
		
		self.assertEqual('Dancing, decorations, parties! The bright lights of Christmas, bonfires and fireworks, wedding snaps with dodgy dos and birthdays from our youth.', site_cnt.e('.right p').text)
		
		button_upload = site_cnt.e('.left a')
		
		self.assertEqual('%s/project/15-remember/upload/projects/bridge/1/?subproject=21' % URL_BASE, button_upload.get_attribute('href'))
		self.assertEqual('Pin your memories'														, button_upload.e('span').text)
		
		self.assertEqual('Explore more', site_cnt.e('.cf h3').text)
		
		projects = [
			['Keep Warm'		, '16-remember-keep-warm/'			, '16'],
			['Play'				, '18-remember-play/'				, '18'],
			['Cook and Clean'	, '19-remember-cook-and-clean/'		, '19'],
			['Watch and Listen'	, '23-remember-watch-and-listen/'	, '23'],
			['Work'				, '24-remember-work/'				, '24'],
		]
		
		h2s			= self.es('.w5 h2')
		h2s_links	= self.es('.w5 h2 a')
		img_links	= self.es('.w5 a:nth-child(2)')
		imgs		= self.es('.w5 a:nth-child(2) img')
		
		for n in range(len(projects)):
			i = projects[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[2] + '/type/project_image,banner_image/dim/320x144/crop/1/', imgs[n].get_attribute('src'))
		
		self.assertEqual('%s/attach%s/photos/gallery/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		