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
    #path('details/details/<int:pk>/deletetodo', views.redirect_view1),
]
# path('', views.home, name='home'),
# path('todos/add/', views.add, name='add'),
# path('add/', views.add, name='add'), I need to add this path and
# also redirect it to /todos/ not todos/#
# note how i used redirect_view to go to another url