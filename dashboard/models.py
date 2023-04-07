#  Copyright (c) 2023 - All rights reserved.
#  Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

import datetime

from django.db import models

class SineData(models.Model):
    data_val = models.DecimalField(decimal_places=20, max_digits=30)
    label = models.TimeField(auto_now=True)

    class Meta:
        ordering = ['-label']

    def get_data(self, start, end):
        self.start = datetime.time(start)
        self.end = datetime.time(end)
        self.data = SineData.objects.filter(label__gte=self.start, label__lte=self.end)
        return self.data


class HeartBeatData(models.Model):
    value = models.DecimalField(decimal_places=25, max_digits=30)
    time_stamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-time_stamp']

