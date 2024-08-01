
from django.contrib import admin
from django.urls import path

import mainapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp.views.index,name='index_url')

]
