from django.urls import path
from . import views
from .views import redirect_view

app_name = 'todos'
urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', views.index, name='index'),
    path('details/<int:pk>', views.details, name='details'),
    path('todos/add/', views.add, name='add'),
    path('add/', views.add, name='add'),
    path('apps/', views.flexbox, name='flexbox'),
    path('apps/todos/', redirect_view),
    path('apps/bills/', views.indexBills, name='indexBills'),
    path('apps/bills/amounts/', views.addamount, name='addamount'),
    path('amounts/', views.addamount, name='addamount'),
    path('details/details/<int:pk>/deletetodo', views.deletetodo, name='deletetodo'),
]
