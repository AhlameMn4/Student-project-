from django.contrib import admin

from .models import Announcement, CalendarEvent


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "posted_by", "scope", "is_published", "created_at")
    list_filter = ("scope", "is_published")
    search_fields = ("title", "content", "posted_by__email")


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_type", "scope", "start_at", "end_at", "created_by")
    list_filter = ("event_type", "scope")
    search_fields = ("title", "created_by__email")
