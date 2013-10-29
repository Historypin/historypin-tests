# -*- coding: utf-8 -*-

from base import *

class Projects(HPTestCase):
	@url('/projects/')
	def test_index(self):
		self.assertTitle('Historypin | Projects')
		
		paragraph = self.e('.home-top p')
		self.assertEqual(u'Explore our Historypin Projects and add your own memories. If you’d like to work with us to create a new Historypin Project, get in touch.', paragraph.text)
		self.assertEqual(URL_BASE + '/contact', paragraph.e('a').get_attribute('href'))
		
		projects = [
			['%d-hp-olympics' % ID_PROJECTS[0], "Olympic memories"					, "Have you got photos and memories from the Olympics through the ages?"									, '%d' % ID_PROJECTS_IMAGES[0]],
			['%d-DiamondJubilee' % ID_PROJECTS[1], "Pinning The Queen's history"	, "Have you celebrated a Royal Jubilee over the past 60 years or even seen a Royal visit?"					, '%d' % ID_PROJECTS_IMAGES[1]],
			['%d-balboa'		% ID_PROJECTS[2], "Balboa Park"						, "Celebrating the Centennial of the 1915-1916 Panama-California Exposition in San Diego, CA."				, '%d' % ID_PROJECTS_IMAGES[2]],
			['%d-chevy'			% ID_PROJECTS[3], "Me and My Chevy"					, "Share your memories of your first cars, family holidays, road trips and more."							, '%d' % ID_PROJECTS_IMAGES[3]],
			['%d-grandparents'	% ID_PROJECTS[4], "Amazing Grandparents"			, "Is your Gran, Grandad, Nan or Pops awesome? Add your grandparents to our Hall of Fame."					, '%d' % ID_PROJECTS_IMAGES[4]],
			['%d-remember'		% ID_PROJECTS[5], "Remember how we used to..."		, "work, play, watch and listen, cook and clean, keep warm and celebrate. How did you used to do things?"	, '%d' % ID_PROJECTS_IMAGES[5]],
			['%d-yearofthebay'	% ID_PROJECTS[6], "Year of the Bay"					, "What events, big and small, have shaped the San Francisco Bay? Share your memories."						, '%d' % ID_PROJECTS_IMAGES[6]],
			['%d-sandy'			% ID_PROJECTS[7], "Hurricane Sandy"					, "Record, Remember, Rebuild: How have communities in the US and Caribbean been affected by Sandy?"			, '%d' % ID_PROJECTS_IMAGES[7]],
			['%d-1989'			% ID_PROJECTS[8], "Europeana 1989"					, "Share your stories, photographs and videos about the Fall of the Iron Curtain."							, '%d' % ID_PROJECTS_IMAGES[8]],
			['%d-japan-project'	% ID_PROJECTS[9], u"Historypin 日本上陸！"			, u"日本での展開について詳しく知る"																				, '%d' % ID_PROJECTS_IMAGES[9]],
			['%d-putting-art-on-the-map' % ID_PROJECTS[10], 'Putting Art on the Map', 'Explore, curate and enrich the Imperial War Museums\' First World War artworks.'							, '%d' % ID_PROJECTS_IMAGES[10]],
			['%d-all-our-stories' % ID_PROJECTS[11], 'All Our Stories'				, 'Explore an archive of community projects funded by the Heritage Lottery Fund.'							, '%d' % ID_PROJECTS_IMAGES[11]],
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
			self.assertEqual(URL_BASE + '/projects/img/pid/' + i[3]	+ '/type/project_image,banner,logo/dim/292x230/crop/1/', images[n].get_attribute('src'))
