from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Thread


def index(request):
    latest_thread_list = Thread.objects.order_by('-created_on')[:5]
    context = {'latest_thread_list': latest_thread_list}
    return render(request, 'threads/index.html', context)


def detail(request, thread_id):
    try:
        thread = Thread.objects.get(pk=thread_id)
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    # thread = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'threads/detail.html', {'thread': thread})


def vote(request, thread_id):
    return HttpResponse("You're voting on thread %s." % thread_id)

def results(request, thread_id):
    response = "You're looking at the results of thread %s."
    return HttpResponse(response % thread_id)

