#from django.shortcuts import render, HttpResponse
from http.client import HTTPResponse
from socket import IPV6_DONTFRAG
from .models import Article, People
from .serializers import ArticleSerializer, PeopleSerializer
#from django.http import JsonResponse
#from rest_framework.parsers import JSONParser
#from django.views.decorators.csrf import csrf_exempt
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# def Index(request):
#    return HttpResponse("It is working again.")


'''
# add csrf_exempt to make POST command able to work
# @csrf_exempt
@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def people_list(request):

    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)


@api_view(['GET', ])
def people_details(request, pk):
    try:
        people = People.objects.get(pk=pk)
    except People.DoesNotExist:
        return Response(status == status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PeopleSerializer(people)
        return Response(serializer.data)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''

from rest_framework.decorators import APIView
from django.shortcuts import get_object_or_404


class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):

    def get_object(self, id):
        return get_object_or_404(Article, id=id)

    def get(self, request, id):
        article = self.get_object(id=id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id=id)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id=id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
