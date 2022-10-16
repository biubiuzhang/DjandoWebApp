from rest_framework import serializers
from .models import Article

# To user serializer
#   1. python manage.py shell
#   2. from API.serializers import ArticleSerializer
#   3. s = ArticleSerializer()
#   4. print(repr(s))
#   5. Output:
#      ArticleSerializer():
#      id = IntegerField(label='ID', read_only=True)
#      title = CharField(max_length=100)
#      description = CharField(style={'base_template': 'textarea.html'})


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description']
