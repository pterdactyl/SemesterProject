#  Copyright (c) 2023 - All rights reserved.
#  Created by Peter Lin for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Peter Lin, 400270145 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.
from django.contrib import auth
from django.shortcuts import render


def index(request):
    data = ""
    user_details = auth.get_user(request)
    profile_picture = 'user_placeholder.svg'
    context = {
        'data': data,
        'profile_picture': profile_picture
    }
    return render(request, 'index.html', context)