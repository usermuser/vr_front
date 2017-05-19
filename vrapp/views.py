from django.shortcuts import render
from .models import Process

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Process.objects.order_by('-pub_date')[:5]
    context = {'latest_process_list': latest_question_list}
    return render(request, 'vrapp/index.html', context)
