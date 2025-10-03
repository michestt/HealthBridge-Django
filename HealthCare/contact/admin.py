from django.contrib import admin
from .models import Contact, message_subject_1, message_subject_2

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display=("user_name", "message_subject2", "user_email", "user_message")


class MessageSubjectAdmin(admin.ModelAdmin):
	list_display = ('category', 'title')
	ordering = ('category',)


admin.site.register(Contact,  ContactAdmin)
admin.site.register(message_subject_1)
admin.site.register(message_subject_2, MessageSubjectAdmin)

