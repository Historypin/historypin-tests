from base import *
import os, sys

class Not_Logged(HPTestCase):
	
	@url('/en/person/65536/explore/pin/657460')
	def test_share(self):
		
		self.e('[ng-show="$state.params.pin"] .icon-share').click()
		self.e_wait('.share-link-container')
		
		displayed(self, '.share-container li a')
		displayed(self, '.embed-container')
		
		self.go('/en/person/65536')
		self.e_wait('.icon-share')
		
		self.e('.icon-share').click()
		
		self.e_wait('.share-link-container')
		
		displayed(self, '.share-container li a')
		displayed(self, '.embed-container')
		
		self.go('/en/premium-automated-collection')
		self.e_wait('.site-toolbar div:nth-of-type(1) .icon-share')
		
		self.e('.icon-arrow-down').click()
		sleep(1)
		
		self.e('.site-toolbar div:nth-of-type(1) .icon-share').click()
		
		self.e_wait('.share-link-container')
		
		displayed(self, '.share-container li a')
		displayed(self, '.embed-container')