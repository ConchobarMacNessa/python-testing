from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	try:
		qu = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/details.html', {'question': qu})

def results(request, question_id):
	response = "You're looking at question %s." 
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)
