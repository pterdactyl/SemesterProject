import datetime

from django.db import models


class SineData(models.Model):
    data_val = models.DecimalField(decimal_places=20, max_digits=30)
    time_stamp = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-time_stamp']

    def get_data(self, start, end):
        self.start = datetime.time(start)
        self.end = datetime.time(end)
        self.data = SineData.objects.filter(label__gte=self.start, label__lte=self.end)
        return self.data
