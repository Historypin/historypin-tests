from base import *
import os, sys

class Not_Logged(HPTestCase):
	
	@url('/en/person/65536/explore/pin/657460')
	def test_share(self):
		
		self.e('[ng-show="$state.params.pin"] .icon-share').click()
		self.e_wait('.share-link-container')
		
		displayed(self, 		'.share-container li a')
		displayed(self, 		'.embed-container')
		
		self.go('/en/person/65536')
		self.e_wait('.icon-share')
		
		self.e('.icon-share').click()
		self.e_wait('.share-link-container')
		
		displayed(self, 		'.share-container li a')
		displayed(self, 		'.embed-container')
		
		self.go('/en/premium-automated-collection')
		self.e_wait('.site-toolbar div:nth-of-type(1) .icon-share')
		
		self.e('.icon-arrow-down').click()
		sleep(1)
		
		self.e('.site-toolbar div:nth-of-type(1) .icon-share').click()
		self.e_wait('.share-link-container')
		
		displayed(self, 		'.share-container li a')
		displayed(self, 		'.embed-container')
	
	@url('/en/person/65536/explore/pin/657460')
	def test_favourite(self):
		self.e_wait('.site-toolbar .icon-heart')
		
		self.e('.site-toolbar .icon-heart').click()
		self.e_wait('.show-join')
		
		self.assertEqual("Sorry to interrupt, but you'll need to login or create an account to do that. Should only take a minute and we'll send you on your way.'", self.e('.forced-log').text)
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
	@url('/en/person/65536/explore/pin/657460')
	def test_repin(self):
		
		self.e('.icon-repin').click()
		self.e_wait('.show-join')
		
		self.assertEqual("Sorry to interrupt, but you'll need to login or create an account to do that. Should only take a minute and we'll send you on your way.'", self.e('.forced-log').text)
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
	@url('/en/premium-automated-collection')
	def test_add_pin(self):
		self.e('.icon-arrow-down').click()
		sleep(1)
		
		self.e('.icon-add-pin').click()
		self.e_wait('.show-join')
		
		self.assertEqual("Sorry to interrupt, but you'll need to login or create an account to do that. Should only take a minute and we'll send you on your way.'", self.e('.forced-log').text)
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
		self.go('/en/person/65536/')
		self.e_wait('.site-toolbar .icon-add-pin')
		
		self.e('.site-toolbar .icon-add-pin').click()
		sleep(2)
		
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		self.assertEqual('Welcome back! Please login to your account', self.e('.login-dialog .normal-log').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
	@url('/en/person/65536/')
	def test_add_collection(self):
		self.e_wait('.icon-add-collection')
		
		self.e('.icon-add-collection').click()
		sleep(1)
		
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		self.assertEqual('Welcome back! Please login to your account', self.e('.login-dialog .normal-log').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
		self.go('/en/premium-automated-collection')
		self.e('.icon-arrow-down').click()
		sleep(1)
		
		self.e('.site-toolbar .icon-add-collection').click()
		sleep(1)
		
		self.assertEqual("Sorry to interrupt, but you'll need to login or create an account to do that. Should only take a minute and we'll send you on your way.'", self.e('.forced-log').text)
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
	@url('/')
	def test_sign_join(self):
		
		self.e('.btn-sign-in').click()
		sleep(1)
		
		self.assertEqual('New to Historypin?', self.e('.login-dialog .new-to-hp p').text)
		self.assertEqual('Welcome back! Please login to your account', self.e('.login-dialog .normal-log').text)
		
		displayed(self, 		'.login-dialog .new-to-hp a')
		displayed(self, 		'.login-dialog #login-google')
		displayed(self, 		'.login-dialog #login-facebook')
		displayed(self, 		'.login-dialog #login-twitter')
		displayed(self, 		'.login-dialog #sign-mail')
		
		self.e('.login-dialog .icon-close').click()
		sleep(1)
		
		self.e('.btn-join').click()
		sleep(1)
		
		self.assertEqual('JOIN HISTORYPIN', 																self.e('.join-dialog h3').text)
		self.assertEqual('Sign up for a free account and become a member of the Historypin community', 		self.e('#dialog-wrapper p').text)
		self.assertEqual('Already have an account?', 														self.e('#dialog-wrapper .new-to-hp p').text)
		self.assertEqual('http://v76-beta-1.historypin-hrd.appspot.com/terms-and-conditions/', 				self.e('.field-wrapp [for="accepted_toc"] a').get_attribute('href'))
		self.assertEqual('http://v76-beta-1.historypin-hrd.appspot.com/privacy-policy/', 					self.e('.field-wrapp [for="accepted_toc"] a:nth-of-type(2)').get_attribute('href'))
		
		displayed(self, 		'.show-login')
		displayed(self, 		'#dialog-wrapper #login-google')
		displayed(self, 		'#dialog-wrapper #login-facebook')
		displayed(self, 		'#dialog-wrapper #login-twitter')
		displayed(self, 		'#dialog-wrapper #login-mail')
		displayed(self, 		'.field-wrapp #accepted_toc')				# agree checkbox
		
	@url('/en/premium-automated-collection')
	def test_about_panel(self):
		
		self.e('.icon-arrow-down').click()
		sleep(1)
		
		self.e('.site-toolbar .icon-info').click()
		sleep(1)
		
		self.assertEqual('ABOUT THE COLLECTION', 															self.e('.about .about-cnt h1').text)
		self.assertEqual('Premium Automated Collection', 													self.e('.project-description-wrapper h2').text)
		self.assertEqual('Premium Automated Collection', 													self.e('.project-description.section-bottom-line p').text)
		self.assertEqual('CONTRIBUTION', 																	self.e('.contribution-sec h4').text)
		self.assertEqual('ON', 																				self.e('.status-indicator-copy').text)
		self.assertEqual('@automation awesome', 															self.e('.contact p').text)
		self.assertEqual('PART OF', 																		self.e('.related-cards h4').text)
		self.assertEqual('ACTIVITY', 																		self.e('.activity-wrapper h4').text)
		self.assertEqual('DISCUSSION', 																		self.e('.comments .pane-section-title').text)
		self.assertEqual('kris.test00', 																	self.e('.type-of-activity a').text)
		self.assertEqual('http://v76-beta-1.historypin-hrd.appspot.com/en/premium-automated-collection/', 	self.e('.type-of-activity a:nth-of-type(2)').get_attribute('href'))
		self.assertEqual('Nobody is discussing this collection yet. Be the first to comment!', 				self.e('.comments .zero-state-message p').text)
		self.assertEqual('COLLECTION MANAGERS', 															self.e('.about-sidebar h4').text)
		self.assertEqual('kris.test00', 																	self.e('.about-sidebar .user-name').text)
		
		displayed(self, 		'.comments .zero-state-message a')
		displayed(self, 		'.activity .time')
		displayed(self, 		'.places-card img')
		displayed(self, 		'.project-stats p')
		displayed(self, 		'.about-cnt .section-top-line .icon-close')
		
		
		