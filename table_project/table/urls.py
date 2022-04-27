from django.contrib import admin
from django.urls import path, include
from table import views as view


urlpatterns = [
    path('table1/', view.table1, name='table1'),
    path('table2/', view.table2, name='table2'),
    path('table3/', view.table3, name='table3'),
    path('multiplechoicefield/', view.modelmultiplechoicefield, name='modelmultiplechoicefield'),
    path('', view.home, name='home'),
    path('jsonresponse/footballclubs', view.footballclubs, name='footballclubs'),
]
