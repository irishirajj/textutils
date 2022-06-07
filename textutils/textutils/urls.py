"""textutils URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
   image.png 2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('displaytextfile',views.displayTextFile,name="displayTextFile"),
    path('punctuationremover',views.rmvpunc,name="rmvpunc"),
    path('capitalizefirstletter',views.capfirst,name="capfirst"),
    path('newlineremover',views.rmvnewline,name="rmvnewline"),
    path('spaceremover',views.rmvspace,name="rmvspace"),
    path('charcounter',views.cntchar,name="cntchar"),
    path('analyze',views.analyze,name='analyze'),
    path('ex1',views.exercise1,name='ex1'),
 
]
