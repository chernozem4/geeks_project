from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer
from rest_framework import status

@api_view(http_method_names=['GET'])
def post_list_api_view(request):
    #step 1: Collect  (QuerySet)
    post = Post.objects.select_related('category').prefetch_related('search_word', 'comments').all()

    #step 2: Reformat posts to list of Dictionaries (json)
    data = PostSerializer(instance=post, many=True).data

    #2 способ
    #list_ = []
    #for post in posts:
    #    list_.append({
    #        'ig': post.id,
    #        'title': post.title,
    #        'text': post.text,
    #        'is_active': post.is_active
    #    })


    #step 3: Return response as JSON
    return Response(data = data)


@api_view(http_method_names=['GET'])
def post_detail_api_view(request, id):
    # step 1: Collect  (QuerySet)
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response(data={'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    # step 2: Reformat posts to list of Dictionaries (json)
    data = PostSerializer(instance=post, many=False).data

    # step 3: Return response as JSON
    return Response(data=data)