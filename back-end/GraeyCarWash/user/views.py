from django.conf import settings
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms import CustomUserCreationForm
from user.models import User
from django.contrib.auth.forms import AuthenticationForm


def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect(settings.LOGOUT_REDIRECT_URL)
    return HttpResponse(status=405)


def user_login(request):
    if request.user.is_authenticated:
        return redirect('wash:washer-list')
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('wash:washer-list')

    return render(
        request,
        'user/login.html',
        context={
            'form': form
        }
    )


def user_registration(request):
    user_create_form = CustomUserCreationForm()
    if request.method == 'POST':
        user_create_form: CustomUserCreationForm = CustomUserCreationForm(request.POST, files=request.FILES)
        if user_create_form.is_valid():
            customer: User = user_create_form.save(commit=False)
            customer.status = User.Status.customer
            customer.save()
            return redirect('user:user_login')

    return render(
        request,
        template_name='user/registration.html',
        context={
            'form': user_create_form
        }
    )