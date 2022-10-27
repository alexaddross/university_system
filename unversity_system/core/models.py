import uuid
from django.db import models
from user.models import User


class Discipline(models.Model):
    id = models.UUIDField(uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=255)


class StudentGroup(models.Model):
    id = models.UUIDField(uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(User)

    def save(self):
        if self.students.count() > 3:
            raise ValueError('There is maximum of 20 students in group')
        else:
            super(StudentGroup, self).save()


class StudyingDirection(models.Model):
    id = models.UUIDField(uuid.uuid4(), primary_key=True)
    name = models.CharField(max_length=255)
    disciplines = models.ForeignKey(Discipline, on_delete=models.SET_NULL, null=True)
    groups = models.ForeignKey(StudentGroup, on_delete=models.SET_NULL, null=True)
