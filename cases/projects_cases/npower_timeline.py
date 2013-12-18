# -*- coding: utf-8 -*-

from base import *

class Project_Timeline(HPTestCase):
	@url('/project/31-remember-timeline')
	def test_index(self):
		
		self.assertTitle('Timeline of Inventions | Home')
		
		site_cnt = self.e('#site-content')
		desc = site_cnt.e('.right')
		
		self.assertEqual('%s/project/15-remember/' % URL_BASE							, desc.e('a').get_attribute('href'))
		self.assertEqual('%s/projects/img/pid/31/type/logo/dim/600x120/' % URL_BASE		, desc.e('a img').get_attribute('src'))
		
		self.assertIn('Energy and technological advances over the last century have revolutionised the way we work', desc.e('p').text)
		
		button_upload = site_cnt.e('.left a')
		
		self.assertEqual('%s/project/15-remember/upload/' % URL_BASE, button_upload.get_attribute('href'))
		self.assertEqual('Pin your memories'						, button_upload.e('span').text)
		
		
		paragraph = self.e('#site-content > p')
		self.assertEqual('In partnership with', paragraph.e('span').text)
		
		partners = [
			['http://www.npower.com/'	, 'npower_logo.png'],
			['http://www.mirrorpix.com/', 'mirrorpix.jpg'],
		]
		
		links	= paragraph.es('a')
		imgs	= paragraph.es('a img')
		
		for n in range(len(partners)):
			i = partners[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/resources/images/webapps/npower/' + i[1], imgs[n].get_attribute('src'))
		
		back_project = site_cnt.e('h3 a')
		self.assertEqual('%s/project/15-remember/' % URL_BASE, back_project.get_attribute('href'))
		self.assertEqual('Back to project'					, back_project.text)
		
		self.go('/attach/project/31-remember-timeline/photos/timeline/')
		
		sleep(3)
		
		timeline	= self.e('#my-timeline')
		
		self.assertIsInstance(timeline.e('.date')	, WebElement)
		self.assertIsInstance(timeline.e('h3')	, WebElement)
		self.assertIsInstance(timeline.e('img')	, WebElement)
		
		nav_next = timeline.e('.nav-next')
		
		self.assertIsInstance(nav_next.e('.date')	, WebElement)
		self.assertIsInstance(nav_next.e('.title')	, WebElement)
		nav_next.e('.icon').click()
		
		nav_prev = timeline.e('.nav-previous')
		self.assertIsInstance(nav_prev.e('.date')	, WebElement)
		self.assertIsInstance(nav_prev.e('.title')	, WebElement)
		
		self.assertIsInstance(self.e('.vco-navigation'), WebElement)
		
