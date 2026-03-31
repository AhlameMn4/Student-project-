import uuid

from django.core.exceptions import ValidationError
from django.db import models


class AudienceScope(models.TextChoices):
    GLOBAL = "global", "Global"
    MAJOR = "major", "Major"
    COURSE = "course", "Course"


class EventType(models.TextChoices):
    EXAM = "exam", "Exam"
    DEADLINE = "deadline", "Deadline"
    HOLIDAY = "holiday", "Holiday"
    MEETING = "meeting", "Meeting"
    OTHER = "other", "Other"


class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    posted_by = models.ForeignKey(
        "accounts.User", on_delete=models.PROTECT, related_name="announcements"
    )
    title = models.CharField(max_length=180)
    content = models.TextField()
    scope = models.CharField(max_length=20, choices=AudienceScope.choices)
    major = models.ForeignKey(
        "academics.Major",
        on_delete=models.CASCADE,
        related_name="announcements",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="announcements",
        null=True,
        blank=True,
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.scope == AudienceScope.GLOBAL and (self.major_id or self.course_id):
            raise ValidationError("Global announcement cannot target a major or course.")
        if self.scope == AudienceScope.MAJOR and not self.major_id:
            raise ValidationError("Major-scoped announcement must target a major.")
        if self.scope == AudienceScope.COURSE and not self.course_id:
            raise ValidationError("Course-scoped announcement must target a course.")

    def __str__(self):
        return self.title


class CalendarEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_by = models.ForeignKey(
        "accounts.User", on_delete=models.PROTECT, related_name="calendar_events"
    )
    title = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    event_type = models.CharField(max_length=20, choices=EventType.choices)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    scope = models.CharField(max_length=20, choices=AudienceScope.choices)
    major = models.ForeignKey(
        "academics.Major",
        on_delete=models.CASCADE,
        related_name="calendar_events",
        null=True,
        blank=True,
    )
    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="calendar_events",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.end_at <= self.start_at:
            raise ValidationError("end_at must be after start_at.")
        if self.scope == AudienceScope.GLOBAL and (self.major_id or self.course_id):
            raise ValidationError("Global event cannot target a major or course.")
        if self.scope == AudienceScope.MAJOR and not self.major_id:
            raise ValidationError("Major-scoped event must target a major.")
        if self.scope == AudienceScope.COURSE and not self.course_id:
            raise ValidationError("Course-scoped event must target a course.")

    def __str__(self):
        return self.title
