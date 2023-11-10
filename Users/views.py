from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import RegisterForm, loginForm


def register_view(request):

    if request.nethod == 'GET':
        contex_data = {
            'form': RegisterForm
        }

        return render(request, 'users/register.html', context=contex_data)

    if request.nethod == 'POST':
        data = request.POST
        form = RegisterForm(data)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        if cleaned_data.get('password1') == cleaned_data.get('password2'):
            User.objects.create_user(
                username=cleaned_data.get('username'),
                password=cleaned_data.get('password1')
            )
            return redirect('/users/login')
        else:
            form.add_error('password1', 'sorry try again :)')


        context_data = {
            'form': form
        }

        return render(request, 'users/register.html', context=context_data)

def login_view(request, context_data=None):

    if request.nethod == 'GET':
        contex_data = {
            'form': loginForm
        }

        return render(request, 'users/login.html', context=context_data)


    if request.nethod == 'POST':
        data = request.POST
        form = loginForm(data)

        if form.is_valid():
            """authenticate"""
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password'),
            )

            if user:
                """authorization"""
                login(request=user, user=user)
                return redirect('/post')
            else:
                form.add_error('username', 'sorry try again :)')

        context_data = {
            'form': form
        }

        return render(request, 'user/login.html', context=context_data)

def logout_view(request):
    logout(request)
    return redirect('/post')