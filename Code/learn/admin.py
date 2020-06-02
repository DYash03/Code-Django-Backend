from django.contrib import admin
from . models import Contact, Editor, Technologies
# Register your models here.
admin.site.register(Technologies)
admin.site.register(Contact)
admin.site.register(Editor)
