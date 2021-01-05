from django.shortcuts import render
import random

def home(request):
    return render(request, 'generator/home.html')

def generate(request):

    options = list()

    if (request.GET.get('lowercase')):
        options.extend('abcdefghijklmnopqrstuvwxyz')

    if (request.GET.get('uppercase')):
        options.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    if (request.GET.get('numbers')):
        options.extend('0123456789')

    if (request.GET.get('symbols')):
        options.extend('!@#$%^&*()_+-=')

    options.extend(set(request.GET.get('additional_letters')))

    password = ''

    if len(options):
        length = int(request.GET.get('length', 12))
        for i in range(length):
            password += random.choice(options)

    return render(request, 'generator/view_pass.html', { 'password':password })
