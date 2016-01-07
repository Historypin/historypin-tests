# -*- coding: utf-8 -*-

from base import *
import os, sys

class Pages_View(HPTestCase):
	
	@url('/')
	def test_homepage(self):
		self.e_wait('.collections')
		sleep(1)
		
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
		self.e_wait('.gallery-listing a:nth-of-type(20) img')
		sleep(2)
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '.img-wrapper img')											# first project card
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
		sleep(1)
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/people', self.e('#main-header-nav li:nth-of-type(4) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/people', self.e('.page-desc a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.project-item:first-of-type')								# first card from listing
		displayed(self, '.pagination-list')
		displayed(self, '#intercom-launcher')
		self.e('.select2-input').send_keys('premium automated collection')
		sleep(2)
		
		self.e('.select2-result:nth-of-type(1)').click()
		# self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(3)
		
		self.assertEqual('Premium Automated Collection', self.e('.card-title').text)

	@url('/en/people')
	def test_meet_our_members(self):
		self.e_wait('.pagination-list')
		sleep(1)
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')								# search button
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.card')
		displayed(self, '.pagination-list')
		displayed(self, '.footer-col a')
		displayed(self, '#intercom-launcher')
		self.e('.select2-input').send_keys('kristesttwitter')						# search members
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(2)
		
		self.assertEqual('KrisTestTwitter', self.e('.card-title').text)

	@url('/en/places')
	def test_places(self):
		self.e_wait('.pagination-list')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/people', self.e('.page-desc a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/place/australia', self.e('.page-desc a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/place/zimbabwe', self.e('.page-desc a:nth-of-type(3)').get_attribute('href'))
		self.assertTrue(self.e('#search button.blue-bg').is_displayed())			# reset search button
		displayed(self, '.img-wrapper')												# place image first place card
		displayed(self, '.pagination-list')
		displayed(self, '.footer-col a')
		displayed(self, '#intercom-launcher')
		self.e('.home-search-input').send_keys("bulgaria")
		sleep(1)
		
		self.e('.home-search-input').send_keys(Keys.ENTER)
		sleep(1)
		
		self.assertEqual('Bulgaria', self.e('.desc-wrapper h3').text)
		
	@logged_in
	@url('/en/person/65536')
	def test_profile_view(self):
		sleep(5)
		# self.e_wait('.pin-item')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		displayed(self, '.profile-image')
		self.assertEqual('kris.test00', self.e('.profile-meta h2').text)
		displayed(self, '.activity-wrapper li')
		self.e('.activity-wrapper .button.blue-bg').click()							# expand activity field button 
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/list/collections', self.e('#projects:nth-of-type(2) .button').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/explore/', self.e('#projects:nth-of-type(2) .button:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/list/pins', self.e('#pins .button:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/explore/', self.e('#pins .button:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/list/tours', self.e('#tours .button:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/explore/', self.e('#tours .button:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/list/pins_favourited', self.e('#favourites .button:nth-of-type(1)').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/explore/search/pin:favourite', self.e('#favourites .button:nth-of-type(2)').get_attribute('href'))
		displayed(self, '#projects .icon-pen')										# edit button on first card project
		displayed(self, '#projects .icon-trash')									# delete button on first card project
		displayed(self, '#pins .icon-pen')											# edit button on first pin card
		displayed(self, '#pins .icon-trash')										# delete button on first pin card
		displayed(self, '#tours .icon-pen')											# edit button on first tour card
		displayed(self, '#tours .icon-trash')										# delete button on first tour card
		displayed(self, '#favourites a')
		displayed(self, '.footer-col a')
		displayed(self, '#intercom-launcher')
		
		side_buttons_profile(self)
		
	# @logged_in
	# @url('/en/person/65536')
	# def test_profil_edit(self):
	# 	self.e_wait('.icon-edit')
		
	# 	self.e('.icon-edit').click()
	# 	self.e_wait('#save-mah')
		
	# 	self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
	# 	displayed(self, '.profile-image')
	# 	displayed(self, '.icon-trash')
	# 	displayed(self, '#name')
	# 	displayed(self, '#description')
	# 	displayed(self, '#place')
	# 	displayed(self, '#birthyear')
	# 	displayed(self, '#website')
	# 	displayed(self, '#facebook')
	# 	displayed(self, '#twitter')
	# 	displayed(self, '#google-plus')
	# 	displayed(self, '[for="facebook_switch"]')
	# 	displayed(self, '[for="twitter_switch"]')
	# 	displayed(self, '[for="google_switch"]')
	# 	displayed(self, '[for="notification_switch"]')
	# 	displayed(self, '[for="newsletter_switch"]')
	# 	displayed(self, '[for="featured_user"]')
	# 	displayed(self, '.edit-option-panel h5')
	# 	displayed(self, '.footer-col a')
	# 	displayed(self, '#intercom-launcher')
	# 	instance(self, '[class="file-input"]')
	# 	instance(self, '[label="1900"]')
	# 	instance(self, '[label="1999"]')
		
		
	@url('/en/person/65536/list/collections')
	def test_collection_list(self):
		self.e_wait('.card')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536', self.e('.page-desc a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.project-item:first-of-type')								# first card from listing
		displayed(self, '#intercom-launcher')
		self.e('.select2-input').send_keys('premium automated collection')
		sleep(2)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(3)
		
		self.assertEqual('Premium Automated Collection', self.e('.card-title').text)
		
	@url('/en/person/65536/explore')
	def test_collections_explore(self):
		self.e_wait('.card')
		sleep(1)
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('kris.test00', self.e('.simple-banner h2').text)
		displayed(self, '#sort-select')												# order filter
		displayed(self, '.img-wrapper img')											# first project card
		displayed(self, '#map')
		displayed(self, '#timeline')												# map timeline
		displayed(self, '.layout-triger')											# expand map and gallery button
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/', self.e('.site-toolbar a').get_attribute('href'))
		self.e('.select2-input').send_keys('premium automated collection')
		sleep(2)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(4)
		
		self.assertEqual('Premium Automated Collection', self.e('.card-title').text)
		
	@url('/en/person/65536/list/pins')
	def test_pins_list(self):
		self.e_wait('.card')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536', self.e('.page-desc a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.card')													# first card from listing
		displayed(self, '#intercom-launcher')
		self.e('.select2-input').send_keys('selenium pin')
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(2)
		
		self.assertEqual('Selenium pin', self.e('.card-title').text)
		
	@url('/en/person/65536/list/tours')
	def test_tours_list(self):
		self.e_wait('.card')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536', self.e('.page-desc a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.card')													# first card from listing
		displayed(self, '#intercom-launcher')
		self.e('.select2-input').send_keys('premium automated tour')
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		sleep(2)
		
		self.assertEqual('Premium Automated Tour', self.e('.card-title').text)
		
	@url('/en/person/65536/list/pins_favourited')
	def test_favourited_list(self):
		self.e_wait('.card')
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536', self.e('.page-desc a').get_attribute('href'))
		displayed(self, '#sort-select')												# order filter
		displayed(self, '#search button:first-of-type')
		displayed(self, '#search button.blue-bg')									# reset search button
		displayed(self, '.card')													# first card from listing
		displayed(self, '#intercom-launcher')
		#after fix search bug
		# self.e('.select2-input').send_keys('at the loibl obelisks')
		# sleep(1)
		
		# self.e('.select2-input').send_keys(Keys.ENTER)
		# sleep(3)
		
		# self.assertEqual('At the loibl obelisks', self.e('.card-title').text)
		
	@url('/en/person/65536/explore/search/pin:favourite')
	def test_favourited_explore(self):
		self.e_wait('.card')
		sleep(1)
		
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/collections/', self.e('#main-header-nav li:nth-of-type(3) a').get_attribute('href'))
		self.assertEqual('kris.test00', self.e('.simple-banner h2').text)
		displayed(self, '#sort-select')												# order filter
		displayed(self, '.img-wrapper img')											# first project card
		displayed(self, '#map')
		displayed(self, '#timeline')												# map timeline
		displayed(self, '.layout-triger')											# expand map and gallery button
		self.assertEqual('http://v75-beta-2.historypin-hrd.appspot.com/en/person/65536/', self.e('.site-toolbar a').get_attribute('href'))
		self.e('.select2-input').send_keys('at the loibl obelisks')
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)
		self.e('.select2-input').send_keys('at the loibl obelisks')
		sleep(1)
		
		self.e('.select2-input').send_keys(Keys.ENTER)								# temporary solution
		sleep(3)
		
		self.assertEqual('At the Loibl obelisks', self.e('.card-title').text)
		
		
		