from django.shortcuts import render


def profile(request, username):
    ctx = {}
    return render(request, 'profile.html', ctx)

