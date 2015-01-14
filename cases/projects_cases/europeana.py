# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Europeana(HPTestCase, Attach):
	
	if IS_LIVE: PROJECT_URL = ''
	else: PROJECT_URL = '/project/34-1989'
	
	ATTACH_URL = '{0}/en/attach'.format(URL_ROOT_1989)
	
	ATTACH_TABS = [
		'{0}/tours/all/'		.format(PROJECT_URL),
		'{0}/photos/index/'		.format(PROJECT_URL),
		'{0}/photos/gallery/'	.format(PROJECT_URL),
	]
	
	test_attach_tabs	= Attach.attach_tabs
	test_tab_map		= Attach.attach_tab_map
	test_tab_gallery	= Attach.attach_tab_gallery
	
	# ALL CONTACT AND PRIVACY POLICY TESTS WILL FAIL WHEN ARE RUNNED IN THE TEST SUITE, BECAUSE THERE IS NO ENOUGH TIME BETWEEN THE Test EXECUTION OF EACH CASE
	
	# @unittest.expectedFailure
	def test_tab_tours(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		sleep(2)
		filter_by = self.e('.search-filter-pos')
		self.assertEqual('Sort by  ', filter_by.e('span').text)
		
		radio_buttons	= filter_by.es('input')
		labels			= filter_by.es('label')
		
		self.assertIsInstance(radio_buttons[0], WebElement)
		self.assertTrue(radio_buttons[0].is_selected())
		self.assertFalse(radio_buttons[1].is_selected())
		
		self.assertEqual(' Most Recent'	, labels[0].e('strong').text)
		self.assertEqual(' Most Popular', labels[1].e('strong').text)
		
		item = self.e('#list li:nth-of-type(1) > a')
		self.assertIsInstance(item, WebElement)
		self.assertIsInstance(item.e('img'), WebElement)
		
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, item.e('span').get_attribute('class'))
		
		paragraph = self.e('#list li:nth-of-type(1) p')
		self.assertIsInstance(paragraph.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(paragraph.e('a:nth-of-type(2)'), WebElement)
		
		radio_buttons[1].click()
		
		item = self.e('#list li:nth-of-type(1) > a')
		self.assertIsInstance(item, WebElement)
		self.assertIsInstance(item.e('img'), WebElement)
		
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, item.e('span').get_attribute('class'))
		
		paragraph = self.e('#list li:nth-of-type(1) p')
		self.assertIsInstance(paragraph.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(paragraph.e('a:nth-of-type(2)'), WebElement)
	
	# @unittest.expectedFailure
	def test_search_by_relevance(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Search', input_search.get_attribute('placeholder'))
		self.assertEqual('Go', button_go.e('span').text)
		
		input_search.send_keys('Berlin')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertIsInstance(radio_buttons[2], WebElement)
		self.assertTrue(radio_buttons[2].is_selected())
		
		self.assertEqual('{0}/en/attach{1}/tours/all'.format(URL_ROOT_1989, self.PROJECT_URL), self.e('.clear-search').get_attribute('href'))
		self.assertEqual('Clear search', self.e('.clear-search').text)
		
		self.assertIn(u'Search results for "Berlin":', site_cnt.e('.search-result').text)
		
		items = site_cnt.es('#list li')
		
		self.assertGreater(len(items), 20)
		
		next_link = site_cnt.e('#list .show-next')
		self.assertEqual('{0}/en/attach{1}/tours/all/page/2/order/relevance/?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL), next_link.get_attribute('href'))
		
		self.e('.clear-search').click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[0].is_selected())
	
	def test_next_page_relevance(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Search', input_search.get_attribute('placeholder'))
		self.assertEqual('Go', button_go.e('span').text)
		
		input_search.send_keys('Berlin')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		radio_buttons[2].click()
		
		site_cnt		= self.e('#photo_list_content')
		next_link = site_cnt.e('#list .show-next')
		next_link.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[2].is_selected())
		
		items = site_cnt.es('#list li')
		
		self.assertGreater(len(items), 20)
		
	
	# @unittest.expectedFailure
	def test_search_by_popularity(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		input_search.send_keys('Berlin')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		radio_buttons[1].click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[1].is_selected())
		
		items = site_cnt.es('#list li')
		
		self.assertGreater(len(items), 20)
		
		self.e('.clear-search').click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[0].is_selected())
	
	# @unittest.expectedFailure
	def test_next_page_popularity(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Search', input_search.get_attribute('placeholder'))
		self.assertEqual('Go', button_go.e('span').text)
		
		input_search.send_keys('Berlin')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		radio_buttons[1].click()
		site_cnt		= self.e('#photo_list_content')
		next_link = site_cnt.e('#list .show-next')
		next_link.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		self.assertTrue(radio_buttons[1].is_selected())
		
		items = site_cnt.es('#list li')
		
		self.assertGreater(len(items), 20)
		
	
	# @unittest.expectedFailure
	def test_search_by_most_recent(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		input_search.send_keys('Berlin')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		radio_buttons[0].click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[0].is_selected())
		
		items = site_cnt.es('#list li')
		
		self.assertGreater(len(items), 20)
		
		self.e('.clear-search').click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[0].is_selected())
	
	# @unittest.expectedFailure
	def test_next_page_recent(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Search', input_search.get_attribute('placeholder'))
		self.assertEqual('Go', button_go.e('span').text)
		
		input_search.send_keys('Berlin')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		radio_buttons[0].click()
		
		site_cnt	= self.e('#photo_list_content')
		next_link	= site_cnt.e('#list .show-next')
		next_link.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		self.assertTrue(radio_buttons[0].is_selected())
		
		items = site_cnt.es('#list li')
		
		self.assertGreater(len(items), 20)
	
	def test_search_no_results(self):
		self.go('{0}{1}/tours/all/'.format(self.ATTACH_URL, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		input_search	= site_cnt.e('#stories-search')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Go', button_go.e('span').text)
		
		input_search.send_keys('ASDFGHQWERTYUIOPS')
		button_go.click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		labels			= filter_by.es('label')
		
		self.assertIsInstance(radio_buttons[2], WebElement)
		self.assertTrue(radio_buttons[2].is_selected())
		self.assertEqual(' Most Relevant', labels[2].e('strong').text)
		self.assertEqual(u'Search results for "ASDFGHQWERTYUIOPS": (0)', site_cnt.e('.search-result').text)
		
		self.assertEqual('No results found.', site_cnt.e('h3').text)
		
		self.e('.clear-search').click()
		
		site_cnt		= self.e('#photo_list_content')
		filter_by		= site_cnt.e('.search-filter-pos')
		radio_buttons	= filter_by.es('input')
		
		self.assertTrue(radio_buttons[0].is_selected())
		
		item = self.e('#list li:nth-of-type(1) > a')
		self.assertIsInstance(item, WebElement)
		self.assertIsInstance(item.e('img'), WebElement)
		
		self.assertIn('tour-icon'	, item.e('span').get_attribute('class'))
		self.assertIn('ss-icon'		, item.e('span').get_attribute('class'))
		self.assertIn('ss-openbook'	, item.e('span').get_attribute('class'))
		
		paragraph = self.e('#list li:nth-of-type(1) p')
		self.assertIsInstance(paragraph.e('a:nth-of-type(1)'), WebElement)
		self.assertIsInstance(paragraph.e('a:nth-of-type(2)'), WebElement)
	
	def test_check_search_translation_cz(self):
		self.go('{0}/cz/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual(u'Jít na', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual(u'Roztřídit podle  '	, filter_by.e('span').text)
		self.assertEqual(u' Nejnovější'			, labels[0].e('strong').text)
		self.assertEqual(u' Nejpopulárnější'	, labels[1].e('strong').text)
		self.assertEqual(u' Most Relevant'		, labels[2].e('strong').text)
		
		# TODO fix "Most Relevant" text when there is a translation provided
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'Výsledky dotazu pro', site_cnt.e('.search-result').text)
		
	
	def test_check_search_translation_de(self):
		self.go('{0}/de/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Anzeigen', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual('Sortieren nach  '	, filter_by.e('span').text)
		self.assertEqual(' Neuestes'		, labels[0].e('strong').text)
		self.assertEqual(' Beliebtestes'	, labels[1].e('strong').text)
		self.assertEqual(' der relevanteste', labels[2].e('strong').text)
		
		# TODO fix "Most Relevant" text when there is a translation provided
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'Suchergebnisse für', site_cnt.e('.search-result').text)
	
	def test_check_search_translation_es(self):
		self.go('{0}/es/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Minge:', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual('Sorteerige:  '	, filter_by.e('span').text)
		self.assertEqual(' Viimased'		, labels[0].e('strong').text)
		self.assertEqual(' Populaarseimad'	, labels[1].e('strong').text)
		self.assertEqual(u' Most Relevant'	, labels[2].e('strong').text)
		
		# TODO fix "Most Relevant" text when there is a translation provided
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'otsi tulemusi', site_cnt.e('.search-result').text)
	
	def test_check_search_translation_hu(self):
		self.go('{0}/hu/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Mehet', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual(u'Rendezési sorrend:  '	, filter_by.e('span').text)
		self.assertEqual(u' Legutóbbi'		, labels[0].e('strong').text)
		self.assertEqual(u' Legnépszerűbb'	, labels[1].e('strong').text)
		self.assertEqual(u' Legrelevansabb', labels[2].e('strong').text)
		
		# TODO fix "Most Relevant" text when there is a translation provided
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'Találatok a', site_cnt.e('.search-result').text)
		
	
	def test_check_search_translation_lt(self):
		self.go('{0}/lt/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Eiti', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual(u'Rūšiuoti  '		, filter_by.e('span').text)
		self.assertEqual(u' Naujausi'		, labels[0].e('strong').text)
		self.assertEqual(u' Populiariausi'	, labels[1].e('strong').text)
		self.assertEqual(u' Svarbiausi'		, labels[2].e('strong').text)
		
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'Paieškos rezultatai', site_cnt.e('.search-result').text)
		
	
	def test_check_search_translation_lv(self):
		self.go('{0}/lv/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual('Doties', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual(u'Ðíirot pçc  '				, filter_by.e('span').text)
		self.assertEqual(u' Visjaunâkais'				, labels[0].e('strong').text)
		self.assertEqual(u' Vispopulârâkais'			, labels[1].e('strong').text)
		self.assertEqual(u' Atbilsto\u0161\u0101kais'	, labels[2].e('strong').text)
		
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'meklēšanas rezultāti', site_cnt.e('.search-result').text)
		
	
	def test_check_search_translation_pl(self):
		self.go('{0}/pl/attach{1}/tours/all?search=Berlin'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		site_cnt		= self.e('#photo_list_content')
		button_go		= site_cnt.e('#stories-search-submit')
		
		self.assertEqual(u'Przejdź', button_go.e('span').text)
		
		filter_by		= site_cnt.e('.search-filter-pos')
		labels			= filter_by.es('label')
		
		self.assertEqual(u'Sortuj według  '			, filter_by.e('span').text)
		self.assertEqual(u' Ostatnie'				, labels[0].e('strong').text)
		self.assertEqual(u' Najpopularniejsze'		, labels[1].e('strong').text)
		self.assertEqual(u' najtrafniejsze wyniki'	, labels[2].e('strong').text)
		
		# TODO fix "Most Relevant" text when there is a translation provided
		# TODO add verification for "Clear search" text when there is translation
		
		self.assertIn(u'Rezultaty dla', site_cnt.e('.search-result').text)
	
	def test_sub_nav_cz(self):
		self.go('{0}/cz{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/cz{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		cz_links = [
			[europeana_link	, 'Domov'],
			['{0}explore/#|photos/index/'.format(europeana_link)	, 'Prozkoumat'],
			['{0}upload/index/'.format(europeana_link)			, u'Přispět'],
			['http://pro.europeana.eu/web/europeana-1989/'		, 'O'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(cz_links)):
			i = cz_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_de(self):
		self.go('{0}/de{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/de{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		de_links = [
			[europeana_link										, 'Home'],
			['{0}explore/#|photos/index/'.format(europeana_link)	, 'Entdecken'],
			['{0}upload/index/'			.format(europeana_link)	, u'Beitrag posten'],
			['http://pro.europeana.eu/web/europeana-1989/'		, u'Über'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(de_links)):
			i = de_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_es(self):
		self.go('{0}/es{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/es{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		
		es_links = [
			[europeana_link, 'Kodu'],
			['{0}explore/#|photos/index/'.format(europeana_link)	, 'Uurige'],
			['{0}upload/index/'			.format(europeana_link)	, u'Andke oma panus'],
			['http://pro.europeana.eu/web/europeana-1989/'		, 'Info'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(es_links)):
			i = es_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_hu(self):
		self.go('{0}/hu{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/hu{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		
		hu_links = [
			[europeana_link	, u'Kezd\u0151lap'],
			['{0}explore/#|photos/index/'	.format(europeana_link)	, u'Fedezze fel'],
			['{0}upload/index/'			.format(europeana_link)	, u'Töltse fel'],
			['http://pro.europeana.eu/web/europeana-1989/'			, u'Rólunk'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(hu_links)):
			i = hu_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_lt(self):
		self.go('{0}/lt{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/lt{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		
		lt_links = [
			[europeana_link	, u'Pradinis'],
			['{0}explore/#|photos/index/'	.format(europeana_link)	, u'Naršyti'],
			['{0}upload/index/'			.format(europeana_link)	, u'Pridėti'],
			['http://pro.europeana.eu/web/europeana-1989/'			, u'Apie'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(lt_links)):
			i = lt_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_sub_nav_lv(self):
		self.go('{0}/lv{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/lv{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		
		lv_links = [
			[europeana_link	, u'Sākums'],
			['{0}explore/#|photos/index/'	.format(europeana_link)	, u'Pārlūkot'],
			['{0}upload/index/'				.format(europeana_link)	, u'Pievienot saturu'],
			['http://pro.europeana.eu/web/europeana-1989/'			, u'Par'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(lv_links)):
			i = lv_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
		
	def test_sub_nav_pl(self):
		self.go('{0}/pl{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		europeana_link = '{0}/pl{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		
		pl_links = [
			[europeana_link	, u'Strona gl\xf3wna'],
			['{0}explore/#|photos/index/'	.format(europeana_link)	, u'Zobacz kolekcję'],
			['{0}upload/index/'				.format(europeana_link)	, u'Dodaj pamiątkę'],
			['http://pro.europeana.eu/web/europeana-1989/'			, u'O nas'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		
		for n in range(len(pl_links)):
			i = pl_links[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
	
	def test_index(self):
		self.go('{0}/en{1}'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		europeana_link	= '{0}/en{1}/'.format(URL_ROOT_1989, self.PROJECT_URL)
		eu_logo			= self.e('.small li a')
		
		self.assertEqual(europeana_link, eu_logo.get_attribute('href'))
		self.assertEqual('{0}projects/img/pid/34/dim/1000x162/type/logo/'.format(europeana_link), eu_logo.e('img').get_attribute('src'))
		
		option_menu = self.e('#language_select')
		self.assertEqual('en', option_menu.e('option:nth-of-type(3)').get_attribute('value'))
		self.assertEqual('English', option_menu.e('option:nth-of-type(3)').text)
		
		nav_items = [
			[europeana_link	, 'Home'],
			['{0}explore/#|photos/index/'	.format(europeana_link)	, 'Explore'],
			['{0}upload/index/'				.format(europeana_link)	, 'Contribute'],
			['http://pro.europeana.eu/web/europeana-1989/'			, 'About'],
		]
		
		nav_links = self.es('.sub-navigation li a')
		for n in range(len(nav_items)):
			i = nav_items[n]
			self.assertEqual(i[0], nav_links[n].get_attribute('href'))
			self.assertEqual(i[1], nav_links[n].text)
		
		intro_cnt = self.e('.intro .text.cf')
		self.assertIn('The way history is recorded', intro_cnt.e('p').text)
		
		intro_buttons = [
			['explore/#|photos/index/', 'Explore'],
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
		img_link	= site_cnt.es('.tout p+a')
		
		# broken balctic way link, to be fixed
		
		tout_items = [
			['Relive the Baltic Way - Pin yourself on the map'	, '{0}/en{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL)	, 'tout1_image', 'On 23 August 1989'],
			['Join our events!'									, 'http://blog.europeana.eu/1989-calendar/'							, 'tout2_image', 'Come and tell your story about the Velvet '],
		]
		
		for n in range(len(tout_items)):
			i = tout_items[n]
			self.assertEqual(i[0], h3s[n].text)
			self.assertEqual(i[1], h3s_links[n].get_attribute('href'))
			self.assertEqual(i[1], img_link[n].get_attribute('href'))
			self.assertEqual('{0}/projects/img/pid/34/dim/280x310/type/'.format(URL_ROOT_1989) + i[2] + '/crop/1/', imgs[n].get_attribute('src'))
			self.assertIn(i[3], paragraphs[n].text)
		
		activity = site_cnt.e('#activity')
		self.assertIsInstance(activity.e('h1'), WebElement)
		self.assertEqual('contributions added so far', activity.e('h6').text)
		
		item_feed = site_cnt.e('.activity li:nth-of-type(1)')
		self.assertIsInstance(item_feed.e('a')	, WebElement)
		self.assertIsInstance(item_feed.e('img'), WebElement)
		
		icon_tout1 = site_cnt.e('#icon-tout-0 a')
		
		# this will fail on develop, because of the copying the database
		
		self.assertEqual('{0}/about/'.format(URL_BASE_1989)		, icon_tout1.get_attribute('href'))
		self.assertEqual('Find out more about the project'	, icon_tout1.text)
		self.assertIn('ss-icon'		, icon_tout1.e('span').get_attribute('class'))
		self.assertIn('ss-users'	, icon_tout1.e('span').get_attribute('class'))
		
		icon_tout2 = site_cnt.e('#icon-tout-1 a')
		
		self.assertEqual('http://blog.europeana.eu/category/europeana1989'	, icon_tout2.get_attribute('href'))
		self.assertEqual('Read the latest news on our blog'					, icon_tout2.text)
		self.assertIn('ss-icon'		, icon_tout2.e('span').get_attribute('class'))
		self.assertIn('ss-openbook', icon_tout2.e('span').get_attribute('class'))
		
		featured = self.e('.bottom-p a')
		self.assertEqual('Find out more about the featured photos', featured.text)
		self.assertEqual('{0}/about/'.format(URL_BASE_1989), featured.get_attribute('href'))
		
		self.assertIsInstance(self.e('.addthis_toolbox'), WebElement)
		self.assertEqual('Share:', self.e('.addthis_toolbox h3').text)
		
		self.assertIsInstance(self.e('.addthis_toolbox.right'), WebElement)
		self.assertEqual('Join Europeana 1989 on:', self.e('.addthis_toolbox.right h3').text)
		
		footer_items = [
			['http://pro.europeana.eu/web/europeana-1989/'	, 'About'],
			['{0}terms/'			.format(europeana_link)	, 'Terms and Conditions'],
			['{0}contact/'			.format(europeana_link)	, 'Contact'],
			['{0}privacy-policy/'	.format(europeana_link)	, 'Privacy Policy'],
			['http://www.historypin.com/cookies/'			, 'Cookies'],
			['http://www.shiftdesign.org.uk/'				, u'© Shift'],
		]
		
		footer			= self.e('#supp')
		footer_links	= footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
		
	def test_explore_button(self):
		self.go('http://www.europeana1989.eu/en/')
		
		self.e('.w2 .button.big').click()
		
		site_cnt	= self.e('#site-content')
		activity	= site_cnt.e('#activity')
		self.assertIsInstance(activity, WebElement)
		
		self.assertIsInstance(self.e('.right.next-button.button'), WebElement)
	
	def test_about_en(self):
		self.go('{0}/en{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Why are we doing this?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
	
	def test_about_cz(self):
		self.go('{0}/cz{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Proč to děláme?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
		
	def test_about_de(self):
		self.go('{0}/de{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Warum gibt es Europeana 1989?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_es(self):
		self.go('{0}/es{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Miks me seda teeme?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_hu(self):
		self.go('{0}/hu{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Miért csináljuk?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_lt(self):
		self.go('{0}/lt{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kodėl mes tai darome?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_lv(self):
		self.go('{0}/lv{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kāpēc mēs to darām?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
		
	
	def test_about_pl(self):
		self.go('{0}/pl{1}/about/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Dlaczego to robimy?', site_cnt.e('h2').text)
		self.assertEqual('http://wawwd-resources.s3.amazonaws.com/historypin/projects/1989/about_images.jpg', site_cnt.e('.inner img').get_attribute('src'))
	
	def test_terms_en(self):
		self.go('{0}/en{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Europeana 1989 Terms for User Contributions', site_cnt.e('h2').text)
		
	
	def test_terms_cz(self):
		self.go('{0}/cz{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Podmínky pro příspěvky uživatelů Europeana 1989', site_cnt.e('h2').text)
	
	def test_terms_de(self):
		self.go('{0}/de{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Nutzungsbedingungen für Beiträge zum Projekt Europeana 1989', site_cnt.e('h2').text)
	
	def test_terms_es(self):
		self.go('{0}/es{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 kaastöötingimused', site_cnt.e('h2').text)
	
	def test_terms_hu(self):
		self.go('{0}/hu{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 feltételek a felhasználói hozzájárulásokhoz', site_cnt.e('h2').text)
	
	def test_terms_lt(self):
		self.go('{0}/lt{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'„Europeana 1989“ naudotojų bendradarbiavimo sąlygos', site_cnt.e('h2').text)
	
	def test_terms_lv(self):
		self.go('{0}/lv{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Europeana 1989 Noteikumi lietotāju ieguldījuma sniegšanai', site_cnt.e('h2').text)
	
	def test_terms_pl(self):
		self.go('{0}/pl{1}/terms/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Zasady zwiększania zbiorów Europeana 1989', site_cnt.e('h2').text)
	
	def test_contact_en(self):
		self.go('{0}/en{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Contact', site_cnt.e('h2').text)
	
	def test_contact_cz(self):
		self.go('{0}/cz{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	def test_contact_de(self):
		self.go('{0}/de{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	def test_contact_es(self):
		self.go('{0}/es{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontaktandmed', site_cnt.e('h2').text)
	
	def test_contact_hu(self):
		self.go('{0}/hu{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kapcsolat', site_cnt.e('h2').text)
	
	def test_contact_lt(self):
		self.go('{0}/lt{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontaktai', site_cnt.e('h2').text)
		
	def test_contact_lv(self):
		self.go('{0}/lv{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual(u'Kontakti', site_cnt.e('h2').text)
		
	def test_contact_pl(self):
		self.go('{0}/pl{1}/contact/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Kontakt', site_cnt.e('h2').text)
	
	def test_privacy_policy_en(self):
		self.go('{0}/en{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(3)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_cz(self):
		self.go('{0}/cz{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(1)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_de(self):
		self.go('{0}/de{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(2)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
		
	def test_privacy_policy_es(self):
		self.go('{0}/es{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(4)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_hu(self):
		self.go('{0}/hu{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(5)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_lt(self):
		self.go('{0}/lt{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(6)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_lv(self):
		self.go('{0}/lv{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(7)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_privacy_policy_pl(self):
		self.go('{0}/pl{1}/privacy-policy/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle('Europeana 1989')
		
		option_menu = self.e('#language_select')
		self.assertTrue(option_menu.e('option:nth-of-type(8)').is_selected())
		
		site_cnt = self.e('#site-content')
		self.assertEqual('Privacy Policy', site_cnt.e('h1').text)
	
	def test_balctic_way_en(self):
		self.go('{0}/en{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Relive the Baltic Way – Pin yourself on the map')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Relive the Baltic Way – Pin yourself on the map', site_cnt.e('h1').text)
		self.assertIn('Relive the Baltic Way online.', site_cnt.e('h1 + p').text)
		
		europeana_link	= '{0}/en{1}'.format(URL_BASE, self.PROJECT_URL)
		
		links			= site_cnt.es('.page-top > a')
		
		links_cnt = [
			['{0}/'				.format(europeana_link), 'Back to 1989 homepage'],
			['{0}/upload/index/'.format(europeana_link), 'Contribute'],
		]
		
		for n in range(len(links_cnt)):
			i = links_cnt[n]
			self.assertEqual(i[0], links[n].get_attribute('href'))
			self.assertEqual(i[1], links[n].text)
		
		self.assertIsInstance(self.e('#embed-frame'), WebElement)
	
	def test_balctic_way_cz(self):
		self.go('{0}/cz{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Baltský řetěz - Připněte své fotografie na mapu')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Baltský řetěz - Připněte své fotografie na mapu', site_cnt.e('h1').text)
		self.assertIn(u'Oživme baltský řetěz online.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_de(self):
		self.go('{0}/de{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Der Baltischer Weg - Pinnen Sie Ihr Foto auf die Karte')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Der Baltischer Weg - Pinnen Sie Ihr Foto auf die Karte', site_cnt.e('h1').text)
		self.assertIn(u'Lasst uns den Baltischen Weg online wieder aufleben.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_es(self):
		self.go('{0}/es{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Kus olite teie Balti keti ajal? Pange ennast kaardile!')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Kus olite teie Balti keti ajal? Pange ennast kaardile!', site_cnt.e('h1').text)
		self.assertIn(u'Siin on võimalus Balti kett taas kord läbi teha.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_hu(self):
		self.go('{0}/hu{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Élje át újra a Balti utat – Kerüljön fel a térképre')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Élje át újra a Balti utat – Kerüljön fel a térképre', site_cnt.e('h1').text)
		self.assertIn(u'Online a Balti úton.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_lt(self):
		self.go('{0}/lt{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Atkurkime Baltijos kelią internete')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Atkurkime Baltijos kelią internete', site_cnt.e('h1').text)
		self.assertIn(u'Atkurkime Baltijos kelią internete.', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_lv(self):
		self.go('{0}/lv{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Atjauno Baltijas ceļu – atzīmē sevi kartē!')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Atjauno Baltijas ceļu – atzīmē sevi kartē!', site_cnt.e('h1').text)
		self.assertIn(u'Atjauno Baltijas ceļu tiešsaistē!', site_cnt.e('h1 + p').text)
	
	def test_balctic_way_pl(self):
		self.go('{0}/pl{1}/baltic-way/'.format(URL_ROOT_1989, self.PROJECT_URL))
		
		self.assertTitle(u'Europeana 1989 | Bałtycki Łańcuch - przypnij się do mapy')
		
		site_cnt = self.e('#site-content')
		
		self.assertEqual(u'Bałtycki Łańcuch - przypnij się do mapy', site_cnt.e('h1').text)
		self.assertIn(u'Niech Łańcuch Bałtycki odżyje jeszcze raz online.', site_cnt.e('h1 + p').text)
	
	@unittest.skipIf(IS_LIVE, 'Do not run on live')
	@logged_in
	def test_create_story(self):
		self.go('/en{0}/tours/add/'.format(self.PROJECT_URL))
		
		#####################  STEP 1 ######################
		site_cnt = self.e('#site-content')
		
		self.assertEqual('{0}/en{1}/'.format(URL_BASE, self.PROJECT_URL), site_cnt.e('.back').get_attribute('href'))
		
		tour_title = site_cnt.e('#tour-title')
		
		self.assertEqual('Give your story a name. It will appear across all steps in the story', tour_title.get_attribute('placeholder'))
		
		tour_title.send_keys('This is a story about famous buildings in Sofia, Bulgaria')
		
		site_cnt.e('#tour-description').send_keys('This is a story about famous buildings in Sofia, Bulgaria. They are located in the city centre and are very beautiful.')
		
		name_contributor = site_cnt.e('#name-contributor')
		self.assertEqual('Gabriela Ananieva', name_contributor.get_attribute('value'))
		
		language_select = site_cnt.e('#which-language')
		language_select.e('option:nth-of-type(4)').click()
		
		date_select_from = site_cnt.e('#select-date')
		date_select_from.e('#day option:nth-of-type(4)').click()
		date_select_from.e('#month option:nth-of-type(5)').click()
		date_select_from.e('#year option:nth-of-type(5)').click()
		
		site_cnt.e('.date-precise-wrapper #day_to option:nth-of-type(9)').click()
		site_cnt.e('.date-precise-wrapper #month_to option:nth-of-type(10)').click()
		site_cnt.e('.date-precise-wrapper #month_to option:nth-of-type(4)').click()
		
		country = site_cnt.e('#country')
		country.e('option:nth-of-type(3)').click()
		
		keywords = site_cnt.e('.inline-list:nth-of-type(1)')
		keywords.e('li:nth-of-type(1) a').click()
		keywords.e('li:nth-of-type(6) a').click()
		keywords.e('li:nth-of-type(24) a').click()
		
		site_cnt.e('#additional_keywords').send_keys('#theatres')
		
		events = site_cnt.e('.inline-list:nth-of-type(2)')
		events.e('li:nth-of-type(6) a').click()
		
		site_cnt.e('.tour-next').click()
		
		#####################  STEP 2 ######################
		
		tour_id		= self.browser.current_url.split('/')[8]
		
		site_cnt	= self.e('#site-content')
		tour_step2	= site_cnt.e('#tour-step2')
		tabs_nav	= site_cnt.e('.tabs-nav.cf')
		tabs		= tabs_nav.es('li')
		
		my_items = tour_step2.e('.choose-photos.yours.cf')
		sleep(3)
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/152x108/crop/1/'.format(URL_BLOB, ID_TOUR_IMAGES[0]), my_items.e('img').get_attribute('src'))
		
		my_items.e('.add-photo').click()
		sleep(3)
		sidebar = tour_step2.e('.w4.gallery')
		
		item_1 = sidebar.e('li:nth-of-type(2)')
		sleep(2)
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/152x108/crop/1/'.format(URL_BLOB, ID_TOUR_IMAGES[0]), item_1.e('img').get_attribute('src'))
		self.assertEqual('Bulgarian Army Theater'	, item_1.e('.photo-title').text)
		self.assertEqual('2 February 2013'			, item_1.e('.date').text)
		
		tabs[1].click()
		my_favourites = tour_step2.e('.choose-photos.favourites.cf')
		
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/152x108/crop/1/'.format(URL_BLOB, ID_TOUR_IMAGES[1]), my_favourites.e('img').get_attribute('src'))
		sleep(3)
		my_favourites.e('.add-photo').click()
		
		sleep(3)
		
		item_2 = sidebar.e('li:nth-of-type(3)')
		sleep(3)
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/152x108/crop/1/'.format(URL_BLOB, ID_TOUR_IMAGES[1]), item_2.e('img').get_attribute('src'))
		self.assertEqual('National Theatre in Sofia, Bulgaria'	, item_2.e('.photo-title').text)
		self.assertEqual('2 August 2012'						, item_2.e('.date').text)
		
		site_cnt.e('.tour-next').click()
		
		#####################  STEP 3  ######################
		
		site_cnt	= self.e('#site-content')
		tour_step3	= site_cnt.e('#tour-step3')
		
		sidebar = tour_step3.e('#sortable')
		
		sleep(4)
		self.assertEqual('Bulgarian Army Theater - 2 February 2013'					, tour_step3.e('#step-title').get_attribute('value'))
		self.assertEqual('This is a photo of the famous Bulgarian Army Theater .'	, tour_step3.e('#step-description').get_attribute('value'))
		
		# sidebar.e('li:nth-of-type(2) a').click()
		# sleep(3)
		# self.assertEqual('National Theatre in Sofia, Bulgaria - 2 August 2012'		, tour_step3.e('#step-title').get_attribute('value'))
		# self.assertEqual('This is a photo of National Theatre in Sofia, Bulgaria'	, tour_step3.e('#step-description').get_attribute('value'))
		
		self.es('.cf .right.preview')[1].click()
		
		sleep(3)
		site_cnt	= self.e('#site-content')
		site_cnt.e('.tour-publish.deeplink').click()
		
		sleep(4)
		site_cnt = self.e('#container')
		buttons = site_cnt.es('.center')
		buttons_text = site_cnt.es('span')
		
		buttons_items = [
				['View my story'		, '/explore/'],
				['Contribute'			, '/upload/index/'],
				['Back to 1989 homepage', '/'],
		]
		
		sleep(3)
		
		for n in range(len(buttons_items)):
			i = buttons_items[n]
			self.assertEqual(i[0], buttons_text[n].text)
			self.assertIn('{0}/en{1}{2}'.format(URL_BASE, self.PROJECT_URL, i[1]), buttons[n].get_attribute('href'))
		
		self.go(self.ATTACH_URL + self.PROJECT_URL + '/tours/all')
		
		tour = self.e('#list li:nth-of-type(1)')
		self.assertEqual('{0}/services/thumb/phid/{1}/dim/290x210/crop/1/'.format(URL_BLOB, ID_TOUR_IMAGES[1]), tour.e('img').get_attribute('src'))
		
		tour.e('.delete').click()
		
		alert = self.browser.switch_to_alert()
		sleep(2)
		alert.accept()
		sleep(4)
		
		self.browser.refresh()
		self.assertFalse(self.e('#list').exists('.image_container.ss-icon.ss-photo[href*="{0}"]'.format(tour_id)))
