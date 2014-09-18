# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Chevy(HPTestCase, Attach):
	
	PROJECT_URL = '/project/8-chevy'
	
	ATTACH_TABS = [
		'%s/attach%s/map/index/'		% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/slideshow/'	% (URL_BASE, PROJECT_URL),
		'%s/attach%s/photos/gallery/'	% (URL_BASE, PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Me and My Chevy | Home')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Me and My Chevy', site_cnt.e('h1').text)
		
		self.assertIn(u'Since the first Chevrolet car appeared on our streets in 1911, Chevys have been a massive part of our culture.', site_cnt.e('.main_description').text)
		
		chevy_channel = site_cnt.e('.page-top a')
		self.assertEqual('%s/channels/view/id/28802/' % URL_BASE, chevy_channel.get_attribute('href'))
		
		img_link	= '%s/resources/images/webapps/chevy/' % URL_BASE
		
		touts = [
			['Pin your Chevy memories'			, '%s%s/upload' % (URL_BASE, self.PROJECT_URL)	, '%stout1.jpg' % img_link	, 'Add photos, videos and memories for each one of the Chevy models created over the last 100 years.'],
			['100 Years of Chevy Icons'			, '%s%s#' % (URL_BASE, self.PROJECT_URL)		, '%stout2.jpg' % img_link	, 'From the Series C Classic 6 in 1911 to the 2012 Sonic, check out these design icons.'],
			['See Louis Chevrolet himself'		, '%s/photos/#!/geo:41.416981,-87.365314/zoom:10/date_from:1905-01-01/date_to:1912-12-31/dialog:51753/tab:details/' % URL_BASE, '%stout3.jpg' % img_link, 'The founder of Chevrolet racing in the Cobe Cup Race in Indiana in 1909.'],
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
		
		links[1].click()
		self.assertIsInstance(self.e('.chevy_dialog'), WebElement)
		self.e('.ui-dialog-titlebar-close.ui-corner-all').click()
		
		self.assertEqual('%s/attach%s/map/index/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
