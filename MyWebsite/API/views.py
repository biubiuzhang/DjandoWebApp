from django.shortcuts import render, HttpResponse
from .models import Article, People
from .serializers import ArticleSerializer, PeopleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

# Create your views here.

# def Index(request):
#    return HttpResponse("It is working again.")


def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def people_list(request):

    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return JsonResponse(serializer.data, safe=False)
