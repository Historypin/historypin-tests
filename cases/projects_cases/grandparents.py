# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Grandparents(HPTestCase, Attach):
	
	PROJECT_URL = '/project/10-grandparents'
	
	ATTACH_TABS = [
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Amazing Grandparents | Home')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('My Grandparents are better than yours', site_cnt.e('h1').text)
		
		self.assertIn('Is your Gran, Grandad, Nan or Pops awesome?', site_cnt.e('.page-top p').text)
		
		hp_link = 'http://www.historypin.com'
		
		img_link = '%s/resources/images/webapps/grandparents/' % URL_BASE
		wawwd_link = 'http://wawwd-resources.s3.amazonaws.com/historypin/images/community/'
		
		touts = [
			['Scan your Gran, tag your Grandad!'	, '%s%s/upload/' % (URL_BASE, self.PROJECT_URL)	, '%smain_pin_img.jpg' % img_link	, 'Was your Gran once a hipster? Your Grandad a legend? Raid your attic and share your photos here.'],
			["Prince William's photo of his Gran"	, '%s/project/5-DiamondJubilee/map/#!/geo:51.339732,-0.767807/zoom:18/dialog:83545/tab:details/' % hp_link	, '%squeen.jpg' % img_link			, 'Have a look at the photo and story that Prince William added of his Gran.'],
			['Useful free resources'				, '%s/community/schools-resources' % hp_link																, '%sschools_main.jpg' % wawwd_link	, 'Download useful resources helping you record stories, run sessions and use Historypin in your school or community.'],
		]
		
		touts_cnt	= self.e('.highlights')
		h2s			= touts_cnt.es('h2')
		links		= touts_cnt.es('a')
		images		= touts_cnt.es('img')
		paragraphs	= touts_cnt.es('p')
		
		for n in range(len(touts)):
			i = touts[n]
			self.assertEqual(i[0], h2s[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
			self.assertEqual(i[2], images[n].get_attribute('src'))
			self.assertEqual(i[3], paragraphs[n].text)
		
		self.assertEqual('%s/attach%s/photos/gallery/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
	