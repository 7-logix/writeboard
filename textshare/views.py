from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from textshare.models import Note
from datetime import datetime
from random import shuffle

def index(request):
	notes = Note.objects.all().order_by('-create_date')[:10]
	return render_to_response('textshare/index.html', {'notes': notes}, context_instance=RequestContext(request))

#index page with error report
def index_error(request,err_id):
	notes = Note.objects.all().order_by('-create_date')[:10]
	return render_to_response('textshare/index.html', {'error': err_id, 'notes': notes}, context_instance=RequestContext(request))
	
#show a note in read-only mode
def show_note(request,note_key):
	note = Note.objects.filter(key = note_key)
	
	if note.count() > 0: #note found
		return render_to_response('textshare/read_note.html', {'note': note[0]})
	else: #note doesn't exist
		return index_error(request,1)
		
#show a note in read-write mode
def edit_note(request,note_key,note_pass):
	note = Note.objects.filter(key = note_key)
	
	if note.count() > 0: #note found
		if note_pass == note[0].pass_key: #key match
			return render_to_response('textshare/write_note.html', {'note': note[0]},context_instance=RequestContext(request))
		else: #invalid key
			return index_error(request,2)
	else: #note doesn't exist
		return index_error(request,1)

#create a note
def save_note(request):
	if request.POST['note_text'] == "": #note is empty
		notes = Note.objects.all().order_by('-create_date')[:10]
		return HttpResponseRedirect(reverse('textshare.views.index'))
		
	#generate random key
	arr = map(chr, range(97, 123))
	shuffle(arr)
	secret = ''.join(arr[0:11])
	
	#create note
	n = Note(text = request.POST['note_text'], create_date = datetime.now(), key = len(Note.objects.all()), pass_key = secret)
	n.save()
	
	return HttpResponseRedirect(reverse('textshare.views.edit_note', args = (n.key,n.pass_key)))

#update an already existing note
def update_note(request,note_key,note_pass):
	if Note.objects.filter(key = note_key) > 0: #note found
		note = Note.objects.get(key = note_key)
		
		if note.pass_key == note_pass: #key match
			note.text = request.POST['note_text']
			note.save()
			return HttpResponseRedirect(reverse('textshare.views.edit_note', args = (note.key,note.pass_key)))
		else: #invalid key
			return index_error(request,2)
	else: #note doesn't exist
		return index_error(request,1)