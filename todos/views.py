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
    todo = Todo.objects.get(pk=pk)#Note the pk=pk and the url.
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


def flexbox(request):
    return render(request, 'FlexBox.html')


def redirect_view(request):
    response = redirect('/todos/')
    return response


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
    bill = Bills.objects.get(pk=pk)#Note the pk=pk and the url.
    context = {'bill': bill
               }

    return render(request, 'detailsBills.html', context)


def deletetodo(request, pk):
    if request.method == 'POST':
        d = Bills.objects.get(pk=pk)
        d.delete()
    return redirect('/todos/')

