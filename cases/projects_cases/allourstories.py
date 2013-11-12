# -*- coding: utf-8 -*-

from base import *

class Project_AllOurStories(HPTestCase):
	@url('/project/44-all-our-stories')
	def test_index(self):
		
		self.assertTitle('All Our Stories | Home')
		
		self.assertEqual(URL_BASE + '/projects/img/dim/1000x250/crop/1/image_id/146', self.e('#banner_images img').get_attribute('src'))
		
		proj_link = '%s/project/44-all-our-stories' % URL_BASE
		site_cnt = self.e('#site-content')
		desc_main = site_cnt.e('.main_description')
		
		self.assertIn('During 2013 over 500 organisations were awarded grants for dynamic', desc_main.text)
		
		button_proj = desc_main.e('a')
		self.assertEqual('%s/channels/'	% proj_link, button_proj.get_attribute('href'))
		self.assertEqual('All Our Stories projects'							, button_proj.e('span').text)
		
		link_section = site_cnt.e('.additional-links')
		
		self.assertEqual('Are you an All Our Stories grantee?', link_section.e('h3').text)
		
		links = link_section.es('a')
		
		hrefs = [
			['https://s3-eu-west-1.amazonaws.com/wawwd-resources/HLF_AOS_Historypin+Guide_Final.pdf', 'Read the Get Started Guide'],
			['%s/user/?from=/project/44-all-our-stories/channels/set_type/'				% proj_link	, 'Register'],
			['%s/upload/'																% proj_link	, 'Upload your digital records'],
		]
		
		for n in range(len(hrefs)):
			i = hrefs[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
		
		activity = site_cnt.e('#activity')
		
		self.assertIsInstance(activity.e('.counter')		, WebElement)
		self.assertEqual('pieces of content added so far'	, activity.e('h6').text)
		
		item_first = activity.es('.activity li:first-of-type a')
		
		self.assertIsInstance(item_first[0], WebElement)
		self.assertIsInstance(item_first[0].e('img'), WebElement)
		self.assertIsInstance(item_first[1], WebElement)
		self.assertIsInstance(item_first[2], WebElement)
		
		self.assertEqual('%s/attach/project/44-all-our-stories/map/index/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
	
	@url('/project/44-all-our-stories/channels/')
	def test_projects(self):
		
		self.assertTitle('All Our Stories | Featured Channels')
		
		button_home = self.e('.button-wrapper a')
		self.assertEqual('%s/project/44-all-our-stories/' % URL_BASE, button_home.get_attribute('href'))
		self.assertEqual('Home', button_home.e('span').text)
		
		channel = self.e('.channels-list li:first-of-type')
		self.assertIsInstance(channel.e('.logo'), WebElement)
		self.assertIsInstance(channel.e('.name'), WebElement)
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
	