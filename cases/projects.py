# -*- coding: utf-8 -*-

from base import *

class Projects(HPTestCase):
	@url('/projects/')
	def test_index(self):
		self.assertTitle('Historypin | Projects')
		
		paragraph = self.e('.home-top p')
		self.assertEqual(u'Explore our Historypin Projects and add your own memories. If you’d like to work with us to create a new Historypin Project, get in touch.', paragraph.text)
		self.assertEqual('{0}/contact'.format(URL_BASE), paragraph.e('a').get_attribute('href'))
		
		projects = [
			['{0}-hp-olympics'		.format(ID_PROJECTS[0]), "Olympic memories"					, "Have you got photos and memories from the Olympics through the ages?"									, '{0}'.format(ID_PROJECTS_IMAGES[0])],
			['{0}-DiamondJubilee'	.format(ID_PROJECTS[1]), "Pinning The Queen's history"		, "Have you celebrated a Royal Jubilee over the past 60 years or even seen a Royal visit?"					, '{0}'.format(ID_PROJECTS_IMAGES[1])],
			['{0}-balboa'			.format(ID_PROJECTS[2]), "Balboa Park"						, "Celebrating the Centennial of the 1915-1916 Panama-California Exposition in San Diego, CA."				, '{0}'.format(ID_PROJECTS_IMAGES[2])],
			['{0}-chevy'			.format(ID_PROJECTS[3]), "Me and My Chevy"					, "Share your memories of your first cars, family holidays, road trips and more."							, '{0}'.format(ID_PROJECTS_IMAGES[3])],
			['{0}-grandparents'		.format(ID_PROJECTS[4]), "Amazing Grandparents"				, "Is your Gran, Grandad, Nan or Pops awesome? Add your grandparents to our Hall of Fame."					, '{0}'.format(ID_PROJECTS_IMAGES[4])],
			['{0}-remember'			.format(ID_PROJECTS[5]), "Remember how we used to..."		, "work, play, watch and listen, cook and clean, keep warm and celebrate. How did you used to do things?"	, '{0}'.format(ID_PROJECTS_IMAGES[5])],
			['{0}-yearofthebay'		.format(ID_PROJECTS[6]), "Year of the Bay"					, "What events, big and small, have shaped the San Francisco Bay? Share your memories."						, '{0}'.format(ID_PROJECTS_IMAGES[6])],
			['{0}-sandy'			.format(ID_PROJECTS[7]), "Hurricane Sandy"					, "Record, Remember, Rebuild: How have communities in the US and Caribbean been affected by Sandy?"			, '{0}'.format(ID_PROJECTS_IMAGES[7])],
			['{0}-1989'				.format(ID_PROJECTS[8]), "Europeana 1989"					, "Share your stories, photographs and videos about the Fall of the Iron Curtain."							, '{0}'.format(ID_PROJECTS_IMAGES[8])],
			['{0}-japan-project'	.format(ID_PROJECTS[9]), u"Historypin 日本上陸！"				, u"日本での展開について詳しく知る"																				, '{0}'.format(ID_PROJECTS_IMAGES[9])],
			['{0}-queens'			.format(ID_PROJECTS[10]), 'Queens: Neighborhood Stories'	, 'Share the photos, videos, audio clips and stories that tell the history of your neighborhood.'			, '{0}'.format(ID_PROJECTS_IMAGES[10])],
			['{0}-putting-art-on-the-map'	.format(ID_PROJECTS[11]), 'Putting Art on the Map'	, 'Explore, curate and enrich the Imperial War Museums\' First World War artworks.'							, '{0}'.format(ID_PROJECTS_IMAGES[11])],
			['{0}-railroads'				.format(ID_PROJECTS[12]), 'Living With The Railroads', 'Help build a shared collection of life along the railroads.'											, '{0}'.format(ID_PROJECTS_IMAGES[12])],
			['{0}-sourdough-and-rye'		.format(ID_PROJECTS[13]), 'Sourdough and Rye'		, 'A place to share Bay Area Jewish history'																, '{0}'.format(ID_PROJECTS_IMAGES[13])],
			['{0}-all-our-stories'			.format(ID_PROJECTS[14]), 'All Our Stories'			, 'Explore an archive of community projects funded by the Heritage Lottery Fund.'							, '{0}'.format(ID_PROJECTS_IMAGES[14])],
			['{0}-yarra'					.format(ID_PROJECTS[15]), 'Yarra Ranges: Changing Places', "Celebrate the history of Yarra Ranges' high streets by sharing your photos and memories."			, '{0}'.format(ID_PROJECTS_IMAGES[15])],
			['{0}-east-at-main-street'		.format(ID_PROJECTS[16]), 'East at Main Street'		, u"Asian & Pacific Islander Americans mapping their history."												, '{0}'.format(ID_PROJECTS_IMAGES[16])],
		]
		
		
		links			= self.es('.col .inn h2 > a')
		headings		= self.es('.col .inn h2')
		paragraphs		= self.es('.col .inn p')
		images			= self.es('.col .inn img')
		banner_links	= self.es('.col .inn .banner-holder')
		
		url				= '{0}/project/'.format(URL_BASE)
		
		for n in range(len(projects)):
			i = projects[n]
			self.assertEqual('{0}{1}/'.format(url, i[0]), links[n].get_attribute('href'))
			self.assertEqual('{0}{1}/'.format(url, i[0]), banner_links[n].get_attribute('href'))
			self.assertEqual(i[1]				, headings[n].text)
			self.assertEqual(i[2]				, paragraphs[n].text)
			self.assertEqual('{0}/projects/img/pid/{1}/type/project_image,banner,logo/dim/292x230/crop/1/'.format(URL_BASE, i[3]), images[n].get_attribute('src'))
