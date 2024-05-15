from django.db import models

#Models
class Runner(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)

    def __str__(self):
        return self.firstName + self.lastName

class Run(models.Model):
    runner = models.ForeignKey(Runner,
                               on_delete = models.CASCADE)
    date = models.DateTimeField()
    distance = models.FloatField()
    time = models.DurationField()