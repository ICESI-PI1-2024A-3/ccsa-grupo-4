from django.db import IntegrityError
from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from ..models import Event
from ..models import User


def home(request):
    if request.user.is_superuser:  # Si es el admin, lista todas las tareas
        events = Event.objects.all()
    else:  # si no es el admin, solo lista las tareas asociadas a el/ella
        events = Event.objects.filter(user=request.user)
    return render(request, 'home.html', {'Eventos': events})


def admin(request):
    return redirect(admin.site.urls)


def signup(request):
    if request.method == "GET":
        return render(
            request,
            "signup.html",
            {
                "form": UserCreationForm,
            },
        )
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], email=request.POST['email'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {
                        "form": UserCreationForm,
                        "error": "User already exists",
                    },
                )
        return render(
            request,
            "signup.html",
            {
                "form": UserCreationForm,
                "error": "Password do not match",
            },
        )



def signout(request):
    logout(request)
    return redirect('signin')


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect",
                },
            )
        else:
            login(request, user)
            return redirect('home')


def search_user(request):
    if request.method == 'GET':
        return render(request, 'users_search.html')
    elif request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query.isdigit():  # Si la consulta es un número, buscar por ID
            users = User.objects.filter(id=search_query)
        else:  # De lo contrario, buscar por nombre de usuario
            users = User.objects.filter(username__icontains=search_query)
        return render(request, 'users_search.html', {'users': users})
