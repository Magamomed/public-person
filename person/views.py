from django.shortcuts import render, redirect , get_object_or_404
from .forms import PublicPersonForm, SignUpForm, LoginForm
from .models import PublicPerson
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required
def add_person(request):
    if request.method == 'POST':
        form = PublicPersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_persons')
    else:
        form = PublicPersonForm()
    return render(request, 'person/add_person.html', {'form': form})

@login_required
def list_persons(request):
    persons = PublicPerson.objects.all()
    return render(request, 'person/list_persons.html', {'persons': persons})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_approved = False
            user.save()
            return redirect('approval_pending')
    else:
        form = SignUpForm()
    return render(request, 'person/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_approved:
                    login(request, user)
                    return redirect('add_person')
                else:
                    return redirect('approval_pending')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, 'person/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def approval_pending(request):
    return render(request, 'person/approval_pending.html')

def person_detail(request, pk):
    person = get_object_or_404(PublicPerson, pk=pk)
    return render(request, 'person/person_detail.html', {'person': person})

def person_biography(request, pk):
    person = get_object_or_404(PublicPerson, pk=pk)
    return render(request, 'person/person_biography.html', {'person': person})

def person_works(request, pk):
    person = get_object_or_404(PublicPerson, pk=pk)
    return render(request, 'person/person_works.html', {'person': person})

@login_required
def delete_person(request, pk):
    person = get_object_or_404(PublicPerson, pk=pk)
    if request.method == 'POST':
        person.delete()
        return redirect('list_persons')
    return render(request, 'person/delete_person.html', {'person': person})
