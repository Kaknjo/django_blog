

# Create your views here.
from django.http import HttpResponse
from django.template import loader


from .models import Question

def index(request):
	# Srtiramo u niz od 5 clanova po datumu objavljivanja pitanja i ispisujemo ih for petljom 

    lista_zadnjih_pitanja=Question.objects.order_by('-pub_date')[:5]
    template=loader.get_template('polls/index.html')
    context={
    	'lista_zadnjih_pitanja':lista_zadnjih_pitanja
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("Pitanje je %s" % question_id)

def result(request, question_id):
	response="Odgovor na pitanje je %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("Glasali ste na pitanje" % question_id)

