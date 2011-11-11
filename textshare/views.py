from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from textshare.models import Note
from datetime import datetime

def index(request):
	return render_to_response('textshare/index.html')
    
def show_note(request,note_key):
	note = get_object_or_404(Note, key = note_key)
	return render_to_response('textshare/note.html', {'note': note})
	
def save_note(request):
	n = Note(text = request.POST['note_text'], create_date = datetime.now(), note_key = len(Note.objects.all))
	n.save()
	return HttpResponseRedirect(reverse('textshare.views.show_note', args = (n.key)))