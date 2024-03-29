#  Copyright (c) 2023 - All rights reserved.
#  Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.urls import path

from . import views

app_name = 'tabulation'
urlpatterns = [
    path('', views.index, name='index'),
    path("sinewave/", views.sine_wave, name='sine_wave'),
    path("heartbeat/", views.heart_beat, name='heartbeat'),
]
