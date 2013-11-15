# -*- coding: utf-8 -*-

from base import *

# TODO - check footer links for each language from the option menu in each page (list for the translations, func for each assertion and for loop)

class Project_Europeana(HPTestCase):
	
	@url('http://www.europeana1989.eu/cz/')
	def test_sub_nav_cz(self):
		
		europeana_link = 'http://www.europeana1989.eu/cz/'
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
	
	@url('http://www.europeana1989.eu/de/')
	def test_sub_nav_de(self):
		
		europeana_link = 'http://www.europeana1989.eu/de/'
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
	
	@url('http://www.europeana1989.eu/es/')
	def test_sub_nav_es(self):
		
		europeana_link = 'http://www.europeana1989.eu/es/'
		
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
	
	@url('http://www.europeana1989.eu/hu/')
	def test_sub_nav_hu(self):
		
		europeana_link = 'http://www.europeana1989.eu/hu/'
		
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
	
	@url('http://www.europeana1989.eu/lt/')
	def test_sub_nav_lt(self):
		
		europeana_link = 'http://www.europeana1989.eu/lt/'
		
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
	
	@url('http://www.europeana1989.eu/lv/')
	def test_sub_nav_lv(self):
		
		europeana_link = 'http://www.europeana1989.eu/lv/'
		
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
		
	@url('http://www.europeana1989.eu/pl/')
	def test_sub_nav_pl(self):
		
		europeana_link = 'http://www.europeana1989.eu/pl/'
		
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
	
	@url('http://www.europeana1989.eu/en/')
	def test_index(self):
		
		self.assertTitle('Europeana 1989')
		
		europeana_link	= 'http://www.europeana1989.eu/en/'
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
			self.assertEqual('http://www.europeana1989.eu/projects/img/pid/34/dim/280x310/type/' + i[2] + '/crop/1/', imgs[n].get_attribute('src'))
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
		
	
	@url('http://www.europeana1989.eu/en/about/')
	def test_about_en(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Why are we doing this?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
	
	@url('http://www.europeana1989.eu/cz/about/')
	def test_about_cz(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Proč to děláme?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
		
	@url('http://www.europeana1989.eu/de/about/')
	def test_about_de(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Warum gibt es Europeana 1989?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	@url('http://www.europeana1989.eu/es/about/')
	def test_about_es(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Miks me seda teeme?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	@url('http://www.europeana1989.eu/hu/about/')
	def test_about_hu(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Miért csináljuk?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	@url('http://www.europeana1989.eu/lt/about/')
	def test_about_lt(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kodėl mes tai darome?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	@url('http://www.europeana1989.eu/lv/about/')
	def test_about_lv(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kāpēc mēs to darām?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	@url('http://www.europeana1989.eu/pl/about/')
	def test_about_pl(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Dlaczego to robimy?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
	
	@url('http://www.europeana1989.eu/en/terms/')
	def test_terms_en(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Europeana 1989 Terms for User Contributions', site_cnt.e('h2').text)
		
	
	@url('http://www.europeana1989.eu/cz/terms/')
	def test_terms_cz(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Podmínky pro příspěvky uživatelů Europeana 1989', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/de/terms/')
	def test_terms_de(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Nutzungsbedingungen für Beiträge zum Projekt Europeana 1989', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/es/terms/')
	def test_terms_es(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 kaastöötingimused', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/hu/terms/')
	def test_terms_hu(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 feltételek a felhasználói hozzájárulásokhoz', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/lt/terms/')
	def test_terms_lt(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'„Europeana 1989“ naudotojų bendradarbiavimo sąlygos', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/lv/terms/')
	def test_terms_lv(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 Noteikumi lietotāju ieguldījuma sniegšanai', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/pl/terms/')
	def test_terms_pl(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Zasady zwiększania zbiorów Europeana 1989', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/en/contact/')
	def test_contact_en(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Contact', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/cz/contact/')
	def test_contact_cz(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/de/contact/')
	def test_contact_de(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/es/contact/')
	def test_contact_es(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontaktandmed', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/hu/contact/')
	def test_contact_hu(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kapcsolat', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/lt/contact/')
	def test_contact_lt(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontaktai', site_cnt.e('h2').text)
		
	@url('http://www.europeana1989.eu/lv/contact/')
	def test_contact_lv(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kontaktçðanâs', site_cnt.e('h2').text)
		
	@url('http://www.europeana1989.eu/pl/contact/')
	def test_contact_pl(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	@url('http://www.europeana1989.eu/en/privacy-policy/')
	def test_privacy_policy_en(self):
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	@url('http://www.europeana1989.eu/cz/privacy-policy/')
	def test_privacy_policy_cz(self):
		pass
	
	@url('http://www.europeana1989.eu/de/privacy-policy/')
	def test_privacy_policy_de(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/es/privacy-policy/')
	def test_privacy_policy_es(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/hu/privacy-policy/')
	def test_privacy_policy_hu(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/lt/privacy-policy/')
	def test_privacy_policy_lt(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/lv/privacy-policy/')
	def test_privacy_policy_lv(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/pl/privacy-policy/')
	def test_privacy_policy_pl(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/en/cookies/')
	def test_cookies(self):
		# TODO
		# assert a title, img and text
		pass
	
	@url('http://www.europeana1989.eu/en/baltic-way/')
	def test_balctic_way(self):
		
		self.assertTitle('Europeana 1989 | Relive the Baltic Way – Pin yourself on the map')
		
		site_cnt = self.e('#site-content')
		
		links = site_cnt.es('a')
		
		links_cnt = [
			['http://www.europeana1989.eu/en/project/34-1989/', 'Back to 1989 homepage'],
			['', ''],
			['', ''],
		]
		
	
