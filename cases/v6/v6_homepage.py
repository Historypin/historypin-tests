# -*- coding: utf-8 -*-

from base import *
import os, sys

class Homepage_V6(HPTestCase):
	
	@url('/en/explore/')
	def test_header(self):
		
		self.assertTitle('Historypin')
		
		header	= self.e('#header')
		links	= header.es('li a')
		
		header_items = [
			['Home'					, URL_BASE + '/'],
			['Map'					, URL_BASE + '/map/'],
			['Projects'				, URL_BASE + '/projects/'],
			['Channels'				, URL_BASE + '/channels/'],
			['Tours and Collections', URL_BASE + '/curated/'],
			['Get Involved'			, URL_BASE + '/community/'],
			['Blog'					, 'http://blog.historypin.com/'],
			['Login'				, URL_BASE + '/user/'],
			['Join'					, URL_BASE + '/user/'],
			['Pin'					, URL_BASE + '/upload/'],
		]
		
		for n in range(len(header_items)):
			i = header_items[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
	
	@url('/en/explore/')
	def test_index(self):
		
		self.assertTitle('Historypin')
		
		header	= self.e('#header')
		self.assertEqual('%s/' % URL_BASE, header.e('h1 a').get_attribute('href'))
		
		self.assertEqual('Historypin', self.e('h3').text)
		self.assertIsInstance(self.e('.home-anchor'), WebElement)
		
		timeline = self.e('#timeline')
		self.assertEqual('1800', timeline.e('.start').text)
		self.assertEqual('1800', timeline.e('.ui-slider-handle-left').text)
		
		
		self.assertEqual('2029', timeline.e('.end').text)
		self.assertEqual('2029', timeline.e('.ui-slider-handle-right').text)
		
		self.assertIsInstance(timeline.e('.ui-slider-range'), WebElement)
		
		self.assertIsInstance(self.e('#map'), WebElement)
	
	@url('/en/explore/geo/46.850422,17.791903,11')
	def test_map(self):
		# click on the pin on the map
		# assert title views and link to the channel
		# assert image
		# assert description and infor
		# assert the tooltip on the map
		# assert year slider
		# close the sidebar
		# assert that it's close
		sleep(5)
		self.e('#map .gm-style div').click()
		
		sleep(10)
		
	@url('/en/explore/pin/160345')
	def test_pin(self):
		
		sleep(6)
		self.assertEqual('1989', self.e('#timeline .tooltip').text)
		column_header = self.e('#pin .row')
		
		self.assertEqual('Outside a tavern at Lake Balaton', self.e('#explore h1').text)
		self.assertEqual('http://www.historypin.com/channels/img/46399/logo/1/dim/50x50/crop/1/', column_header.e('.author-image img').get_attribute('src'))
		self.assertEqual('Pinned by\nDeutsche Kinemathek'	, column_header.e('.author').text)
		self.assertEqual('%s/channels/view/46399' % URL_BASE, column_header.e('.author a').get_attribute('href'))
		
		sleep(3)
		# self.assertEqual('Balaton Uplands National Park, 8237 Tihany, Kossuth Lajos Street 31, Hungary', self.e('.tooltip.arrow-down').text)  # TODO fix this, because the map is slow and cannot load the tooltip on time
		
		share_toolbox = self.e('.addthis_toolbox')
		self.hover(share_toolbox)
		share_items = share_toolbox.es('li')
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		
		column_3b = self.e('.content')
		self.assertEqual('http://www.historypin.com/services/thumb/phid/160345/dim/600x600/quality/80/', column_3b.e('img').get_attribute('src'))
		
		self.assertIsInstance(column_3b.e('.info-anchor'), WebElement)
		
		h4s = ['DESCRIPTION', 'TAGS', 'INFORMATION', 'CREATOR']
		h4s_cnt = column_3b.es('h4')
		for n in range(len(h4s)): self.assertEqual(h4s[n], h4s_cnt[n].text)
		
		column_header.e('.close-anchor').click()
		self.assertFalse(column_header.is_displayed())
		self.assertFalse(column_3b.is_displayed())
	
	@logged_in
	@url('/en/explore/oreo/pin/223343/geo/43.24369,23.956892,6')
	def test_text_pin(self):
		
		self.assertEqual('Test Project for QA', self.e('h3').text)
		self.assertEqual('5 May 2012', self.e('.tooltip.arrow-up').text)
		
		self.assertEqual('ulitsa "Okolovrasten pat", 1756 Sofia, Bulgaria', self.e('.tooltip.arrow-down').text)
		
		column_row = self.e('.c3b')
		
		sleep(10)
		self.assertEqual('Title Text Pin1', column_row.e('h1').text)
		self.assertEqual('http://www.historypin.com/channels/img/49127/logo/1/dim/50x50/crop/1/', column_row.e('.author-image img').get_attribute('src'))
		self.assertEqual('Rawr', column_row.e('.author a').text)
		self.assertEqual('%s/channels/view/49127' % URL_BASE, column_row.e('.author a').get_attribute('href'))
		
		self.assertIn(u'Lorem Ipsum е елементарен примерен текст, използван в печатарската и типографската индустрия.', self.e('.text-pin').text)
		
		share_toolbox = self.e('.addthis_toolbox')
		self.hover(share_toolbox)
		social_cnt = self.e('.social-container')
		share_items = social_cnt.es('li')
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		
		self.e('.info-anchor.ss-icon.ss-info').click()
		
		# info_pin = self.e('.description')
		
		# h4s = ['DESCRIPTION', 'TAGS', 'INFORMATION', 'CREATOR'] TODO FIX THIS
		# h4s_cnt = info_pin.es('h4')
		# for n in range(len(h4s)): self.assertEqual(h4s[n], h4s_cnt[n].text)
		
		self.assertEqual("License: Copyright (c) all rights reserved\nAttribution:\nOriginal link:\nRepository:\nNotes:", self.e('.information').text)
	
	@url('/en/explore/1989')
	def test_project(self):
		
		self.assertTitle('Historypin')
		
		banner = self.e('#banner')
		self.assertEqual('Europeana 1989', banner.e('h3').text)
		
		timeline = self.e('#timeline')
		self.assertEqual('1930', timeline.e('.start').text)
		self.assertEqual('1930', timeline.e('.ui-slider-handle-left').text)
		
		self.assertEqual('2013', timeline.e('.end').text)
		self.assertEqual('2013', timeline.e('.ui-slider-handle-right').text)
		self.assertIsInstance(timeline.e('.ui-slider-range'), WebElement)
		
		if not self.e('.panel.expanded').is_displayed():
			banner.e('.home-anchor').click()
		
		sleep(4)
		self.assertEqual(URL_BASE + '/projects/img/pid/34/type/project_image,banner,logo/dim/1024x290/crop/1/', banner.e('img').get_attribute('src'))
		
		self.assertEqual('Mirrorpix Archives', banner.e('.channel-link span').text)
		self.assertEqual('Europeana 1989: We Made History', banner.e('.description strong').text)
		self.assertIn(u'The way history is recorded isn’t just about what museums and institutions think is important', banner.e('.description').text)
		
		share_toolbox	= self.e('.social-container')
		share_items		= share_toolbox.es('li')
		
		self.hover(share_toolbox)
		self.assertIsInstance(share_items[0], WebElement)
		self.assertIsInstance(share_items[1], WebElement)
		self.assertIsInstance(share_items[2], WebElement)
		self.assertIsInstance(share_items[3], WebElement)
		self.assertIsInstance(share_items[4], WebElement)
		
		self.assertEqual('Explore the map', self.e('#btn-explore').text)
		self.e('#btn-explore').click()
		
		self.browser.set_window_size(1680, 900)
		sleep(5)
		
		banner.e('.home-anchor').click()
		self.assertEqual('Read more...', self.e('.read-more').text)
		self.e('.read-more').click()
		
		self.assertIn(u'The way history is recorded isn’t just about what museums and institutions think is important', banner.e('.description').text)
	
	@url('/en/explore/')
	def test_footer(self):
		
		self.assertTitle('Historypin')
		
		footer	= self.e('#footer')
		links	= footer.es('li a')
		
		footer_items = [
			['Terms and Conditions'	, URL_BASE + '/terms-and-conditions/'],
			['Privacy Policy'		, URL_BASE + '/privacy-policy/'],
			['Cookies'				, URL_BASE + '/cookies/'],
			['Facebook'				, 'http://www.facebook.com/pages/Historypin/192291707448024/'],
			['Twitter'				, 'http://twitter.com/Historypin/'],
			['Google +'				, 'https://plus.google.com/116628462065893538180/posts/'],
			['Blog'					, 'http://blog.historypin.com/'],
			[u'© We Are What We Do'	, 'http://wearewhatwedo.org/'],
		]
		
		for n in range(len(footer_items)):
			i = footer_items[n]
			self.assertEqual(i[0], links[n].text)
			self.assertEqual(i[1], links[n].get_attribute('href'))
	
