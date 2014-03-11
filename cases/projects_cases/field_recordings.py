# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_FieldRecordings(HPTestCase, Attach):
	
	PROJECT_URL = '/project/53-can-you-help-us-enrich-these-field-recordings-of-b'
	ATTACH_TABS = [
		'%s/attach%s/map/index/'	% (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	# test_tab_map		= Attach.attach_tab_map  #TODO fix this - this won't work because there is no content to be clicked on the map
	
	# TODO add tabs, if there is one and when they are added
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Can you help us enrich these field recordings of bird sounds? | Home')
		
		self.assertEqual('%s/projects/img/dim/1000x250/crop/1/image_id/203' % URL_BASE, self.e('#banner_images li img').get_attribute('src'))
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual('Can you help us enrich these field recordings of bird sounds?', site_cnt.e('h1').text)
		self.assertIn('The British Library and Netherlands Institute for Sound and Vision have many recordings of bird sounds from across the UK and Netherlands.', site_cnt.e('.main_description').text)
		
		self.assertEqual('%s/attach%s/map/index/' % (URL_BASE, self.PROJECT_URL), site_cnt.e('#embed-frame').get_attribute('src'))
		
		# TODO fix this items when links are provided
		
		touts_items = [
			['Explore Europeana Records'						, 'Europeana offers access to 30 million cultural'	, 'tout1_image'],
			['Do you have relevant photos, video and audio?'	, 'Upload them and pin them to the map.'			, 'tout2_image'],
		]
		
		h3s_links	= site_cnt.es('.w23 .inner h3')
		paragraphs	= site_cnt.es('.w23 .inner p')
		# imgs_links	= site_cnt.es('.w23 .inner p + a')
		imgs		= site_cnt.es('.w23 .inner img')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			# self.assertEqual(tout_yarra_link + i[0], h3s_links[n].get_attribute('href'))
			# self.assertEqual(i[0], imgs_links[n].get_attribute('href'))
			self.assertEqual(i[0], h3s_links[n].text)
			self.assertIn(i[1], paragraphs[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/53/dim/270x310/type/' + i[2] + '/crop/1/', imgs[n].get_attribute('src'))
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('contributions made so far', activity.e('h6').text)
		
		self.assertEqual('Share:', self.e('.addthis_toolbox h3').text)
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		self.assertEqual('Image credit: XXXXXXXXXXXXXXXXXXXXX', self.e('.image-credits').text)
		
		# TODO test first item from the activity feed, when there is one
