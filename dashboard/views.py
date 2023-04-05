import datetime
import json
import time

import numpy as np
from django.shortcuts import render
from .models import SineData

class SineWaveData:
    values: int = []
    labels: str = []

    def __init__(self):
        labels = np.linspace(0, 1000, 1000, dtype=int)
        values = np.sin(labels * np.pi ** 2)
        self.values = json.dumps(values.tolist())
        self.labels = json.dumps(labels.tolist())


def index(request):
    template = 'dashboard/sinewave.html'
    if request.method == "POST":

        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        data = SineData.get_data(start_time, end_time)
    else:
        time_scale = (time.time(), time.time()-datetime.timedelta(minutes=5))
        data = SineData.get_data(time.time(), time.time()-datetime.timedelta(minutes=5))
    context = {
        "time_scale": time_scale,
        "data": data,

    }
    return render(request, template, context)


def sinewave(request):
    template = 'dashboard/sinewave.html'
    data = SineWaveData
    context = {
        "data": data,
    }
    return render(request, template, context)
