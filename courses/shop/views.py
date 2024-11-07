from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


def index(request):
    courses = Course.objects.all()
    # return HttpResponse(''.join([str(course) + '<br>' for course in courses]))
    return render(request, 'shop/courses.html', {'courses': courses})


def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})
