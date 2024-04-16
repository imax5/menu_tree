from django.contrib import admin

from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'order', 'parent', 'name' ,'url')
    list_display_links = ('pk', 'order', 'parent', 'name' ,'url')
    search_fields = ('order', 'parent', 'name', 'url')

admin.site.register(Menu, MenuAdmin)