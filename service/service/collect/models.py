from django.db import models
import django.utils.timezone as future_time_requested


ANONYMOUS = 'user:spongebob'


class Result(models.Model):
    posted = models.DateTimeField('date requested', default=future_time_requested.now)
    origin = models.CharField(max_length=250, default=ANONYMOUS)
    passed = models.TextField(blank=True, default='')
    failed = models.TextField(blank=True, default='')
    gold_diff = models.TextField(blank=True, default='')

    class Meta:
        ordering  = ('-posted',)
