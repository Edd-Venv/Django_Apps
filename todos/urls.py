from django.urls import path
from . import views
from .views import redirect_view
from .views import deletetodo

app_name = 'todos'
urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.index, name='index'),
    path('details/<int:pk>', views.details, name='details'),
    path('todos/add/', views.add, name='add'),
    path('add/', views.add, name='add'),
    path('apps/', views.appilcations, name='applications'),
    path('apps/todos/', redirect_view),
    path('apps/bills/', views.indexBills, name='indexBills'),
    path('apps/bills/amounts/', views.addamount, name='addamount'),
    path('amounts/', views.addamount, name='addamount'),
    path('deletetodo/<int:pk>/', deletetodo),
]
