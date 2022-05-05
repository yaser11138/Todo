from django.db import models
from django.contrib.auth.models import User


class TodoManager(models.Manager):
    def get_all_todos_related_to_user(self, user):
        return self.filter(user=user).order_by("-date", "-time")

    def get_today_todos_related_to_user(self, user,date):
        return self.filter(user=user, date=date)


class Todo(models.Model):
    title = models.CharField(max_length=10)
    date = models.DateField()
    time = models.TimeField()
    is_complete = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = TodoManager()

    class Meta:
        unique_together = ["date", "time"]

    def __str__(self):
        return self.title



