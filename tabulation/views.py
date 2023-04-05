import datetime
import time

import numpy as np
from django.db import connection
from django.shortcuts import render


def index(request):
    data = []
    values = np.linspace(0, 1000, 1000)
    values = np.sin(values * np.pi ** 2)
    FFT = fft_sine(values)
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i], "fft": FFT[i]})

    if (request.method == "GET"):
        pass
    gets = {"fft_hide": request.GET.get('fft_hide')}
    debug = request.method
    context = {
        "data" : data,
        "gets" : gets,
        "debug": debug
    }
    page = 'tabulation/sinewave.html'
    return render(request, page, context)


def sine_wave(request):
    data = []
    if "start_time" in request.GET:
        start_time = request.GET['start_time']
        start_time = datetime.datetime.strptime(start_time, '%H:%M')

        start_time = start_time.replace(year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
        start_time = time.mktime(start_time.timetuple())
    else:
        start_time = time.time()

    if 'records' in request.GET:
        records = request.GET['records']
    else:
        records = 5000
    values = Get_SineData(start_time, records)
    for val in values:
        data.append(val['data_val'])
    FFT = fft_sine(data)
    data = []
    for i in range(len(values)):
        data.append({'label': i, 'value': values[i]['data_val'], "fft": FFT[i]})

    gets = {"fft_hide": request.GET.get('fft_hide')}

    start_time = datetime.datetime.fromtimestamp(start_time).strftime('%H:%M')

    context = {
        "data"      : data,
        "gets"      : gets,
        'start_time': start_time,
        'records'   : records
    }
    page = 'tabulation/sinewave.html'
    return render(request, page, context)


def fft_sine(data):
    data = np.fft.fft(data)
    return data


def Get_SineData(time_stamps, records):
    cur = connection.cursor()
    command = "SELECT * from dashboard_sinedata where label between  FROM_UNIXTIME({time})-interval 1 minute and FROM_UNIXTIME({time}) limit {records}".format(time=time_stamps, records=records)
    cur.execute(command)
    return dictfetchall(cur)


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
