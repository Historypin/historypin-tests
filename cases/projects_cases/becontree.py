# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Becontree(HPTestCase, Attach):
	
	PROJECT_URL = '/project/58-this-used-to-be-fields'
	ATTACH_URL = '/en/attach'
	
	ATTACH_TABS = [
		'{0}/photos/gallery/'.format(PROJECT_URL),
		'{0}/map/index/'		.format(PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_map		= Attach.attach_tab_map
	
	def test_landing_page(self):
		self.go('{0}{1}/'.format(URL_BASE, self.PROJECT_URL))
		
		self.assertTitle('This Used to be Fields')
		
		site_cnt = self.e('.intro')
		
		self.assertEqual('This Used to be Fields', site_cnt.e('h1').text)
		self.assertIn('Across Britain and around the world, the events and effects of the First World War shaped a century of dramatic change and progress.', site_cnt.e('p').text)
		
		buttons_landing_page = site_cnt.e('.buttons')
		
		self.assertEqual('Explore', buttons_landing_page.e('a:nth-of-type(1)').text)
		self.assertEqual('{0}{1}/explore/'.format(URL_BASE, self.PROJECT_URL), buttons_landing_page.e('a:nth-of-type(1)').get_attribute('href'))
		
		self.assertEqual('Contribute', buttons_landing_page.e('a:nth-of-type(2)').text)
		self.assertEqual('{0}{1}/upload/index/'.format(URL_BASE, self.PROJECT_URL), buttons_landing_page.e('a:nth-of-type(2)').get_attribute('href'))
	
	def test_explore_button(self):
		self.go('{0}{1}/'.format(URL_BASE, self.PROJECT_URL))
		
		site_cnt				= self.e('.intro')
		buttons_landing_page	= site_cnt.e('.buttons')
		
		buttons_landing_page.e('a:nth-of-type(1)').click()
		
		explore_title_wrap = self.e('h1.container')
		
		self.assertEqual('{0}{1}/'.format(URL_BASE, self.PROJECT_URL), explore_title_wrap.e('a').get_attribute('href'))
		self.assertEqual('{0}/resources/images/project-barking-and-dagenham/project-title.png'.format(URL_BASE), explore_title_wrap.e('a img').get_attribute('src'))
	
	def test_index(self):
		self.go('{0}{1}/'.format(URL_BASE, self.PROJECT_URL))
		
		tout_items = [
			['Launch of the mural!'	, 'tout1_image', 'Join us to celebrate the new mural in Becontree'		, '/2014/08/31/becontree-mural/'],
			['Get involved'			, 'tout2_image', 'Find out how you can get involved with the project'	, '/2013/06/25/this-used-to-be-fields-get-involved/'],
		]
		
		site_cnt	= self.e('#site-content')
		h3s			= site_cnt.es('.tout.w2 h3')
		images		= site_cnt.es('.tout.w2 img')
		paragraphs	= site_cnt.es('.tout.w2 p')
		h3s_link	= site_cnt.es('.tout.w2 h3 a')
		images_link	= site_cnt.es('.tout.w2 p + a')
		blog_link	= 'http://blog.historypin.com'
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual('{0}/projects/img/pid/58/dim/290x315/type/{1}/crop/1/'.format(URL_BASE, i[1]), images[n].get_attribute('src'))
			self.assertIn(i[2], paragraphs[n].text)
			self.assertEqual(blog_link + i[3], h3s_link[n].get_attribute('href'))
			self.assertEqual(blog_link + i[3], images_link[n].get_attribute('href'))
		
		activity = site_cnt.e('#activity')
		li_first = activity.e('li:first-of-type')
		
		self.assertIsInstance(li_first.e('a')		, WebElement)
		self.assertIsInstance(li_first.e('a img')	, WebElement)
		self.assertIsInstance(li_first.e('p')		, WebElement)
		self.assertIsInstance(li_first.e('p a')		, WebElement)
		
		icon_tout1 = site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('{0}/2013/06/25/this-used-to-be-fields/'.format(blog_link), icon_tout1.get_attribute('href'))
		self.assertEqual('About this project', icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('mailto:steve.rolling@historypin.org', icon_tout2.get_attribute('href'))
		self.assertEqual('Contact us', icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-phone'	, icon_tout2.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		
		partnership = self.e('.partnership')
		
		self.assertEqual('In partnership with', partnership.e('span').text)
		
		self.assertEqual('http://www.lbbd.gov.uk/MuseumsAndHeritage/BoroughArchivesandLocalStudies/Pages/home.aspx', partnership.e('.barking-logo a').get_attribute('href'))
		self.assertEqual('http://createlondon.org/', partnership.e('.create-logo a').get_attribute('href'))
		
		self.assertEqual('Photo credit: Becontree Station, 1955 courtesy of LBBD Archive', self.e('.photo-credits').text)
		
		footer_items = [
			['{0}/terms-and-conditions/'.format(URL_BASE), 'Terms and Conditions'],
			['{0}/privacy-policy/'		.format(URL_BASE), 'Privacy policy'],
			['{0}/cookies/'				.format(URL_BASE), 'Cookies'],
			['http://www.shiftdesign.org.uk/'	, u'\xa9 Shift'],
		]
	
		footer			= self.e('.footer-shadow')
		footer_links	= footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
		