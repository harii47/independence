from django.shortcuts import render
import datetime

date = datetime.datetime.now()
time = date.time()
date = date.date()


def home(request):
    return render(request, 'index.html')


def return_home(request):
    if request.method == "POST":
        pass
    return render(request, 'index.html', {'date': date, 'time': time})

