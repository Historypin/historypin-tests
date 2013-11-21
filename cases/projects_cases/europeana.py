# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Europeana(HPTestCase, Attach):
	
	PROJECT_URL = 'http://www.europeana1989.eu'
	ATTACH_TABS = [
		['%s/en/attach/tours/all/' % PROJECT_URL, '%s/en/attach/photos/index/' % (PROJECT_URL), '%s/en/attach/photos/gallery/' % PROJECT_URL],
	]
	
	# TODO fix this - won't work because we take self.go('/attach' + self.PROJECT_URL + '/map/'), but in Europeana link for the attach is different
	# test_attach_tabs	= Attach.attach_tabs
	# test_tab_tours	= Attach.attach_tab_tours
	# test_tab_map		= Attach.attach_tab_map
	# test_tab_gallery	= Attach.attach_tab_gallery
	
	def test_sub_nav_cz(self):
		self.go(self.PROJECT_URL + '/cz/')
		
		europeana_link = '%s/cz/' % self.PROJECT_URL
		cz_links = [
			[europeana_link	, 'Domov'],
			['%sexplore/#|map/' % europeana_link, 'Prozkoumat'],
			['%supload/index/' % europeana_link	, u'Přispět'],
			['http://pro.europeana.eu/web/europeana-1989/'	, 'O'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(cz_links)):
			i = cz_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_de(self):
		self.go(self.PROJECT_URL + '/de/')
		
		europeana_link = '%s/de/' % self.PROJECT_URL
		de_links = [
			[europeana_link	, 'Home'],
			['%sexplore/#|map/' % europeana_link, 'Entdecken'],
			['%supload/index/' % europeana_link	, u'Beitrag posten'],
			['http://pro.europeana.eu/web/europeana-1989/'	, u'Über'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(de_links)):
			i = de_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_es(self):
		self.go(self.PROJECT_URL + '/es/')
		
		europeana_link = '%s/es/' % self.PROJECT_URL
		
		es_links = [
			[europeana_link	, 'Kodu'],
			['%sexplore/#|map/' % europeana_link, 'Uurige'],
			['%supload/index/' % europeana_link	, u'Andke oma panus'],
			['http://pro.europeana.eu/web/europeana-1989/'	, 'Info'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(es_links)):
			i = es_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_hu(self):
		self.go(self.PROJECT_URL + '/hu/')
		
		europeana_link = '%s/hu/' % self.PROJECT_URL
		
		hu_links = [
			[europeana_link	, u'Kezdőlap'],
			['%sexplore/#|map/' % europeana_link, u'Fedezze fel'],
			['%supload/index/' % europeana_link	, u'Töltse fel'],
			['http://pro.europeana.eu/web/europeana-1989/'	, u'Rólunk'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(hu_links)):
			i = hu_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_lt(self):
		self.go(self.PROJECT_URL + '/lt/')
		
		europeana_link = '%s/lt/' % self.PROJECT_URL
		
		lt_links = [
			[europeana_link	, u'Pradinis'],
			['%sexplore/#|map/' % europeana_link, u'Naršyti'],
			['%supload/index/' % europeana_link	, u'Pridėti'],
			['http://pro.europeana.eu/web/europeana-1989/'	, u'Apie'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(lt_links)):
			i = lt_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_lv(self):
		self.go(self.PROJECT_URL + '/lv/')
		
		europeana_link = '%s/lv/' % self.PROJECT_URL
		
		lv_links = [
			[europeana_link	, u'Sākums'],
			['%sexplore/#|map/' % europeana_link, u'Pārlūkot'],
			['%supload/index/' % europeana_link	, u'Pievienot saturu'],
			['http://pro.europeana.eu/web/europeana-1989/'	, u'Par'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(lv_links)):
			i = lv_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
		
	def test_sub_nav_pl(self):
		self.go(self.PROJECT_URL + '/pl/')
		
		europeana_link = '%s/pl/' % self.PROJECT_URL
		
		pl_links = [
			[europeana_link	, u'Strona glówna'],
			['%sexplore/#|map/' % europeana_link, u'Zobacz kolekcję'],
			['%supload/index/' % europeana_link	, u'Dodaj pamiątkę'],
			['http://pro.europeana.eu/web/europeana-1989/'	, u'O nas'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(pl_links)):
			i = pl_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	# @url()
	
	def test_index(self):
		self.go(self.PROJECT_URL + '/en/')
		
		self.assertTitle('Europeana 1989')
		
		europeana_link	= '%s/en/' % self.PROJECT_URL
		eu_logo			= self.e('.small li a')
		
		self.assertEqual(europeana_link, eu_logo.get_attribute('href'))
		self.assertEqual('%sprojects/img/pid/34/dim/1000x162/type/logo/' % europeana_link, eu_logo.e('img').get_attribute('src'))
		
		option_menu = self.e('#language_select')
		self.assertEqual('en', option_menu.e('option:nth-of-type(3)').get_attribute('value'))
		self.assertEqual('English', option_menu.e('option:nth-of-type(3)').text)
		
		nav_items = [
			[europeana_link	, 'Home'],
			['%sexplore/#|map/' % europeana_link, 'Explore'],
			['%supload/index/' % europeana_link	, 'Contribute'],
			['http://pro.europeana.eu/web/europeana-1989/'	, 'About'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		for n in range(len(nav_items)):
			i = nav_items[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
		
		intro_cnt = self.e('.intro .text.cf')
		self.assertIn('Europeana 1989: We Made History', intro_cnt.e('p').text)
		
		intro_buttons = [
			['explore/#|map/', 'Explore'],
			['upload/index/', 'Contribute'],
		]
		
		links = intro_cnt.es('.button.big')
		for n in range(len(intro_buttons)):
			i = intro_buttons[n]
			self.assertEqual(europeana_link + i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
		
		site_cnt	= self.e('#site-content')
		h3s			= site_cnt.es('.tout h3')
		h3s_links	= site_cnt.es('.tout h3 a')
		paragraphs	= site_cnt.es('.tout p')
		imgs		= site_cnt.es('.tout img')
		img_link	= site_cnt.es('.tout .cover')
		
		tout_items = [
			[u'Relive the Baltic Way – Pin yourself on the map'	, '%sbaltic-way/' % europeana_link			, 'tout1_image', 'On 23 August 1989'],
			['Join our events!'									, 'http://blog.europeana.eu/1989-calendar/'	, 'tout2_image', 'Come and tell your story about the Velvet '],
		]
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], h3s_links[n].get_attribute('href'))
			self.assertEqual(i[1], img_link[n].get_attribute('href'))
			self.assertEqual('%s/projects/img/pid/34/dim/280x310/type/' % self.PROJECT_URL + i[2] + '/crop/1/', imgs[n].get_attribute('src'))
			self.assertIn(i[3], paragraphs[n].text)
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('contributions added so far', activity.e('.counter p').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		icon_tout1 = site_cnt.e('#icon-tout-0 a')
		
		self.assertEqual('%sabout/' % europeana_link		, icon_tout1.get_attribute('href'))
		self.assertEqual('Find out more about the project'	, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://blog.europeana.eu/category/europeana1989'	, icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'					, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-newspaper', icon_tout2.e('span').get_attribute('class'))
		
		featured = self.e('.bottom-p a')
		self.assertEqual('Find out more about the featured photos', featured.text)
		self.assertEqual('%sabout/' % europeana_link, featured.get_attribute('href'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		self.assertEqual('Share:', self.e('.addthis_toolbox h3').text)
		
		self.assertIsInstance(self.e('.addthis_toolbox.right'), WebElement)
		self.assertEqual('Join Europeana 1989 on:', self.e('.addthis_toolbox.right h3').text)
		
		footer_items = [
			['http://pro.europeana.eu/web/europeana-1989/'	, 'About'],
			['%sterms/'			 % europeana_link			, 'Terms and Conditions'],
			['%scontact/'		 % europeana_link			, 'Contact'],
			['%sprivacy-policy/' % europeana_link			, 'Privacy Policy'],
			['http://www.historypin.com/cookies/'			, 'Cookies'],
			['http://wearewhatwedo.org/'					, u'© We Are What We Do'],
		]
		
		footer			= self.e('#supp')
		footer_links	= footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
		
	
	def test_about_en(self):
		self.go(self.PROJECT_URL + '/en/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Why are we doing this?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
	
	def test_about_cz(self):
		self.go(self.PROJECT_URL + '/cz/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Proč to děláme?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
		
	def test_about_de(self):
		self.go(self.PROJECT_URL + '/de/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Warum gibt es Europeana 1989?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_es(self):
		self.go(self.PROJECT_URL + '/es/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Miks me seda teeme?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_hu(self):
		self.go(self.PROJECT_URL + '/hu/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Miért csináljuk?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_lt(self):
		self.go(self.PROJECT_URL + '/lt/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kodėl mes tai darome?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_lv(self):
		self.go(self.PROJECT_URL + '/lv/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kāpēc mēs to darām?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_pl(self):
		self.go(self.PROJECT_URL + '/pl/about/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Dlaczego to robimy?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
	
	def test_terms_en(self):
		self.go(self.PROJECT_URL + '/en/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Europeana 1989 Terms for User Contributions', site_cnt.e('h2').text)
		
	
	def test_terms_cz(self):
		self.go(self.PROJECT_URL + '/cz/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Podmínky pro příspěvky uživatelů Europeana 1989', site_cnt.e('h2').text)
	
	def test_terms_de(self):
		self.go(self.PROJECT_URL + '/de/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Nutzungsbedingungen für Beiträge zum Projekt Europeana 1989', site_cnt.e('h2').text)
	
	def test_terms_es(self):
		self.go(self.PROJECT_URL + '/es/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 kaastöötingimused', site_cnt.e('h2').text)
	
	def test_terms_hu(self):
		self.go(self.PROJECT_URL + '/hu/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 feltételek a felhasználói hozzájárulásokhoz', site_cnt.e('h2').text)
	
	def test_terms_lt(self):
		self.go(self.PROJECT_URL + '/lt/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'„Europeana 1989“ naudotojų bendradarbiavimo sąlygos', site_cnt.e('h2').text)
	
	def test_terms_lv(self):
		self.go(self.PROJECT_URL + '/lv/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 Noteikumi lietotāju ieguldījuma sniegšanai', site_cnt.e('h2').text)
	
	def test_terms_pl(self):
		self.go(self.PROJECT_URL + '/pl/terms/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Zasady zwiększania zbiorów Europeana 1989', site_cnt.e('h2').text)
	
	def test_contact_en(self):
		self.go(self.PROJECT_URL + '/en/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Contact', site_cnt.e('h2').text)
	
	def test_contact_cz(self):
		self.go(self.PROJECT_URL + '/cz/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	def test_contact_de(self):
		self.go(self.PROJECT_URL + '/de/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	def test_contact_es(self):
		self.go(self.PROJECT_URL + '/es/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontaktandmed', site_cnt.e('h2').text)
	
	def test_contact_hu(self):
		self.go(self.PROJECT_URL + '/hu/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kapcsolat', site_cnt.e('h2').text)
	
	def test_contact_lt(self):
		self.go(self.PROJECT_URL + '/lt/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontaktai', site_cnt.e('h2').text)
		
	def test_contact_lv(self):
		self.go(self.PROJECT_URL + '/lv/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kontaktçðanâs', site_cnt.e('h2').text)
		
	def test_contact_pl(self):
		self.go(self.PROJECT_URL + '/pl/contact/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	def test_privacy_policy_en(self):
		self.go(self.PROJECT_URL + '/en/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_cz(self):
		self.go(self.PROJECT_URL + '/cz/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_de(self):
		self.go(self.PROJECT_URL + '/de/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
		
	def test_privacy_policy_es(self):
		self.go(self.PROJECT_URL + '/es/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_hu(self):
		self.go(self.PROJECT_URL + '/hu/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_lt(self):
		self.go(self.PROJECT_URL + '/lt/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_lv(self):
		self.go(self.PROJECT_URL + '/lv/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_pl(self):
		self.go(self.PROJECT_URL + '/pl/privacy-policy/')
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_balctic_way_en(self):
		self.go(self.PROJECT_URL + '/en/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Relive the Baltic Way – Pin yourself on the map')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Relive the Baltic Way – Pin yourself on the map', site_cnt.e('h1').text)
		self.assertIn('Relive the Baltic Way online.', site_cnt.e('h1 + p').text)
		
		europeana_link	= '%s/en/' % self.PROJECT_URL
		
		links			= site_cnt.es('.page-top > a')
		
		links_cnt = [
			['project/34-1989/'	, 'Back to 1989 homepage'],
			['upload/index/'	, 'Contribute'],
		]
		
		for n in range(len(links_cnt)):
			i = links_cnt[n]
			self.assertEqual(europeana_link + i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
		
		self.assertIsInstance(self.e('#embed-frame'), WebElement)
	
	def test_balctic_way_cz(self):
		self.go(self.PROJECT_URL + '/cz/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Baltský řetěz - Připněte své fotografie na mapu')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Baltský řetěz - Připněte své fotografie na mapu', site_cnt.e('h1').text)
		self.assertIn(u'Oživme baltský řetěz online.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_de(self):
		self.go(self.PROJECT_URL + '/de/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Der Baltischer Weg - Pinnen Sie Ihr Foto auf die Karte')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Der Baltischer Weg - Pinnen Sie Ihr Foto auf die Karte', site_cnt.e('h1').text)
		self.assertIn(u'Lasst uns den Baltischen Weg online wieder aufleben.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_es(self):
		self.go(self.PROJECT_URL + '/es/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Kus olite teie Balti keti ajal? Pange ennast kaardile!')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Kus olite teie Balti keti ajal? Pange ennast kaardile!', site_cnt.e('h1').text)
		self.assertIn(u'Siin on võimalus Balti kett taas kord läbi teha.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_hu(self):
		self.go(self.PROJECT_URL + '/hu/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Élje át újra a Balti utat – Kerüljön fel a térképre')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Élje át újra a Balti utat – Kerüljön fel a térképre', site_cnt.e('h1').text)
		self.assertIn(u'Online a Balti úton.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_lt(self):
		self.go(self.PROJECT_URL + '/lt/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Atkurkime Baltijos kelią internete')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Atkurkime Baltijos kelią internete', site_cnt.e('h1').text)
		self.assertIn(u'Atkurkime Baltijos kelią internete.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_lv(self):
		self.go(self.PROJECT_URL + '/lv/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Atjauno Baltijas ceļu – atzīmē sevi kartē!')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Atjauno Baltijas ceļu – atzīmē sevi kartē!', site_cnt.e('h1').text)
		self.assertIn(u'Atjauno Baltijas ceļu tiešsaistē!', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_pl(self):
		self.go(self.PROJECT_URL + '/pl/baltic-way/')
		
		self.assertTitle(u'Europeana 1989 | Bałtycki Łańcuch - przypnij się do mapy')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Bałtycki Łańcuch - przypnij się do mapy', site_cnt.e('h1').text)
		self.assertIn(u'Niech Łańcuch Bałtycki odżyje jeszcze raz online.', site_cnt.e('h1 + p').text)
	