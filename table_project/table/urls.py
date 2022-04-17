from django.contrib import admin
from django.urls import path, include
from table import views as view


urlpatterns = [
    path('table1/', view.table1, name='table1'),
    path('multiplechoicefield/', view.modelmultiplechoicefield, name='modelmultiplechoicefield'),
    path('', view.home, name='home'),
]
