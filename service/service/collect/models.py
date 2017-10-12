from django.db import models
import django.utils.timezone as future_time_requested


ANONYMOUS = 'user:spongebob'
NA = 'NA'

class Result(models.Model):
    posted = models.DateTimeField('date requested', default=future_time_requested.now)
    origin = models.CharField(max_length=250, default=ANONYMOUS)
    tests = models.TextField(blank=True, default='')
    status = models.TextField(blank=True, default='')
    platform = models.TextField(blank=True, default=NA)
    instrumentation = models.TextField(blank=True, default=NA)
    configuration = models.TextField(blank=True, default=NA)
    cl = models.TextField(blank=True, default=NA)
    duration_ix = models.TextField(blank=True, default=NA)
    duration_ecl2ix = models.TextField(blank=True, default=NA)
    num_processes_ix = models.TextField(blank=True, default=NA)
    num_threads_ix = models.TextField(blank=True, default=NA)
    test_suite = models.TextField(blank=True, default=NA)


    class Meta:
        ordering  = ('-posted',)
