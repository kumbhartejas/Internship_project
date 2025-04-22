from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from .models import *


class menu(admin.ModelAdmin):
    list_display = ('name','image_prev','section')
    prepopulated_fields = {'slug': ('name',)}  
    def image_prev(self,obj):
        if obj.image :
            return format_html(   
                 '<img src="{0}" width="100" height="100" style="border-radius:10px;"/></a>',
                obj.image.url
            )
        return "No Image"
            
    image_prev.allow_tags=True  
    image_prev.short_description = "Preview" 

admin.site.register(item,menu)
admin.site.register(Section)
admin.site.register(scroll)

class item_no(admin.ModelAdmin):
    list_display = ( 'name', 'lastname','subject','submitted_at')

class book(admin.ModelAdmin):
    list_display = ( 'name', 'email','date','time','submitted_at')  

admin.site.register(m_form,item_no)
admin.site.register(Booking,book)