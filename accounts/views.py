from django.shortcuts import render

from users.forms import CustomUserCreationForm, CustomUserChangeForm, CustomUserLoginForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email)')
            password = form.cleaned_data.get('password')

            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = CustomUserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

