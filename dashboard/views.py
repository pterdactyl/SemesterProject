#  Copyright (c) 2023 - All rights reserved.
#  Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

import datetime
import time
import json

import numpy as np
from .models import SineData
from django.db import connection
from django.shortcuts import render


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



def heartbeat(request):
    if "start_time" in request.GET:
        start_time = request.GET['start_time']
        start_time = datetime.datetime.strptime(start_time, '%H:%M')

        start_time = start_time.replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        start_time = time.mktime(start_time.timetuple())
    else:
        start_time = time.time()

    if 'queries' in request.GET:
        queries = request.GET['queries']
    else:
        queries = 300
    data = Get_HearBeatData(start_time, queries)

    if data == [] or data == ():
        template = 'error.html'
        return render(request, template)
    template = 'dashboard/heartbeat.html'
    start_time = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M')

    if request.user.is_authenticated:
        profile_picture = request.user.profile.profile_picture
    else:
        profile_picture = "profile_pictures/user_placeholder.svg"

    context = {
        "queries"        : queries,
        "start_time"     : start_time,
        "data"           : data,
        'profile_picture': profile_picture
    }
    return render(request, template, context)


def Get_SineData(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT data_val, label as labels from dashboard_sinedata where label between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(time=time_stamps, records=records)
    cur.execute(command)
    return dictfetchall(cur)


def Get_HearBeatData(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT value, time_stamp from dashboard_heartbeatdata where time_stamp between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(time=time_stamps,
                                                                                                                                                                                         records=records)
    cur.execute(command)
    return dictfetchall(cur)


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

