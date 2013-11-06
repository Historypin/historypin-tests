# -*- coding: utf-8 -*-

from base import *

class Project_Balboa(HPTestCase):
	@url('/project/6-balboa')
	def test_index(self):
		
		self.assertTitle('Balboa Park | Home')
		
		logo_link = self.e('#logo-title a')
		
		self.assertEqual('http://balboapark.org/', logo_link.get_attribute('href'))
		self.assertEqual('%s/resources/images/webapps/balboa/logo.png' % URL_BASE, logo_link.e('img').get_attribute('src'))
		
		self.assertEqual('%s/attach/project/6-balboa/photos/index/' % URL_BASE, self.e('#embed-frame').get_attribute('src'))
		
		balboa_link = 'http://www.balboapark.org'
		
		footer_items = [
			['%s/info/' % balboa_link				, 'About'],
			['%s/faq' % URL_BASE					, 'FAQs'],
			['%s/terms-and-conditions' % URL_BASE	, 'Terms & Conditions'],
			['%s/contact/' % balboa_link			, 'Contact'],
		]
		
		footer = self.e('#supp')
		footer_links = footer.es('li a')
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], footer_links[n].get_attribute('href'))
			self.assertEqual(i[1], footer_links[n].text)
		
	
	@url('/attach/project/6-balboa/map/')
	def test_map_tab(self):
		
		
		
		
		pass
	
	@url('/attach/project/6-balboa/collections/all/')
	def test_collections_tab(self):
		pass
	
	@url('/attach/project/6-balboa/contribute/')
	def test_contribute_tab(self):
		pass
	
	