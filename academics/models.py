import uuid

from django.core.exceptions import ValidationError
from django.db import models


class TermType(models.TextChoices):
    FALL = "fall", "Fall"
    SPRING = "spring", "Spring"
    SUMMER = "summer", "Summer"
    ANNUAL = "annual", "Annual"


class Major(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.code} - {self.name}"


class Semester(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    year = models.PositiveIntegerField()
    term = models.CharField(max_length=20, choices=TermType.choices)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-year", "term"]
        constraints = [
            models.UniqueConstraint(fields=["year", "term"], name="uniq_year_term")
        ]

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("end_date must be after start_date.")

    def __str__(self):
        return f"{self.name} ({self.term} {self.year})"
