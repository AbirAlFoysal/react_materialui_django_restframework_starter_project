from django.contrib import admin
from .models import Crud

# Register your models here.

class CrudAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Crud, CrudAdmin)