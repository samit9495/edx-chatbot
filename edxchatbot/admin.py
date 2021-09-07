from django.contrib import admin

from .models import *

class CourseChatbotAdmin(admin.ModelAdmin):
    list_display = ['chatbot_name', 'course_id', 'chatbot_url']

admin.site.register(CourseChatbot, CourseChatbotAdmin)
