from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from textshare.models import Note
from datetime import datetime

def index(request):
	return render_to_response('textshare/index.html',context_instance=RequestContext(request))
    
def show_note(request,note_key):
	note = Note.objects.get(key = note_key)
	return render_to_response('textshare/read_note.html', {'note': note})
	
def edit_note(request,note_key,note_pass):
	if note_key == note_pass:
		note = Note.objects.get(key = note_key)
		return render_to_response('textshare/write_note.html', {'note': note},context_instance=RequestContext(request))
	else:
		return render_to_response('textshare/index.html',context_instance=RequestContext(request))
	
def save_note(request):
	n = Note(text = request.POST['note_text'], create_date = datetime.now(), key = len(Note.objects.all()))
	n.save()
	return HttpResponseRedirect(reverse('textshare.views.show_note', args = (n.key,)))
	
def update_note(request,note_key):
	n = Note.objects.get(key = note_key)
	n.text = request.POST['note_text']
	n.save()
	return HttpResponseRedirect(reverse('textshare.views.show_note', args = (n.key,)))