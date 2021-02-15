from django.shortcuts import render, redirect

from user.forms import CustomUserCreationForm
from user.models import User


def user_login(request):
    return render(
        request,
        'user/login.html'
    )


def user_registration(request):
    user_create_form = CustomUserCreationForm()
    if request.method == 'POST':
        user_create_form = CustomUserCreationForm(request.POST, files=request.FILES)
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