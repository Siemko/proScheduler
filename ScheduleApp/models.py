from django.db import models
from django.utils import timezone
import datetime


class Days(models.Model):
    day_date = models.DateField('Day to plan')
    min_date = datetime.date.today()

    def __str__(self):
        return self.day_date.strftime('%m/%d/%Y')

    def plans_inpast(self):
        return (self.day_date >= datetime.date.today())


class DayTasks(models.Model):
    day = models.ForeignKey(Days, on_delete=models.CASCADE,related_name="tasks")
    task_text = models.CharField(max_length=300)

    def __str__(self):
        return self.task_text


