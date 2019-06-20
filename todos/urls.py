from django.urls import path
from . import views
from .views import redirect_view
from .views import deletetodo
from .views import deleterecipe

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
    path('apps/recipes/', views.recipe_view, name='recipe_view'),
    path('recipe/details_recipe/<int:pk>', views.details_recipe, name='details_recipe'),
    path('deleterecipe/<int:pk>/', deleterecipe),
    path('recipe/addrecipe/', views.addrecipe, name='addrecipe'),
    path('addrecipe/', views.addrecipe, name='addrecipe'),
]
