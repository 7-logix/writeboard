from textshare.models import Note
from django.contrib import admin

class NoteAdmin(admin.ModelAdmin):
	fields = ['text', 'key', 'pass_key', 'create_date']
	list_display = ('key', 'pass_key', 'create_date')
	list_filter = ['create_date']
	date_hierarchy = 'create_date'

admin.site.register(Note,NoteAdmin)