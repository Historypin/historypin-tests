from base import *
import os, sys

class Favourite_Pin(HPTestCase):
	
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def test_favourite(self):
		
		self.e_wait('.pin-item img')
		sleep(1)
		
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.assertEqual('Selenium pin', self.e('.pin-item h3').text)
		self.e('.pin-item').click()
		self.e_wait('.icon-heart')
		sleep(2)
		
		fav_counter = int(self.e('#fav-counter.ng-binding').text)
		self.e('.icon-heart').click()
		sleep(1)
		
		new_fav_counter = int(self.e('#fav-counter.ng-binding').text)
		self.assertTrue(new_fav_counter == (fav_counter + 1))
		
		self.unfavourite()
		
	@logged_in
	@url('/en/person/{0}/'.format(ID_USER))
	def unfavourite(self):
		
		self.e_wait('.pin-item img')
		
		self.assertEqual('now', self.e('.activity li:first-of-type .time').text)
		self.assertEqual('Selenium pin', self.e('#favourites .pin-item h3').text)
		self.assertTitle("Historypin | kris.test00's Historypin profile")
		self.e('.pin-item').click()
		self.e_wait('.icon-heart')
		sleep(2)
		
		fav_counter = int(self.e('#fav-counter.ng-binding').text)
		self.e('.icon-heart').click()
		sleep(1)
		
		new_fav_counter = int(self.e('#fav-counter.ng-binding').text)
		self.assertTrue(new_fav_counter == (fav_counter - 1))