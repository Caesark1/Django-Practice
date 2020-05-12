from django.contrib import admin
from .models import *

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email","date",)