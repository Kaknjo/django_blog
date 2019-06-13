

# Create your views here.
from django.http import HttpResponse

from .models import Question

def index(request):
	# Srtiramo u niz od 5 clanova po datumu objavljivanja pitanja i ispisujemo ih for petljom 

    lista_zadnjih_pitanja=Question.objects.order_by('-pub_date')[:5]
    izlaz=','.join([q.question_text for q in lista_zadnjih_pitanja])
    return HttpResponse(izlaz)

def detail(request, question_id):
	return HttpResponse("Pitanje je %s" % question_id)

def result(request, question_id):
	response="Odgovor na pitanje je %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Glasali ste na pitanje" % question_id)

