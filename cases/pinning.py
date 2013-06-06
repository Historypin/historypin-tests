# -*- coding: utf-8 -*-

from base import *

class Pinning(HPTestCase):
	
	@url('/upload/')
	def test_add_stuff_page(self):
		
		steps = ['Choose stuff to add', 'Add something', 'Pin it to the map', 'All done']
		
		texts = self.es('.progress-bar li')
		
		for n in range(len(steps)): self.assertEqual(steps[n], texts[n].text)
		
		cnt_upload = self.e('.upload-content')
		self.assertEqual('I want to add', cnt_upload.e('h2').text)
		
		photo_type = self.e('.upload-type li .photos')
		self.assertEqual('Photos', photo_type.text)
		self.assertEqual(URL_BASE + '/upload-item/index/', photo_type.get_attribute('href'))
		self.assertIn('ss-icon'		, photo_type.e('span').get_attribute('class'))
		self.assertIn('ss-picture'	, photo_type.e('span').get_attribute('class'))
		
		video_type = self.e('.upload-type li .videos')
		self.assertEqual('Video', video_type.text)
		self.assertEqual(URL_BASE + '/upload-video/index/', video_type.get_attribute('href'))
		self.assertIn('ss-icon'		, video_type.e('span').get_attribute('class'))
		self.assertIn('ss-video'	, video_type.e('span').get_attribute('class'))
		
		audio_type = self.e('.upload-type li .audio')
		self.assertEqual('Audio', audio_type.text)
		self.assertEqual(URL_BASE + '/upload-audio/index/', audio_type.get_attribute('href'))
		self.assertIn('ss-icon'			, audio_type.e('span').get_attribute('class'))
		self.assertIn('ss-headphones'	, audio_type.e('span').get_attribute('class'))
		
		self.assertEqual('Want to upload large amounts of content? Read about our Bulk Uploader', self.e('.bottom-p').text)
		self.assertEqual(URL_BASE + '/bulkbridge/', self.e('.bottom-p a').get_attribute('href'))
	
	@url('/')
	def test_index(self):
		pass
