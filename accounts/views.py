from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse

@login_required(login_url='/accounts/login/')
def index(request):
    page = 'accounts/index.html'
    context = {
        "profile_picture": "user_placeholder.svg"
    }
    response = render(request, template_name=page, context=context)
    response.set_cookie('profile_picture', 'user_placeholder.svg')

def signup(request):
    page = 'accounts/signup.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/')
    else:
        form = UserCreationForm()
    context = {
        "form": form
    }
    return render(request, page, context)