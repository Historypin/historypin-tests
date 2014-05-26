# -*- coding: utf-8 -*-

from base import *

class Suggestions(HPTestCase):
	
	@unittest.expectedFailure  # to test with test photo, suggestions should be allowed on the map
	@url('dialog:/%d/tab:write-story/suggest:title/' % ID_MAP_ITEM)
	def test_title_suggestion(self):
		# TODO
		title_option = self.e('#suggestion_field option:nth-of-type(2)')
		self.assertTrue(title_option.is_selected())
		self.assertEqual('Title', title_option.text)
		
		self.e('#suggestion_title input').send_keys('Bulgarian theater')
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think this is the right title')
		self.e('.apply').click()
		
		sleep(4)
		
		self.assertTrue(self.e('#info-dialog'), WebElement)
		
		title_suggestion = ('.stories_list .suggestion.title')
		self.assertEqual(self.e('#photo-side .photo-title').text, title_suggestion.e('.ba_from .value').text)  # to compare if the title is equal to photo title
		
		self.assertEqual('Bulgarian theater'				, title_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think this is the right title'	, title_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(title_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@unittest.expectedFailure
	@url('dialog/%d/tab:write-story/suggest:date/' % ID_MAP_ITEM)
	def test_specific_date_suggestion(self):
		
		sp_date_option = self.e('#suggestion_field option:nth-of-type(3)')
		self.assertTrue(sp_date_option.is_selected())
		self.assertEqual('Date', sp_date_option.text)
		
		self.e('#day option:nth-of-type(4)').click()
		self.e('#month option:nth-of-type(10)').click()
		self.e('#year option:nth-of-type(4)').click()
		
		# TODO check if it is correct
		self.assertEqual('disabled', self.e('#year_from').get_attribute('class'))
		self.assertEqual('disabled', self.e('#year_to').get_attribute('class'))
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think this is the right specific date')
		self.e('.apply').click()
		
		sleep(4)
		
		sp_date_suggestion = ('.stories_list .suggestion.date')
		self.assertEqual(self.e('#photo-side .photo-date').text		, sp_date_suggestion.e('.ba_from .value').text)
		self.assertEqual('3 September 2012'							, sp_date_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think this is the right specific date'	, sp_date_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(sp_date_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('dialog/%d/tab:write-story/suggest:date/' % ID_MAP_ITEM)
	def test_timeframe_date_suggestion(self):
		
		date_option = self.e('#suggestion_field option:nth-of-type(3)')
		self.assertTrue(date_option.is_selected())
		self.assertEqual('Date', date_option.text)
		
		self.e('#year_from option:nth-of-type(4)').click()
		self.e('#year_to option:nth-of-type(3)').click()
		
		self.assertEqual('disabled', self.e('#day').get_attribute('class'))
		self.assertEqual('disabled', self.e('#month').get_attribute('class'))
		self.assertEqual('disabled', self.e('#year').get_attribute('class'))
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think this is the right timeframe')
		self.e('.apply').click()
		
		sleep(4)
		
		date_timeframe_suggestion = ('.stories_list .suggestion.date')
		self.assertEqual(self.e('#photo-side .photo-date').text	, date_timeframe_suggestion.e('.ba_from .value').text)
		self.assertEqual('2012 - 2013'							, date_timeframe_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think this is the right timeframe'	, date_timeframe_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(date_timeframe_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('dialog/%d/tab:write-story/suggest:keywords/' % ID_MAP_ITEM)
	def test_tags_suggestion(self):
		
		tags_option = self.e('#suggestion_field option:nth-of-type(4)')
		self.assertTrue(tags_option.is_selected())
		self.assertEqual('Tags', tags_option.text)
		
		tags_suggestion = self.e('#suggestion_keywords textarea')
		tags_suggestion.clear()
		
		tags_suggestion.send_keys('theater, Sofia')
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think these are the correct tags')
		self.e('.apply').click()
		
		sleep(4)
		
		tags_suggestion = ('.stories_list .suggestion.tags')
		self.assertEqual('Palace Hotel, Call Building, ruin, destruction,San Francisco Earthquake, 1906 San Francisco earthquake, sanfranciscoearthquake, 1906 earthquake, earthquake, earthquakes', tags_suggestion.e('.ba_from .value').text)
		self.assertEqual('theater, Sofia'						, tags_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think these are the correct tags'	, tags_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(tags_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('dialog/%d/tab:write-story/suggest:location/' % ID_MAP_ITEM)
	def test_location_suggestion(self):
		# TODO
		
		location_suggestion = self.e('#suggestion-location_cnt')
		location_suggestion.e('#location').send_keys('bulevard "Knyaginya Maria Luiza" 9-11, 1000 Sofia, Bulgaria')
		
		location_suggestion.e('#location_search').click()
		location_suggestion.e('#location_save').click()
		
		self.assertEqual('bulevard "Knyaginya Maria Luiza" 9-11, 1000 Sofia, Bulgaria', self.e('.suggestion-value-geo-tags').text)
		
		self.e('.apply').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.e('.write_story').send_keys('I think this is the correct location')
		self.e('.apply').click()
		
		sleep(4)
		
		location_suggestion = ('.stories_list .suggestion.location')
		self.assertEqual(self.e('#photo-side .photo-address').text	, location_suggestion.e('.ba_from .value').text)
		self.assertEqual('theater, Sofia'							, location_suggestion.e('.ba_to .value').text)
		self.assertEqual('I think this is the correct location'		, location_suggestion.e('.story_cnt').text)
		
		self.assertTrue(self.e('.suggestion-accept'), WebElement)
		self.assertTrue(self.e('.icon.delete'), WebElement)
		
		self.e('.icon.delete').click()
		
		alert = self.browser.switch_to_alert()
		alert.accept()
		
		self.assertFalse(location_suggestion, WebElement)
		
		# TODO refactor this when suggestions are on the map
		pass
	
	@url('/%d' % ID_MAP_ITEM)
	def test_streetview_suggestion(self):
		# TODO
		# open link /tab:suggestion-location/suggest:streetview/
		# drag and drop the image with SV
		# click Record position
		# assert SV suggestion
		# click publish
		# accept the allert
		# enter a description
		# check the suggestion section
		# delete the suggestion
		
		# TODO refactor this when suggestions are on the map
		pass
	
