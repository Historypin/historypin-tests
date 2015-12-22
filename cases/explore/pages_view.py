# -*- coding: utf-8 -*-

from base import *
import os, sys
import logging

class Pages_View(HPTestCase):
	
	@url('/')
	def test_homepage(self):
		self.e_wait('.collections')
		
		displayed(self, '.collections :nth-child(9)')								# check displayed collection == 9
		displayed(self, '#main-header-logo')
		self.assertEqual('Explore Historypin', self.e('#main-header-nav li').text)
		displayed(self, '.entrance-type')
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/people', self.e('.explore-collections a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections', self.e('.button-center-wrapp a').get_attribute('href'))
		displayed(self, '.footer-col a')
		displayed(self, '#intercom-launcher')
		self.e('.home-search-input').send_keys('los angeles')
		sleep(1)
		
		self.e('.home-search-input').send_keys(Keys.ENTER)
		self.e_wait('.title')
		self.assertTrue('http://www.v75-beta-2.historypin-hrd.appspot.com/en/explore/geo/34.052234,-118.243685,10/bounds/33.532954,-118.538256,34.568353,-117.949114', url)

	@url('/en/explore')
	def test_explore_view(self):
		self.e_wait('.pagination-list')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '.img-wrapper')												# first project card
		displayed(self, '#map')
		displayed(self, '#timeline')												# map timeline
		displayed(self, '.layout-triger')											# expand map and gallery button
		displayed(self, '.pagination-list')
		displayed(self, '#intercom-launcher')
		side_buttons(self)
		
		self.e('.select2-input').send_keys('pin')									# search by tag or keyword
		sleep(1)
		
		self.e('.select2-result:nth-of-type(2)').click()
		self.e_wait('.pin-item')

	@url('/en/collections')
	def test_all_collections(self):
		self.e_wait('.pagination-list')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/people', self.e('#main-header-nav li:nth-of-type(4) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/people', self.e('.page-desc a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.project-item:first-of-type')								# first card from listing
		displayed(self, '.pagination-list')
		displayed(self, '#intercom-launcher')
		self.e('.select2-input').send_keys('premium automated collection')
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		self.e_wait('.card-title')
		
		self.assertEqual('Premium Automated Collection', self.e('.card-title').text)

	@url('/en/people')
	def test_meet_our_members(self):
		self.e_wait('.pagination-list')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')								# search button
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.card')
		displayed(self, '.pagination-list')
		displayed(self, '#intercom-launcher')
		displayed(self, '#search button.blue-bg')									# reset search button
		self.e('.select2-input').send_keys('kristesttwitter')						# search members
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(1)
		
		self.assertEqual('KrisTestTwitter', self.e('.card-title').text)

	@logged_in
	@url('/en/person/65536')
	def test_profile_view(self):
		sleep(5)
		# self.e_wait('.pin-item')
		
		self.assertTrue(self.e('.profile-image').is_displayed())
		self.assertTrue(self.e('.profile-meta').is_displayed())
		self.assertTrue(self.e('.activity-wrapper').is_displayed())
		self.assertTrue(self.e('.activity-wrapper .button.blue-bg').is_displayed())	# expand activity field button 
		self.assertTrue(self.e('#projects .icon-pen').is_displayed())				# edit button on first card project
		self.assertTrue(self.e('#projects .icon-trash').is_displayed())				# delete button on first card project
		self.exists('#pins .icon-pen')												# edit button on first pin card
		self.exists('#pins .icon-trash')											# delete button on first pin card
		self.exists('#tours .icon-pen')												# edit button on first tour card
		self.exists('#tours .icon-trash')											# delete button on first tour card
		self.exists('#favourites')
		
		side_buttons_profile(self)

	@url('/en/places')
	def test_places(self):
		self.e_wait('.pagination-list')
		
		self.assertTrue(self.e('.main-header-cnt').is_displayed())
		self.assertTrue(self.e('.home-search-input').is_displayed())				# search place
		self.assertTrue(self.e('#search button.blue-bg').is_displayed())			# reset search button
		self.exists('.img-wrapper')													# place image first place card
		self.exists('.pagination-list')
		
		
		