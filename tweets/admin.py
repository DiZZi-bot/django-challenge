from django.contrib import admin
from .models import Tweet, Like

class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payload', 'like_count', 'created_at')

admin.site.register(Tweet, TweetAdmin)
admin.site.register(Like)
