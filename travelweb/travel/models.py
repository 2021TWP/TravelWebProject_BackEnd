from django.db import models
# from django.contrib.auth.models import Group

class Schedule_content(models.Model):
    objects = models.Manager()
    content = models.TextField()
    travel_date = models.DateTimeField


class Schedule(models.Model):
    objects = models.Manager()
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE())
    content_id = models.ForeignKey(Schedule_content, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=300)

# Create your models here.
