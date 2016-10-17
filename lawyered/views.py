from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, divorceForm
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from .models import person
# Create your views here.
def index(request) :
	return render(request, 'lawyered/index.html')
	
def login(request):
	if request.method== 'POST':

		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			username = form.cleaned_data['username']
			if user is not None:
				#login(request,user)
				return render(request,'lawyered/dashboard.html', {'username': username})
			else:
				return render(request, 'lawyered/invalid.html')

	else:
		form = LoginForm()
		return render(request, 'lawyered/login.html', {'form': form})
	

#@login_required
#def dashboard(request):
#	return render(request,'lawyered/dashboard.html',{'section': 'dashboard'})

def register(request):
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			# Create a new user object but avoid saving it yet
			new_user = user_form.save(commit=False)
			# Set the chosen password
			new_user.set_password(user_form.cleaned_data['password'])
			# Save the User object
			new_user.save()
			return render(request,'lawyered/register_done.html')
	else:
		user_form = UserRegistrationForm()
	return render(request,'lawyered/register.html',{'user_form': user_form})

@login_required
def dashboard(request):
	return render(request, 'lawyered/dashboard.html')


def person_list(request):
	persons = person.objects.all()
	query = request.GET.get("q")
	if query:
		persons = persons.filter(area__contains = query)
	return render(request,'lawyered/search.html',{'persons': persons})
	
def divorce(request):
	if request.method== 'POST':

		form = divorceForm(request.POST)
		if form.is_valid():
			
			return render(request,'lawyered/done.html')

	else:
		form = divorceForm()
		return render(request, 'lawyered/divorce.html', {'form': form})
	