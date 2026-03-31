from django.contrib import admin

from .models import Assignment, StudyGroup, StudyGroupMember, Submission


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "course",
        "assignment_type",
        "submission_mode",
        "due_at",
        "is_published",
    )
    list_filter = ("assignment_type", "submission_mode", "is_published")
    search_fields = ("title", "course__code")


@admin.register(StudyGroup)
class StudyGroupAdmin(admin.ModelAdmin):
    list_display = ("name", "assignment", "leader", "created_at")
    search_fields = ("name", "assignment__title", "leader__user__email")


@admin.register(StudyGroupMember)
class StudyGroupMemberAdmin(admin.ModelAdmin):
    list_display = ("group", "student", "joined_at")
    search_fields = ("group__name", "student__user__email")


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("assignment", "student", "group", "status", "score", "submitted_at")
    list_filter = ("status",)
    search_fields = ("assignment__title", "student__user__email", "group__name")
