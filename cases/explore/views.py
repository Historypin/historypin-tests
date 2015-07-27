# -*- coding: utf-8 -*-

from base import *
import os, sys

class Pages_View(HPTestCase):
	
	# TODO Put in order test later to be in seperate files
	# TODO These later could be extended to fully check the content and/or functionality.
	
	@url('{0}/en/'.format(URL_BASE))
	def test_homepage_view(self):
		
		self.assertTitle('Historypin | Home')
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		
		page_intro = self.e('.page-intro')
		self.assertEqual('{0}/resources/explore/images/homepage-intro-image.jpg'.format(URL_BASE), page_intro.e('img').get_attribute('src'))
		self.assertEqual('Working Together To\nRemember Our History', page_intro.e('h1').text)
		
		self.assertIsInstance(self.e('.partners'), WebElement)
		
		# TODO assert all sections in the future when the test is extended and it is the seperate test suite
	
	@url('{0}/en/collections/'.format(URL_BASE))
	def test_collections_view(self):
		
		self.assertTitle('Historypin | Collections')
		
		all_collections_cnt = self.e('.container.projects-all')
		self.assertEqual('Collections', all_collections_cnt.e('h1').text)
		
		self.assertIsInstance(self.e('#search'), WebElement)
	
	@url('{0}/en/oreo/'.format(URL_BASE))
	def test_explore_view(self):
		
		self.assertTitle('Historypin | Project\'s for Quality Assurance')
		
		self.assertIsInstance(self.e('#banner'), WebElement)
	
	@url('{0}/en/new-project-qa/collection/edit'.format(URL_BASE))
	def test_collection_edit_view(self):
		
		self.assertIsInstance(self.e('#explore'), WebElement)
		self.assertEqual('EDIT THE COLLECTION', self.e('.about h1').text)
	
	@url('{0}/en/test-tour-for-automated-test/collection/edit'.format(URL_BASE))
	def test_tour_edit_view(self):
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertIsInstance(self.e('#explore'), WebElement)
	
	@logged_in
	@url('{0}/en/collection/create'.format(URL_BASE))
	def test_collection_create_view(self):
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertIsInstance(self.e('#explore'), WebElement)
		
		self.assertEqual('EDIT THE COLLECTION', self.e('.about h1').text)  # TODO should be fixed because we're on create collection, not edit
	
	@logged_in
	@url('{0}/en/collection/create-tour'.format(URL_BASE))
	def test_tour_create_view(self):
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertIsInstance(self.e('#explore'), WebElement)
	
	@url('{0}/en/people/'.format(URL_BASE))
	def test_people_view(self):
		
		self.assertTitle('Historypin | People')
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertIsInstance(self.e('.users-listing'), WebElement)
	
	@url('{0}/en/person/{1}'.format(URL_BASE, ID_USER))
	def test_person_view(self):
		
		self.assertIsInstance(self.e('.profile-header'), WebElement)
		
		self.assertEqual('Gabriela Ananieva', self.e('h2').text)
	
	@url('{0}/en/person/{1}/edit'.format(URL_BASE, ID_USER))
	def test_person_edit_view(self):
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertIsInstance(self.e('#person-edit'), WebElement)
	
	@url('{0}/en/person/{1}/list/tours'.format(URL_BASE, ID_USER_VIEW))
	def test_person_list_tours_view(self):
		
		self.assertIsInstance(self.e('.projects-all'), WebElement)
		self.assertEqual('Tours', self.e('.projects-all h1').text)
		
	@url('{0}/en/person/{1}/list/collections'.format(URL_BASE, ID_USER_VIEW))
	def test_person_list_collections_view(self):
		
		self.assertIsInstance(self.e('.projects-all'), WebElement)
		self.assertEqual('Collections', self.e('.projects-all h1').text)
	
	@url('{0}/en/person/{1}/list/pins'.format(URL_BASE, ID_USER_VIEW))
	def test_person_list_pins_view(self):
		
		self.assertIsInstance(self.e('.projects-all'), WebElement)
		self.assertEqual('Pins', self.e('.projects-all h1').text)
	
	@url('{0}/en/places/'.format(URL_BASE))
	def test_places_view(self):
		
		self.assertTitle('Historypin | Places')
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertIsInstance(self.e('.listing'), WebElement)
	
	@url('{0}/en/place/bulgaria/'.format(URL_BASE))
	def test_place_level0_view(self):
		
		self.assertIsInstance(self.e('.place-map-wrapper'), WebElement)
		self.assertEqual('Bulgaria', self.e('.container h1').text)
	
	@url('{0}/en/place/bulgaria/list/subplaces'.format(URL_BASE))
	def test_place_list_regions_view(self):
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertEqual('Regions', self.e('.projects-all h1').text)
	
	@url('{0}/en/place/bulgaria/list/people'.format(URL_BASE))
	def test_place_list_users_view(self):
		
		self.assertIsInstance(self.e('#main-header'), WebElement)
		self.assertEqual('Pinners who are collaborating on collections and have made comments', self.e('.users-listing .ng-scope h3+p').text)
	
	@url('{0}/en/place/bulgaria/sofia-stolitsa'.format(URL_BASE))
	def test_place_level1_view(self):
		
		self.assertIsInstance(self.e('.place-map-wrapper'), WebElement)
		self.assertEqual('Sofia (stolitsa), Bulgaria', self.e('.container h1').text)
	
	@url('{0}/en/place/bulgaria/sofia-stolitsa/list/collections'.format(URL_BASE))
	def test_place_list_collections_view(self):
		
		self.assertIsInstance(self.e('.projects-all'), WebElement)
		self.assertEqual('Collections', self.e('.projects-all h1').text)
	
	@url('{0}/en/place/bulgaria/sofia-stolitsa/list/tours'.format(URL_BASE))
	def test_place_list_tours_view(self):
		
		self.assertIsInstance(self.e('.projects-all'), WebElement)
		self.assertEqual('Tours', self.e('.projects-all h1').text)
	
	@url('{0}/en/place/bulgaria/sofia-stolitsa/list/pins'.format(URL_BASE))
	def test_place_list_pins_view(self):
		
		self.assertIsInstance(self.e('.projects-all'), WebElement)
		self.assertEqual('Pins', self.e('.projects-all h1').text)
	