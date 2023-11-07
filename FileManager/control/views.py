from django.shortcuts import render

# Create your views here.


def req_type(requests):
    return render(requests, "index.html")
