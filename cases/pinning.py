# -*- coding: utf-8 -*-

from base import *

class Pinning(HPTestCase):
	
	@logged_in
	@url('/upload/')
	def test_add_stuff_page(self):
		
		steps = ['Choose stuff to add', 'Add Something', 'Pin it to the map', 'All done']
		
		texts = self.es('.progress-bar li')
		
		for n in range(len(steps)): self.assertEqual(steps[n], texts[n].text)
		
		cnt_upload = self.e('.upload-content')
		self.assertEqual('I want to add', cnt_upload.e('h2').text)
		
		photo_type = self.e('.upload-type li .photos')
		self.assertEqual('Photos', photo_type.text)
		self.assertEqual('%s/upload-item/index/' % URL_BASE, photo_type.get_attribute('href'))
		self.assertIn('ss-icon'		, photo_type.e('span').get_attribute('class'))
		self.assertIn('ss-picture'	, photo_type.e('span').get_attribute('class'))
		
		video_type = self.e('.upload-type li .videos')
		self.assertEqual('Video', video_type.text)
		self.assertEqual('%s/upload-video/index/' % URL_BASE, video_type.get_attribute('href'))
		self.assertIn('ss-icon'		, video_type.e('span').get_attribute('class'))
		self.assertIn('ss-video'	, video_type.e('span').get_attribute('class'))
		
		audio_type = self.e('.upload-type li .audio')
		self.assertEqual('Audio', audio_type.text)
		self.assertEqual('%s/upload-audio/index/' % URL_BASE, audio_type.get_attribute('href'))
		self.assertIn('ss-icon'			, audio_type.e('span').get_attribute('class'))
		self.assertIn('ss-headphones'	, audio_type.e('span').get_attribute('class'))
		
		self.assertEqual('Want to upload large amounts of content? Read about our Bulk Uploader', self.e('.bottom-p').text)
		self.assertEqual('%s/bulkbridge/' % URL_BASE, self.e('.bottom-p a').get_attribute('href'))
	
	@logged_in
	@url('/upload-item/index/')
	def test_upload_photo_page(self):
		
		cnt_upload = self.e('.upload-content')
		self.assertEqual('Upload a photo', cnt_upload.e('h2').text)
		self.assertIsInstance(self.e('.fileinput-button'), WebElement)
		self.assertIsInstance(self.e('.delete.ui-button'), WebElement)
		
		cnt = self.e('.dropzone-container')
		self.assertEqual('Drag your images here to add them. They will upload automatically.', cnt.e('h3').text)
		self.assertEqual('Pssst. JPG and PNG files up to 5 megabytes only please.', cnt.e('h5').text)
		
		self.assertEqual('Are you an archive and want to upload large amounts of content? Try our Bulk Uploader for Firefox and Chrome.', self.e('.bottom-p').text)
		self.assertEqual('%s/bulkbridge/' % URL_BASE, self.e('.bottom-p a').get_attribute('href'))
