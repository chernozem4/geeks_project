from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'id title view_count created'.split()


        #добавить все
        #fields = '__all__'

        #исключение
        #exclude = 'created text'.split()
