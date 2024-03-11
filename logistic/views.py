from django.shortcuts import render
from .models import User


def user_detail(request):

    if request.method == 'GET':

        query = request.GET.get('q', '')
        users = User.objects.filter(name__icontains=query) | User.objects.filter(
            id_number__icontains=query)

        return render(request, 'users.html', {'users': users})


def search_users(request):

    name_query = request.GET.get('name', None)
    id_query = request.GET.get('id', None)

    users = []

    if name_query:

        users = User.objects.filter(name__icontains=name_query)

    elif id_query:

        users = User.objects.filter(id_number=id_query)

    return render(request, 'users_search.html', {'users': users})
