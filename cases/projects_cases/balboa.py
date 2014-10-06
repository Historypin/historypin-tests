# -*- coding: utf-8 -*-

from base import *
from attach import Attach

class Project_Balboa(HPTestCase, Attach):
	
	PROJECT_URL		= '/project/6-balboa'
	project_name	= 'balboa'
	# cannot check because #embed_tabs in Balboa doesn't exist
	# ATTACH_TABS = [
	# 	['http://www.balboapark.org/historypin', '%s/attach%s/map/index/' % (URL_BASE, PROJECT_URL), '%s/attach%s/collections/all/' % (URL_BASE, PROJECT_URL), '%s/attach%s/tours/all/' % (URL_BASE, PROJECT_URL), '%s/attach%s/contribute/' % (URL_BASE, PROJECT_URL)],
	# ]
	# test_attach_tabs		= Attach.attach_tabs
	
	test_tab_collections	= Attach.attach_tab_collections
	test_tab_tours_empty	= Attach.attach_tab_tours_empty
	
	def test_tab_map(self):
		self.go('/attach{0}/map/'.format(self.PROJECT_URL))
		
		sleep(4)
		
		self.assertIsInstance(self.e('#date-slider-wrapper'), WebElement)
		self.assertIsInstance(self.e('#tags'), WebElement)
		
		sleep(5)
		
		# no way to do this in selenium as the counter element is hidden
		self.browser.execute_script("ms = $('.hp-marker.hp-marker-cluster'); for(i in ms){ m = ms[i]; if($('.hp-marker-count', m).text() < 100 ){ m.click(); break; } }")
		
		sleep(3)
		cluster = self.e('#galleryInfoWindow_contents li:nth-of-type(1)')
		
		self.assertIsInstance(cluster.e('.hp-info-gallery-pin img'), WebElement)
		self.assertIsInstance(cluster.e('.info h6 a'), WebElement)
		self.assertIsInstance(cluster.e('.info p'), WebElement)
		
		cluster.e('.hp-info-gallery-pin img').click()
		sleep(2)
		self.assertIsInstance(self.e('#info-dialog'), WebElement)
	
	def test_index(self):
		self.go(self.PROJECT_URL)
		
		self.assertTitle('Balboa Park | Home')
		
		logo_link = self.e('#logo-title a')
		
		self.assertEqual('http://balboapark.org/', logo_link.get_attribute('href'))
		self.assertEqual('{0}/resources/images/webapps/balboa/logo.png'.format(URL_BASE), logo_link.e('img').get_attribute('src'))
		
		self.assertEqual('{0}/attach{1}/map/index/'.format(URL_BASE, self.PROJECT_URL), self.e('#embed-frame').get_attribute('src'))
		
		balboa_link = 'http://www.balboapark.org'
		
		footer_items = [
			['{0}/info/'.format(balboa_link), 'About'],
			['{0}/faq'.format(URL_BASE)		, 'FAQs'],
			['{0}/terms-and-conditions'.format(URL_BASE), 'Terms & Conditions'],
			['{0}/contact/'.format(balboa_link)			, 'Contact'],
		]
		
		footer = self.e('#supp')
		footer_links = footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
		
	
	def test_tab_tours(self):
		self.go('/attach{0}/tours/all/'.format(self.PROJECT_URL))
		
		self.assertEqual("balboa hasn't yet published any Tours.", self.e('#page-index h3').text)
	
	def test_tab_contribute(self):
		self.go('/attach{0}/contribute/'.format(self.PROJECT_URL))
		
		contribute_cnt = self.e('#tab-contribute')
		self.assertEqual('Pin your photos using', contribute_cnt.e('h1').text)
		
		self.assertEqual('{0}/user/?from={1}/%23%7Cupload/'.format(URL_BASE, self.PROJECT_URL), contribute_cnt.e('.pin_bridge').get_attribute('href'))
		
		paragraph_links = [
			['Pin your photos to Balboa Park using Historypin'			, '{0}/user/?from={1}/%23%7Cupload/'.format(URL_BASE, self.PROJECT_URL)],
			['Find out more about the not-for-profit project Historypin', '{0}/'.format(URL_BASE)],
		]
		
		links = contribute_cnt.es('p a')
		
		for n in range(len(paragraph_links)):
			i = paragraph_links[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
		
	
