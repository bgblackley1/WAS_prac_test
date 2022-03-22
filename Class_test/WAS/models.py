from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=128, unique=True)
    start_date = models.CharField(max_length=128, unique=False)
    description = models.CharField(max_length=500, unique=False)

    class Meta:
        verbose_name_plural = 'Courses'

    def __list__(self):
        return [self.title, self.start_date, self.description]
