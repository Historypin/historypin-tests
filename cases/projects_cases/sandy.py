# -*- coding: utf-8 -*-

from base import *

class Project_Sandy(HPTestCase):
	@url('/project/26-sandy/')
	def test_index(self):
		
		site_cnt = self.e('#site-content')
		h1_link = site_cnt.e('h1 a')
		self.assertEqual('%s/project/26-sandy' % URL_BASE				, h1_link.get_attribute('href'))
		self.assertEqual('Hurricane Sandy:\nRecord, Remember, Rebuild'	, h1_link.text)
		
		tout = site_cnt.e('.text-tout')
		self.assertEqual('Hurricane Sandy', tout.e('h2').text)
		self.assertIn('How have communities and neighborhoods in the Caribbean and United States been affected by Sandy?', tout.e('p').text)
		
		button_upload = tout.e('a')
		self.assertEqual('%s/project/26-sandy/upload/' % URL_BASE	, button_upload.get_attribute('href'))
		self.assertEqual('Contribute'								, button_upload.e('span').text)
		
		self.assertEqual('%s/projects/img/pid/26/type/project_image/dim/665x406/crop/1/' % URL_BASE, site_cnt.e('.main-image img').get_attribute('src'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('memories and materials contributed so far', activity.e('h6').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		projects = site_cnt.e('.highlights.cf')
		
		projects_items = [
			['Before Sandy'	, '27-before-sandy/', 'What did neighborhoods in the US and the Caribbean look like before Sandy?'			, '27'],
			['After Sandy'	, '28-after-sandy/'	, 'Explore how people are starting to rebuild their homes and communities.'				, '28'],
			['During Sandy'	, '29-during-sandy/', 'Memories and materials from when Sandy passed through communities and neighborhoods.', '29'],
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
			self.assertEqual(i[2], texts[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3] + '/type/banner,project_image,logo/dim/313x214/crop/1/', imgs[n].get_attribute('src'))
		
	
	@url('/project/26-sandy/')
	def test_before_sandy(self):
		pass
	
	@url('/project/26-sandy/')
	def test_during_sandy(self):
		pass
	
	@url('/project/26-sandy/')
	def test_after_sandy(self):
		pass
	
	@url('/project/26-sandy/')
	def test_donate(self):
		pass
