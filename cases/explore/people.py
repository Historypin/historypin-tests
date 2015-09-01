# -*- coding: utf-8 -*-

from base import *
import os, sys

class People(HPTestCase):
	
	@url('/en/people')
	def test_index(self):
		
		self.assertTitle('Historypin | People')
		page_desc = self.e('.page-desc')
		
		self.assertEqual('{0}/en/collections'.format(URL_BASE), page_desc.e('a:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('{0}/en/places'.format(URL_BASE), page_desc.e('a:nth-of-type(2)').get_attribute('href'))
		
		self.assertEqual('Members', self.e('h3').text)
	
	@url('/en/people')
	def test_search_username(self):
		
		self.e('.select2-input.select2-default').send_keys('Gabriela')
		sleep(2)
		self.e('.select2-results li:nth-of-type(2)').click()
		sleep(3)
		
		users = [
			['35019/', 'Gabriela Ananieva'],
			['53986/', 'Gabriela Ananieva'],
		]
		
		user_listing	= self.es('.card a')
		user_name		= self.es('.card h3')
		# user_links = user_listing.e('a')
		# user_name = user_listing.es('Gabriela Ananieva')
		
		for n in range(len(users)):
			i = users[n]
			self.assertEqual('{0}/en/person/{1}'.format(URL_BASE, i[0]), user_listing[n].get_attribute('href'))
			self.assertEqual(i[1], user_name[n].text)
		
	
	
	# @url('')
	# def test_most_popular(self):
		
	# 	# assert if the option menu is ordered by most popular
	# 	# check if the first profile is most viewed
	# 	pass
	
	
	