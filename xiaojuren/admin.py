from django.contrib import admin

from .models import book,Image,link,link2,link3,link6,link7,index

class bookInfoAdmin(admin.ModelAdmin):
	list_dispaly = ("title","date")

class ImageInfoAdmin(admin.ModelAdmin):
	list_dispaly = ("id","name")

class linkInfoAdmin(admin.ModelAdmin):
	list_dispaly = ("id","title")

class link2InfoAdmin(admin.ModelAdmin):
	list_dispaly = ("tail","content","img")

class link3InfoAdmin(admin.ModelAdmin):
	list_display = ("head","content")

class link6InfoAdmin(admin.ModelAdmin):
	list_display = ("img",)

class link7InfoAdmin(admin.ModelAdmin):
	list_display = ("name",)

class indexInfoAdmin(admin.ModelAdmin):
	list_display = ("img",)

admin.site.register(book,bookInfoAdmin)
admin.site.register(Image,ImageInfoAdmin)
admin.site.register(link,linkInfoAdmin)
admin.site.register(link2,link2InfoAdmin)
admin.site.register(link3,link3InfoAdmin)
admin.site.register(link6,link6InfoAdmin)
admin.site.register(link7,link7InfoAdmin)
admin.site.register(index,indexInfoAdmin)
