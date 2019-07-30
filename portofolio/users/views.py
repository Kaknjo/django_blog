from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
#Poruke koje je moguce ispisati sa messagers 
#messages.info
#messages.succes 
#messages.warning
#messages.error
#messages.debug


def register(request):
	if request.method=='POST':
		form=UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, f'Racun kreiran za {username}')
			return redirect('/projects')
	else:
		form=UserRegisterForm()
	return render(request, 'register.html',{'form':form})


# Create your views here.
