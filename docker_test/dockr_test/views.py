import os
import socket

from django.http import HttpResponse
from .tasks import add
from django.shortcuts import render


# Create your views here.


def home(request):
    add.delay(4,4)
    return HttpResponse("Hello {0}-{1}".format(os.getenv("Name","world"),socket.gethostname()))