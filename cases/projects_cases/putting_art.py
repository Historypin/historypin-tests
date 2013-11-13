# -*- coding: utf-8 -*-

from base import *

class Project_PuttingArt(HPTestCase):
	@url('/project/41-putting-art-on-the-map')
	def test_index(self):
		
		self.assertTitle('Putting Art on the Map | Home')
		
		self.assertEqual('%s/projects/img/dim/1020x250/crop/1/image_id/133' % URL_BASE, self.e('#banner_images img').get_attribute('src'))
		
		site_cnt = self.e('#site-content')
		self.assertIn('From John Singer Sargent to Paul Nash, some amazing artists captured scenes of the First World War.', site_cnt.e('.page-top p:nth-of-type(1)').text)
		
		twitter_link = site_cnt.e('.page-top p:nth-of-type(2) a')
		
		self.assertEqual('https://twitter.com/search?q=%23artmap', twitter_link.get_attribute('href'))
		self.assertEqual('#artmap', twitter_link.text)
		
		self.assertEqual('%s/attach/project/41-putting-art-on-the-map/mysteries/index/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		tout_items = [
			['Live event in York'	, 'tout1_image', 'Read about our live crowdsourcing session in York'					, '/?p=4021'],
			['Curate our artworks'	, 'tout2_image', 'Create your own Collection or Tour with the First World War artworks.', '/?p=3765'],
		]
		
		h3s			= site_cnt.es('.tout.w2 h3')
		images		= site_cnt.es('.tout.w2 img')
		paragraphs	= site_cnt.es('.tout.w2 p')
		h3s_link	= site_cnt.es('.tout.w2 h3 a')
		images_link	= site_cnt.es('.tout.w2 p + a')
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/41/dim/270x310/type/' + i[1] + '/crop/1/', images[n].get_attribute('src'))
			self.assertEqual(i[2], paragraphs[n].text)
			self.assertEqual('http://blog.historypin.com' + i[3], h3s_link[n].get_attribute('href'))
			self.assertEqual('http://blog.historypin.com' + i[3], images_link[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		li_first = activity.e('li:first-of-type')
		
		self.assertIsInstance(li_first.e('a')		, WebElement)
		self.assertIsInstance(li_first.e('a img')	, WebElement)
		self.assertIsInstance(li_first.e('p')		, WebElement)
		self.assertIsInstance(li_first.e('p a')		, WebElement)
		
		icon_tout1	= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://blog.historypin.com/?p=3750'	, icon_tout1.get_attribute('href'))
		self.assertEqual('Find out more'		, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2	= site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://blog.historypin.com/category/putting-art-on-the-map/'	, icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'								, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper'	, icon_tout2.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		partners_items = [
			['http://www.iwm.org.uk/'			, 'cent-logo.png'],
			['http://www.ed.ac.uk/home'			, 'uoe-logo.png'],
			['http://www.artsdigitalrnd.org.uk/', 'lottery-funded-logo.png'],
		]
		
		partners	= self.e('.partner-logos')
		h5s			= partners.es('h5')
		links		= partners.es('a')
		images		= partners.es('img')
		
		self.assertEqual('In partnership with'	, h5s[0].text)
		self.assertEqual('With support from'	, h5s[1].text)
		
		for n in range(len(partners_items)):
			i = partners_items[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(URL_BASE + '/resources/images/project-putting-art/' + i[1], images[n].get_attribute('src'))
		