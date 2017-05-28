from django.shortcuts import render
from .models import Process
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
