# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_HPJapan(HPTestCase, Attach):
	
	PROJECT_URL				= '/project/39-japan-project'
	ATTACH_URL				= '/jp/attach'
	FUJINOMIYA_LINK			= '%s/project/47-fujinomiya-project' % URL_BASE
	blog_link				= 'http://blog.historypin.jp'
	
	ATTACH_TABS = [
		'%s/photos/gallery/'	% PROJECT_URL,
		'%s/map/index/'			% PROJECT_URL
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_gallery	= Attach.attach_tab_gallery
	test_tab_map		= Attach.attach_tab_map
	
	
	def __test_main_touts(self):
		
		touts_items = [
			['%s/' % self.FUJINOMIYA_LINK	, u'富士宮プロジェクト'	, u'富士宮プロジェクトページを見る'	, 'tout1_image'],
			['%s/' % self.blog_link			, u'ブログ'			, u'Historypin Japan の最新情報', 'tout2_image'],
		]
		
		h3s_links	= self.es('.w23 .inner h3 a')
		paragraphs	= self.es('.w23 .inner p')
		imgs_links	= self.es('.w23 .inner p + a')
		imgs		= self.es('.w23 .inner a img')
		
		for n in range(len(touts_items)):
			i = touts_items[n]
			self.assertEqual(i[0], h3s_links[n].get_attribute('href'))
			self.assertEqual(i[0], imgs_links[n].get_attribute('href'))
			self.assertEqual(i[1], h3s_links[n].text)
			self.assertEqual(i[2], paragraphs[n].text)
			self.assertEqual(URL_BASE + '/projects/img/pid/39/dim/285x290/type/' + i[3] + '/crop/1/', imgs[n].get_attribute('src'))
		
		sleep(3)
		
		activity = self.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual(u'総投稿数', activity.e('h6').text)
		
		item_feed = self.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
	
	def __test_icon_touts(self):
		
		site_cnt	= self.e('#site-content')
		icon_tout1	= site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('http://www.historypin.com/', icon_tout1.get_attribute('href'))
		self.assertEqual(u'Historypin.com (グローバルサイト）へ移動)'	, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-desktop'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://www.historypin.com/channels/'		, icon_tout2.get_attribute('href'))
		self.assertEqual(u'Explore Historypin Channels in English'	, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-search'	, icon_tout2.e('span').get_attribute('class'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
	
	def __test_footer(self):
		
		supported = self.e('.footer .supported_by')
		self.assertEqual(u'パートナー', supported.e('span').text)
		# self.assertEqual('http://www.glocom.ac.jp/project/historypin/fujinomiya', supported.e('a').get_attribute('href'))
		
		logo_link	= supported.es('a')
		logo_img	= supported.es('img')
		
		self.assertEqual('http://www.britishcouncil.jp/', logo_link[0].get_attribute('href'))
		self.assertEqual('%s/resources/images/project-japan/british-council-logo.png' % URL_BASE, logo_img[0].get_attribute('src'))
		
		footer = self.e('.footer-links')
		footer_links = footer.es('a')
		
		footer_items = [
			['%s/terms-and-conditions/'	% self.blog_link	, 'Terms and conditions'],
			['%s/privacy-policy/'		% self.blog_link	, 'Privacy policy'],
			['%s/cookies/'				% self.blog_link	, 'Cookies'],
			['http://wearewhatwedo.org/'			, u'© We Are What We Do'],
		]
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
	
	@unittest.skipIf('historypin.com' in LINK_BASE, 'test will skip if LINK_BASE is historypin')
	def test_index(self):
		self.go('/jp' + self.PROJECT_URL)
		
		self.assertTitle(u'Historypin 日本上陸！')
		
		site_cnt = self.e('#site')
		nav_links = site_cnt.es('.primary a')
		
		self.assertEqual('%s/resources/images/project-japan/historypin-logo.png' % URL_BASE, nav_links[0].e('img').get_attribute('src'))
		self.assertEqual('http://www.historypin.jp/', nav_links[0].get_attribute('href'))
		
		self.assertEqual('%s/jp%s/' % (URL_BASE, self.PROJECT_URL), nav_links[1].get_attribute('href'))
		self.assertEqual(u'ホーム', nav_links[1].text)
		
		self.assertEqual('%s/jp%s/explore/#|map/' % (URL_BASE, self.PROJECT_URL), nav_links[2].get_attribute('href'))
		self.assertEqual(u'探索', nav_links[2].text)
		
		self.assertEqual('%s/jp%s/upload/' % (URL_BASE, self.PROJECT_URL), nav_links[3].get_attribute('href'))
		self.assertEqual(u'投稿', nav_links[3].text)
		
		self.assertEqual('%s/' % self.blog_link		, nav_links[4].get_attribute('href'))
		self.assertEqual(u'ブログ', nav_links[4].text)
		
		self.assertEqual('%s/about/' % self.blog_link		, nav_links[5].get_attribute('href'))
		self.assertEqual(u'Historypin Japan について', nav_links[5].text)
		
		self.assertEqual('%s/faq/' % self.blog_link		, nav_links[6].get_attribute('href'))
		self.assertEqual(u'よくある質問', nav_links[6].text)
		
		user_links = site_cnt.es('.secondary a')
		
		self.assertEqual('%s/jp%s/user/' % (URL_BASE, self.PROJECT_URL), user_links[0].get_attribute('href'))
		self.assertEqual(u'アカウント作成', user_links[0].text)
		
		self.assertEqual('%s/jp%s/user/' % (URL_BASE, self.PROJECT_URL), user_links[1].get_attribute('href'))
		self.assertEqual(u'ログイン', user_links[1].text)
		
		self.assertIn(u'Historypinは、世界中の人々が自分たちのコミュ', self.e('.intro p').text)
		
		button_items = [
			['/explore/#|map/'	, u'探索する'],
			['/upload/'			, u'投稿する'],
		]
		
		buttons			= self.e('.buttons')
		buttons_links	= buttons.es('a')
		
		for n in range(len(button_items)):
			i = button_items[n]
			self.assertEqual(URL_BASE + '/jp' + self.PROJECT_URL + i[0], buttons_links[n].get_attribute('href'))
			self.assertEqual(i[1], buttons_links[n].e('span').text)
		
		self.assertEqual('%s/resources/images/project-japan/home-bg.jpg' % URL_BASE, self.e('.intro img').get_attribute('src'))
		
		self.__test_main_touts()
		self.__test_icon_touts()
		self.__test_footer()
	
	@unittest.skipIf('historypin.com' in LINK_BASE, 'test will skip if the LINK_BASE is historypin')
	def test_explore(self):
		self.go('/jp' + self.PROJECT_URL)
		
		self.assertTitle(u'Historypin 日本上陸！')
		
		self.assertEqual('%s/jp/attach%s/map/index/' % (URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		self.__test_main_touts()
		self.__test_icon_touts()
		self.__test_footer()
