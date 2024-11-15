from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User

# def index(request):
#     return HttpResponse("Hi!")


def index(request):
    courses = User.objects.all()
    return HttpResponse("Hi!")

    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))
    # return render(request, 'user/courses.html', {'courses': courses})
