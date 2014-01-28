# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_NPower(HPTestCase, Attach):
	
	PROJECT_URL = '/project/15-remember'
	
	ATTACH_TABS = [
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/stories/'	% (URL_BASE, PROJECT_URL)
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_comments	= Attach.attach_tab_comments
	
	def __test_touts(self):
		
		site_cnt = self.e('#site-content')
		
		icon_tout1 = site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('%s/project/31-remember-timeline/' % URL_BASE, icon_tout1.get_attribute('href'))
		self.assertEqual('Explore our timeline of inventions\nover the last century', icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-activity'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://blog.historypin.com/category/remember-how-we-used-to/'		, icon_tout2.get_attribute('href'))
		self.assertEqual('Check out our blog for all the latest\nnews and community updates', icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, icon_tout2.e('span').get_attribute('class'))
		
	def __test_channels(self):
		
		site_cnt = self.e('#site-content')
		bottom_p = site_cnt.e('.bottom-p')
		
		self.assertIn('Featured photos shared by', bottom_p.text)
		
		channels = [
			['571038/'	, 'Mirrorpix'],
			['8759065/'	, 'Dawn Parsonage'],
			['8285366/'	, 'The Benevolent Society'],
			['3036003/'	, 'Science and Society Picture Library'],
			['6900604/'	, 'Reading Post'],
			['14424002/', 'npower archive'],
		]
			
		channels_links = bottom_p.es('a')
		
		for n in range(len(channels)):
			i = channels[n]
			self.assertEqual(URL_BASE + '/channels/view/' + i[0], channels_links[n].get_attribute('href'))
			self.assertEqual(i[1], channels_links[n].text)
		
		last_paragraph = self.e('.bottom-p + p')
		self.assertEqual('In partnership with', last_paragraph.e('span').text)
		
		
		partners = [
			['http://www.npower.com/'	, 'npower_logo.png'],
			['http://www.mirrorpix.com/', 'mirrorpix.jpg'],
		]
		
		links	= last_paragraph.es('a')
		imgs	= last_paragraph.es('a img')
		
		for n in range(len(partners)):
			i = partners[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/resources/images/webapps/npower/' + i[1], imgs[n].get_attribute('src'))
		
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Remember how we used to... | Home')
		
	
		site_cnt = self.e('#site-content')
		desc = site_cnt.e('.right > a')
		
		self.assertEqual('%s%s/' % (URL_BASE, self.PROJECT_URL)						, desc.get_attribute('href'))
		self.assertEqual('%s/projects/img/pid/15/type/logo/dim/600x120/' % URL_BASE	, desc.e('img').get_attribute('src'))
		
		links = site_cnt.es('.right p a')
		
		self.assertEqual('%s/channels/view/id/39451/' % URL_BASE, links[0].get_attribute('href'))
		self.assertEqual('npower'	, links[0].text)
		self.assertEqual('%s/channels/view/id/19/'	% URL_BASE	, links[1].get_attribute('href'))
		self.assertEqual('Mirrorpix', links[1].text)
		
		self.assertIn('Work, play, watch and listen, cook and clean, keep warm and celebrate. How did you and your family used to do things?', site_cnt.e('.right p').text)
		
		button_upload = site_cnt.e('.left a')
		
		self.assertEqual('%s%s/upload/' % (URL_BASE, self.PROJECT_URL), button_upload.get_attribute('href'))
		self.assertEqual('Pin your memories'						, button_upload.e('span').text)
		
		
		projects = [
			['Keep Warm'		, '16-remember-keep-warm/'			, '16', 'Curled up by the hearth with the dog, terrible Christmas jumpers,'],
			['Play'				, '18-remember-play/'				, '18', 'Classic console games and arcade machines.'],
			['Cook and Clean'	, '19-remember-cook-and-clean/'		, '19', 'Dirty dishes in the days before dishwashers,'],
			['Celebrate'		, '21-remember-celebrate/'			, '21', 'Dancing, decorations, parties!'],
			['Watch and Listen'	, '23-remember-watch-and-listen/'	, '23', 'Bigger and boxier!'],
			['Work'				, '24-remember-work/'				, '24', 'Offices, factories, schools or shops or wherever you could make a bob.'],
		]
		
		h2s				= self.es('.w3 h2')
		h2s_links		= self.es('.w3 h2 a')
		img_links		= self.es('.w3 a:nth-child(2)')
		imgs			= self.es('.w3 img')
		texts			= self.es('.w3 p')
		paragraph_links	= self.es('.w3 p a')
		
		for n in range(len(projects)):
			i = projects[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(URL_BASE + '/project/' + i[1], h2s_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], img_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/project/' + i[1], paragraph_links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[2] + '/type/project_image,banner_image/dim/320x144/crop/1/', imgs[n].get_attribute('src'))
			self.assertIn(i[3], texts[n].text)
		
		self.__test_touts()
		self.__test_channels()
		
		self.assertEqual('%s/attach%s/photos/gallery/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
	
