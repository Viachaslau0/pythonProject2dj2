from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import Sigh_inForm, Login_inForm

def login_view(request):
    if request.method == 'POST':
        form = Login_inForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = Login_inForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = Sigh_inForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/restaurant/categories/')
    else:
        form = Sigh_inForm()
    return render(request, 'register.html', {'form': form})

def home(request):
    if request.method == 'POST':
        # Обработка формы регистрации
        register_form = Sigh_inForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('home')

        # Обработка формы входа
        login_form = Login_inForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        register_form = Sigh_inForm()
        login_form = Login_inForm()

    return render(request, 'home.html', {'register_form': register_form, 'login_form': login_form})