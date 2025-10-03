from django.contrib import admin
from fitforum import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('nickname','message','enabled','pub_time')

admin.site.register(models.Level),
admin.site.register(models.Post, PostAdmin)
