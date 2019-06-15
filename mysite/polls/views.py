from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Choice, Question

def index(request):
	# Formira se niz pitanja na osnovu datuma dodavanja pitanja 
	lista_zadnjih_pitanja=Question.objects.order_by('-pub_date')[:5]
	context={
		'lista_zadnjih_pitanja':lista_zadnjih_pitanja
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	#Ukoliko postoji u bayi pitanje sa idom koji smo proslijedili renderovat ce se template i program ce raditi u suptotnom dobit cemo erroor
	pitanje=Question.objects.get(pk=question_id)
	rezultat=get_object_or_404(Question, pk=question_id)
	context={
	'pitanje':pitanje
	}
	return render(request, 'polls/detail.html', context)



def result(request, question_id):
	pitanje=Question.objects.get(pk=question_id)
	return render(request, 'polls/result.html', {
		'pitanje':pitanje
		})
	

def vote(request, question_id):
	#Provjera da li postoji pitanje sa datim idom ukoliko postoji program ce nastaviti dalje ukoliko ne postoji dobit cemo error
	pitanje=get_object_or_404(Question, pk=question_id)
	try: 
		#Ukoliko postoji Choice poslan post zahtjevom sa templatea snimit cemo ga u varijablu selected choice , ukoliko choice ne postoji il iga nismo aktivirali ispisat ce se greska
		selected_choice=pitanje.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html',{ 
			'pitanje':pitanje, 
			'error': "Greska"})
	else:
		#Ukoliko smo glasali na odredeni choice broj glasova za taj choice se povecava za jedan i vracamo se na stranicu npr polls/ 1/result/
		selected_choice.votes+=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:result', args=(pitanje.id,)))

