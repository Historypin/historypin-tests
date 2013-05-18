# -*- coding: utf-8 -*-

from base import *

class Channel(HPTestCase):
	
	@url('/channels/view/10649049/')
	def test_channel_info(self):
		# TODO
		# assert title
		# assert Gabss text
		# assert channel logo
		# assert text and links in photo info
		pass
	
	@url('/channels/view/10649049/')
	def test_channel_details(self):
		# TODO
		# assert channel details text
		# assert channel views text
		# assert fans, pins, tours and collections text
		# assert become a fan button text and link
		# assert share text
		# assert icons and links
		pass
	
	@url('/channels/view/10649049/')
	def test_map_tab(self):
		# TODO
		# assert Map text and link
		# click on map tab
		# assert for embed frame that the link is /attach/uid10649049/map/#!/geo:42.697839,23.32167/zoom:20/
		# assert input field Search by location
		# assert input field Search by tag
		# assert Go button link and text
		# assert years slider
		# 
		pass
	
	@url('/channels/view/10649049/')
	def test_list_tab(self):
		# TODO
		# click on List Tab
		# assert list text 
		# assert list filter radio buttons and texts
		# assert img link and text
		# assert img icons - info actions
		# assert info
		# assert h5s
		# assert paragraphs
		pass
	
	@url('/channels/view/10649049/')
	def test_collections_tab(self):
		# TODO
		# click on Collections Tab
		# assert collections text
		# assert collection img
		# assert collection link
		# assert icon
		# assert text
		# assert collection link
		# assert channel link
		pass
	
	@url('/channels/view/10649049/')
	def test_tours_tab(self):
		# TODO
		# click on Tours Tab
		# assert tours text
		# assert image src
		# assert image link
		# assert tour icon
		# assert text
		# assert tour link 
		# assert channel link
		pass
	
	@url('/channels/view/10649049/')
	def test_comment_feed(self):
		# TODO
		# assert Comment Feed text
		# assert paragraph text
		# asser img src
		# assert img link 
		# assert channel img
		# assert assert chanenel text
		# assert text in the comment
		pass
	