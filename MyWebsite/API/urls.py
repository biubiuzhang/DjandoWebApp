"""MyWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#from .views import article_list, article_details, people_list, people_details
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('articles/<int:id>/', ArticleDetail.as_view()),

    #path('articles', article_list),
    #path('articles/<int:pk>/', article_details),
    #path('peoples', people_list),
    #path('peoples/<int:pk>', people_details),
]
