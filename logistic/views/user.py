from django.db import IntegrityError
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
from django.contrib.auth.decorators import login_required
from ..models import Event
from ..models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


def home(request):
    if request.user.is_superuser:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(user=request.user)
    return render(request, 'home.html', {'Eventos': events})


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
            email = request.POST['email']
            if User.objects.filter(email=email).exists():
                return render(
                    request,
                    "signup.html",
                    {
                        "form": UserCreationForm,
                        "error": "Email already exists",
                    },
                )
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], email=email, password=request.POST['password1'])
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



@login_required
def delete_user(request):
    if request.method == 'POST':
        user = request.user
        
        user_email = user.email
        
        user.delete()

        subject = 'Cuenta eliminada'
        message = f'Hola {user.username},\n\nTu cuenta ha sido eliminada satisfactoriamente.'
        from_email = 'your@example.com'
        recipient_list = [user_email]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print(f"Error al enviar correo electrónico de alerta de eliminación de cuenta: {e}")

        return redirect('signin')
  
    
@login_required  
def user_profile(request):
    return render(request, 'user_profile.html', {'user': request.user})
