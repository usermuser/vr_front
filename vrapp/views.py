from django.shortcuts import render
from .models import Process
<<<<<<< HEAD
from django.views import generic



class ProcessListView(generic.ListView):
    template_name = 'vrapp/process_list'
    context_object_name = 'latest_process_list'

    def get_queryset(self):
        '''Return all process list''' 
        return Process.objects.all()

'''    queryset = Process.objectall()
    latest_question_list = Process.objects.order_by('-pub_date')[:5]
    context = {'latest_process_list': latest_question_list}
    return render(request, 'vrapp/index.html', context)
'''
=======

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    latest_question_list = Process.objects.order_by('-pub_date')[:5]
    context = {'latest_process_list': latest_question_list}
    return render(request, 'vrapp/index.html', context)
>>>>>>> e5ab72fa5fc8bb8ed5d99ded23dfa8793c9622b0
