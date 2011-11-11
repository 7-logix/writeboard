from django.test import TestCase
from django.test.client import Client
from textshare.models import Note
from datetime import datetime

class NoteTests(TestCase):
	def test_submit_note(self):
		c = Client()
		response = c.post('/save/', {'note_text': "first test note"})
		
		self.assertEqual(response.status_code, 302)#check for 302 found
		
	def test_show_note(self):
		note_text = "second test note"
		Note(text = note_text, create_date = datetime.now(), key = len(Note.objects.all())).save()
		
		c = Client()
		response = c.get('/' + str(len(Note.objects.all()) - 1) + '/')
		
		self.assertEqual(response.status_code, 200)#check for 200 OK
		self.assertEqual(response.context['note'].text, note_text)#check for the returned text
