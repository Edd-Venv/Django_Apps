from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from .models import Todo
from .models import Bills


def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos': todos
              }
    return render(request, 'index.html', context)


def details(request, pk):
    todo = Todo.objects.get(pk=pk)
    context = {'todo': todo
               }
    return render(request, 'details.html', context)


def add(request):
    if request.method == 'POST':
        new_user_title = request.POST.get('title')
        new_user_text = request.POST.get('text')

        s = Todo(title=new_user_title, text=new_user_text)
        s.save()

        return redirect('/todos/')
    else:
        return render(request, 'add.html')


def home(request):
    return render(request, 'home.html')


def applications(request):
    return render(request, 'Applications.html')


def redirect_view(request):
    response = redirect('/todos/')
    return response

def deletetodo(request, pk):
    todo_to_delete = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo_to_delete.delete()
        return redirect('/todos/')
    else:
        return render(request, 'details.html')


# Bills Views below

def addamount(request):
    if request.method == 'POST':
        new_user_title = request.POST.get('title')
        new_user_amount = request.POST.get('amount')

        a = Bills(title=new_user_title, amount=new_user_amount)
        a.save()

        return redirect('/apps/bills/')
    else:
        return render(request, 'amounts.html')


def indexBills(request):
    context = {
        'bills': Bills.objects.all()[:10]
    }
    return render(request, 'indexBills.html', context)


def detailsBills(request, pk):
    bill = Bills.objects.get(pk=pk)
    context = {'bill': bill
               }

    return render(request, 'detailsBills.html', context)


