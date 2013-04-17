from base import *

class Pages(HPTestCase):
	
	@url('/about-us/')
	def test_about(self):
		self.assertTitle('Historypin | A 90 second introduction')
		
		self.assertEqual(self.e('#site-content h1.title').text, 'A 90 second introduction')
		self.assertEqual(self.e('iframe').get_attribute('src'), 'http://www.youtube.com/embed/FdT3eKdto4w?rel=0')
	
	@unittest.skip("TODO")
	@url('/')
	def test_app(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_contacts(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_faq(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_press_center(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_privacy_policy(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_support(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_toc(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_team(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_wawwd(self):
		pass

class Community(HPTestCase):
	@unittest.skip("TODO")
	@url('/')
	def test_home(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_home_lams(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_home_projects(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_home_schools(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_how_tos(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_lams_involved(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_lams(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_projects(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_projects_studies(self):
		pass
	
	@unittest.skip("TODO")
	@url('/')
	def test_topics_to_explore(self):
		pass

class CommunitySchools(HPTestCase):
	'''
	Community - Schools
	Community - Schools - Case Studies
	Community - Schools - Case Studies - EIC
	Community - Schools - How To Guides
	Community - Schools - Resources
	Community - Schools - Case Studies - Billericay, Essex, UK
	Community - Schools - Case Studies - Cromer, Norfolk, UK
	Community - Schools - Case Studies - Nelson
	Community - Schools - Case Studies - Newport Primary School, Essex, UK
	'''
	
	
	
	pass
