# -*- coding: utf-8 -*-

from base import *
import os, sys
import logging

class Pages_View(HPTestCase):
	
	@url('/')
	def test_homepage(self):
		self.e_wait('.collections')
		
		self.assertTrue(self.e('#main-header-logo').is_displayed())
		self.assertTrue(self.e('#main-header-nav').is_displayed())
		self.assertTrue(self.e('.entrance-type').is_displayed())
		self.exists('.home-search-input')
		self.exists('.collections')

	@url('/en/explore')
	def test_explore_view(self):
		self.e_wait('.pagination-list')
		
		self.assertTrue(self.e('.main-header-cnt').is_displayed())
		self.assertTrue(self.e('#search .select2-search-field').is_displayed())		# search by tag or keyword
		self.assertTrue(self.e('#sort-select').is_displayed())						# order filter
		self.assertTrue(self.e('.gallery-listing').is_displayed())
		self.assertTrue(self.e('#map').is_displayed())
		self.exists('#timeline')													# map timeline
		self.assertTrue(self.e('.layout-triger').is_displayed())					# expand map and gallery button
		self.exists('.pagination-list')
		
		side_buttons(self)

	@url('/en/collections')
	def test_all_collections(self):
		self.e_wait('.pagination-list')
		
		self.assertTrue(self.e('.main-header-cnt').is_displayed())
		self.assertTrue(self.e('.select2-search-field').is_displayed())				# search collections
		self.assertTrue(self.e('#sort-select').is_displayed())
		self.assertTrue(self.e('#search button:first-of-type').is_displayed())		# order filter
		self.assertTrue(self.e('#search button.blue-bg').is_displayed())			# reset search button
		self.assertTrue(self.e('.project-item:first-of-type').is_displayed())		# first card from listing
		self.exists('.pagination-list')

	@url('/en/people')
	def test_meet_our_members(self):
		self.e_wait('.pagination-list')
		
		self.assertTrue(self.e('.main-header-cnt').is_displayed())
		self.assertTrue(self.e('.select2-search-field').is_displayed())				# search members
		self.assertTrue(self.e('#sort-select').is_displayed())						# order filter
		self.assertTrue(self.e('#search button:first-of-type').is_displayed())		# search button
		self.assertTrue(self.e('#search button.blue-bg').is_displayed())			# reset search button
		self.exists('.users-listing')
		self.exists('.pagination-list')

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
		
		
		