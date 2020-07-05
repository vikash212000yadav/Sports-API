from django.db import models


# Create your models here.


class Sport(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=256)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='markets')

    def __str__(self):
        return self.name + ' | ' + self.sport.name


class Selection(models.Model):
    name = models.CharField(max_length=256)
    odds = models.FloatField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='selections')

    def __str__(self):
        return self.name


class Match(models.Model):
    name = models.CharField(max_length=256)
    startTime = models.DateTimeField()
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='matches')
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='matches')

    class Meta:
        ordering = ('startTime',)
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.name
