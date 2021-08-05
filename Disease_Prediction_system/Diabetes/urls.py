from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name='index'),
    path('diabetes',views.diabetes, name='diabetes'),
    path('diabetesresult',views.diabetesresult, name='diabetesresult')

]