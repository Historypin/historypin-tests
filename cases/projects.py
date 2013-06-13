# -*- coding: utf-8 -*-

from base import *

class Projects(HPTestCase):
	
	@url('/projects/')
	def test_index(self):
		self.assertTitle('Historypin')  # HTML should be fixed to be Historypin | Projects
		
		paragraph = self.e('.home-top p')
		self.assertEqual(u'Explore our Historypin Projects and add your own memories. If you’d like to work with us to create a new Historypin Project, get in touch.'
			, paragraph.text)
		self.assertEqual(URL_BASE + '/contact', paragraph.e('a').get_attribute('href'))
		
		projects = [
			['11461010-hp-olympics'		, "Olympic memories"			, "Have you got photos and memories from the Olympics through the ages?"									, '11461010/type/banner_image'],
			['11462012-DiamondJubilee'	, "Pinning The Queen's history"	, "Have you celebrated a Royal Jubilee over the past 60 years or even seen a Royal visit?"					, '11462012/type/banner_image'],
			['11483012-balboa'			, "Balboa Park"					, "Celebrating the Centennial of the 1915-1916 Panama-California Exposition in San Diego, CA."				, '11483012/type/project_image'],
			['11499008-chevy'			, "Me and my Chevy"				, "Share your memories of your first cars, family holidays, road trips and more."							, '11499008/type/banner_image'],
			['11886013-grandparents'	, "Amazing Grandparents"		, "Is your Gran, Grandad, Nan or Pops awesome? Add your grandparents to our Hall of Fame."					, '11886013/type/banner_image'],
			['13388066-remember'		, "Remember how we used to..."	, "work, play, watch and listen, cook and clean, keep warm and celebrate. How did you used to do things?"	, '13388066/type/banner_image'],
			['13839007-yearofthebay'	, "Year of the Bay"				, "What events, big and small, have shaped the San Francisco Bay? Share your memories."						, '13839007/type/banner_image'],
			['15742010-sandy'			, "Hurricane Sandy"				, "Record, Remember, Rebuild: How have communities in the US and Caribbean been affected by Sandy?"			, '15742010/type/project_image'],
			['16690005-1989'			, "Europeana 1989"				, "Share your stories, photographs and videos about the Fall of the Iron Curtain."							, '16690005/type/project_image'],
			['23580013-japan-project'	, u"Historypin 日本上陸！"		, u"日本での展開について詳しく知る"																				, '23580013/type/project_image'],
		]
		
		
		links			= self.es('.col .inn h2 > a')
		headings		= self.es('.col .inn h2')
		paragraphs		= self.es('.col .inn p')
		images			= self.es('.col .inn img')
		banner_links	= self.es('.col .inn .banner-holder')
		
		url				= URL_BASE + '/project/'
		
		for n in range(len(projects)):
			i = projects[n]
			self.assertEqual(url + i[0]													, links[n].get_attribute('href'))
			self.assertEqual(url + i[0] + '/'											, banner_links[n].get_attribute('href'))
			self.assertEqual(i[1]														, headings[n].text)
			self.assertEqual(i[2]														, paragraphs[n].text)
			self.assertEqual(URL_BASE + '/projects/img/' + i[3]	+ '/dim/292x230/crop/1/', images[n].get_attribute('src'))
