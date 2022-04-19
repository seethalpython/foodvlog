from.models import *
from django.contrib import admin

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields= {'slug':('name',)}
admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','image','available']
    list_editable = ['price','stock','image','available']
    prepopulated_fields= {'slug':('name',)}
admin.site.register(products,prodadmin)

