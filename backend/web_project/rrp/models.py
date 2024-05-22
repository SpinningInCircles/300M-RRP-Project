from django.db import models

class Runner(models.Model):
    firstName = models.CharField(max_length = 150)
    lastName = models.CharField(max_length = 150)


class Run(models.Model):
    runnerName = models.ForeignKey(Runner,
                                   on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now = True)
    duration = models.DurationField()
    distance = models.FloatField()
    