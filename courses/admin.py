from django.contrib import admin

from .models import Course, CourseMajor, Enrollment, StudyMaterial, TeachingAssignment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "semester", "credits", "is_active")
    list_filter = ("semester", "is_active")
    search_fields = ("code", "title")


@admin.register(CourseMajor)
class CourseMajorAdmin(admin.ModelAdmin):
    list_display = ("course", "major", "is_core")
    list_filter = ("is_core", "major")
    search_fields = ("course__code", "major__code")


@admin.register(TeachingAssignment)
class TeachingAssignmentAdmin(admin.ModelAdmin):
    list_display = ("professor", "course", "is_primary", "assigned_at")
    list_filter = ("is_primary",)
    search_fields = ("professor__user__email", "course__code")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("student", "course", "semester", "status", "enrolled_at")
    list_filter = ("semester", "status")
    search_fields = ("student__user__email", "course__code")


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "uploaded_by", "material_type", "is_published")
    list_filter = ("material_type", "is_published")
    search_fields = ("title", "course__code", "uploaded_by__user__email")
