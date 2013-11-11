# -*- coding: utf-8 -*-

from base import *

class Project_Olympics(HPTestCase):
	@url('/project/3-hp-olympics/')
	def test_index(self):
		
		self.assertTitle('Olympic memories | Home')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Olympic memories', site_cnt.e('h1').text)
		
		self.assertIn('There have been world record numbers of world records, jetpacks at opening ceremonies, boycotts from sparring nations, and all those British medals at the 2012 extravaganza in London. ', site_cnt.e('.main_description').text)
		
		olympics_link	= '%s/project/3-hp-olympics' % URL_BASE
		wawwd_link		= 'http://wawwd-resources.s3.amazonaws.com/historypin/projects/olympics/'
		img_link		= '%s/resources/images/webapps/hp-olympics/' % URL_BASE
		
		touts = [
			['Pin your Olympic Content'			, '%s/upload/' % olympics_link		, '%smain_pin_img.jpg' % img_link		, 'Add any photos, videos or memories from the Olympics\nthrough the ages to this collection here.'],
			['Explore our Olympic timeline'		, '%s/#' % olympics_link			, '%solympic_timeline.jpg' % img_link	, 'Odd photos, little known facts and a potted history of the Olympic Games from 1896 to 2012'],
			['Free downloadable activity pack'	, '%sACTIVITY_PACK.zip' % wawwd_link, '%sdownload_img.jpg' % img_link		, 'Perfect for schools and groups, it includes lesson plans, a game and tipsheets for gathering photos'],
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
		self.assertIsInstance(self.e('.olympics_dialog'), WebElement)
		self.e('.ui-dialog-titlebar-close.ui-corner-all').click()
		
		self.assertEqual(URL_BASE + '/attach/project/3-hp-olympics/photos/index/', self.e('#embed-frame').get_attribute('src'))
	