from django.contrib import admin

from .models import Major, Semester


@admin.action(description="Mark selected majors as available")
def mark_majors_active(modeladmin, request, queryset):
    queryset.update(is_active=True)


@admin.action(description="Mark selected majors as unavailable")
def mark_majors_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active")
    list_filter = ("is_active",)
    search_fields = ("code", "name")
    list_editable = ("is_active",)
    actions = (mark_majors_active, mark_majors_inactive)


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("name", "term", "year", "start_date", "end_date", "is_active")
    list_filter = ("term", "year", "is_active")
    search_fields = ("name",)
