from django.contrib import admin

from .models import Major, Semester


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("code", "name")


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("name", "term", "year", "start_date", "end_date", "is_active")
    list_filter = ("term", "year", "is_active")
    search_fields = ("name",)
