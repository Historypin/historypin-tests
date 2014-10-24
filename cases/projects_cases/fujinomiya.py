# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Fujinomiya(HPTestCase, Attach):
	
	PROJECT_URL		= '/project/47-fujinomiya-project'
	ATTACH_URL		= '{0}/jp/attach'.format(URL_ROOT_JP)
	LOCATION_URL	= '/geo:35.224715,138.612945/zoom:21/'
	blog_link		= 'http://blog.historypin.jp'
	
	ATTACH_TABS = [
		'{0}/map/index/'		.format(PROJECT_URL),
		'{0}/photos/gallery/'	.format(PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	
	# TODO location.url to set the location in the attach for map tab
	
	def test_index(self):
		self.go(URL_BASE_FUJI)
		
		self.assertTitle('Fujinomiya project')
		
		site_cnt	= self.e('#site')
		nav_links	= site_cnt.es('.primary a')
		
		self.assertEqual('{0}/resources/images/project-japan/historypin-logo.png'.format(URL_ROOT_JP), nav_links[0].e('img').get_attribute('src'))
		self.assertEqual('http://www.historypin.jp/', nav_links[0].get_attribute('href'))
		
		self.assertEqual('{0}/'.format(URL_BASE_FUJI), nav_links[1].get_attribute('href'))
		self.assertEqual(u'ホーム', nav_links[1].text)
		
		self.assertEqual('{0}/explore/#|map/'.format(URL_BASE_FUJI), nav_links[2].get_attribute('href'))
		self.assertEqual(u'探索', nav_links[2].text)
		
		self.assertEqual('{0}/upload/'.format(URL_BASE_FUJI), nav_links[3].get_attribute('href'))
		self.assertEqual(u'投稿', nav_links[3].text)
		
		self.assertEqual('{0}/category/historypin-japan/fujinomiya/'.format(self.blog_link), nav_links[4].get_attribute('href'))
		self.assertEqual(u'ブログ', nav_links[4].text)
		
		self.assertEqual('http://www.glocom.ac.jp/project/historypin/fujinomiya/', nav_links[5].get_attribute('href'))
		self.assertEqual(u'富士宮プロジェクトについて', nav_links[5].text)
		
		self.assertEqual('{0}/faq/'.format(self.blog_link)		, nav_links[6].get_attribute('href'))
		self.assertEqual(u'よくある質問', nav_links[6].text)
		
		user_links = site_cnt.es('.secondary a')
		
		self.assertEqual('{0}/user/'.format(URL_BASE_FUJI), user_links[0].get_attribute('href'))
		self.assertEqual(u'アカウント作成', user_links[0].text)
		
		self.assertEqual('{0}/user/'.format(URL_BASE_FUJI), user_links[1].get_attribute('href'))
		self.assertEqual(u'ログイン', user_links[1].text)
		
		self.assertEqual(u'富士宮プロジェクト', self.e('.sec-header h1').text)
		
		self.assertEqual('{0}/jp/attach{1}/map/index/'.format(URL_ROOT_JP, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		touts_items = [
			['http://www.glocom.ac.jp/project/historypin/fujinomiya/'			, u'富士宮プロジェクトについて（外部サイト）'	, u'富士宮プロジェクトについて詳しく知る'	, 'tout1_image'],
			['{0}/category/historypin-japan/fujinomiya/'.format(self.blog_link)	, u'富士宮プロジェクトブログ'				, u'富士宮プロジェクトの最新情報'			, 'tout2_image'],
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
			self.assertEqual('{0}/projects/img/pid/47/dim/285x290/type/{1}/crop/1/'.format(URL_ROOT_JP, i[3]), imgs[n].get_attribute('src'))
		
		activity = self.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual(u'総投稿数', activity.e('h6').text)
		
		sleep(2)
		item_feed = activity.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		
		icon_tout1 = self.e('#icon-tout-0 a')
		
		self.assertEqual('http://www.historypin.jp/jp/', icon_tout1.get_attribute('href'))
		self.assertEqual(u'Historypin Japan に戻る'							, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-undo'		, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = self.e('#icon-tout-1 a')
		
		self.assertEqual('http://www.historypin.com/'	, icon_tout2.get_attribute('href'))
		self.assertEqual(u'Historypin.com (グローバルサイト）へ移動)', icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-search'	, icon_tout2.e('span').get_attribute('class'))
		
		supported = self.e('.footer .supported_by')
		self.assertEqual(u'パートナー'					, supported.e('span:nth-of-type(1)').text)
		self.assertEqual(u'富士宮プロジェクト実行委員会'	, supported.e('span:nth-of-type(2) a').text)
		self.assertEqual('http://www.glocom.ac.jp/project/historypin/fujinomiya', supported.e('span:nth-of-type(2) a').get_attribute('href'))
		
		supported_img	= supported.es('img')
		imgs			= ['british-council-logo.png', 'fujitsu.png', 'glocom.png']
		
		for n in range(len(imgs)): self.assertEqual('{0}/resources/images/project-japan/{1}'.format(URL_ROOT_JP, imgs[n]), supported_img[n].get_attribute('src'))
		
		self.assertEqual(u'使用写真はhalsan2000さんとtajima.tomocomさんがシェアしたものです。', self.e('.photos-by span').text)
		
		footer = self.e('.footer-links')
		footer_links = footer.es('a')
		
		footer_items = [
			['{0}/terms-and-conditions/'.format(self.blog_link), 'Terms and conditions'],
			['{0}/privacy-policy/'		.format(self.blog_link), 'Privacy policy'],
			['{0}/cookies/'				.format(self.blog_link), 'Cookies'],
			['http://www.shiftdesign.org.uk/'					, u'© Shift'],
		]
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
	
