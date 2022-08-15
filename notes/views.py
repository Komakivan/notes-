
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import NotesForm
from .models import Notes


# Create your views here.

def index(request):

    note = Notes.objects.all().order_by('-created')
    context = {
        'notes':note,
    }
    return render(request, 'home.html',context )


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pwd')
        pass2 = request.POST.get('confirm')

        if pass1 == pass2:
            user = User.objects.create_user(username, email, pass1)
            user.pass2 = pass2
            user.save()
            # messages.success(request, 'your account has been created successfully')
            return redirect('signin')


    return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username= request.POST['uname']
        password = request.POST['pwd']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    return redirect('signup')


def update(request,pk):

    if request.method == 'POST':
        note = Notes.objects.get(id=pk)
        form = NotesForm(request.POST,instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        note = Notes.objects.get(id=pk)
        form = NotesForm(instance=note)
    contex = {
        'form':form,
    }
    return render(request, 'notes_form.html',contex)


def delete(request,pk):
    note = Notes.objects.get(id=pk)
    note.delete()
    return redirect('index')



def forms(request):
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NotesForm()

    context = {
        'form': form,
    }
    return render(request, 'notes_form.html',context)

def notes_content(request,pk):
    note = Notes.objects.get(id=pk)
    context = {'note':note}
    return render(request,'notes.html',context)