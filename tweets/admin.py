from django.contrib import admin
from .models import Tweet, Like
from django.utils.translation import gettext_lazy as _

class ElonMuskFilter(admin.SimpleListFilter):
    title = _('Elon Musk Filter')
    parameter_name = 'elon_musk'

    def lookups(self, request, model_admin):
        return [
            ('contains', _('Contains "Elon Musk"')),
            ('not_contains', _('Does not contain "Elon Musk"')),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'contains':
            return queryset.filter(payload__icontains='Elon Musk')
        elif self.value() == 'not_contains':
            return queryset.exclude(payload__icontains='Elon Musk')
        return queryset

class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'tweet', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('created_at',)

class TweetAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payload', 'created_at')
    search_fields = ('payload', 'user__username')
    list_filter = ('created_at', ElonMuskFilter)

admin.site.register(Like, LikeAdmin)
admin.site.register(Tweet, TweetAdmin)
