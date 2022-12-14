from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from socialmedia.forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Login realizado com sucesso')
                else:
                    return HttpResponse('Conta não-ativa')
            else:
                return HttpResponse('Login inválido')
    else:
        form = LoginForm()
    return render(request, 'socialmedia/pages/login.html', {'form': form})
