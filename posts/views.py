from django.db.migrations import serializer
from django.shortcuts import render
from django.template.defaultfilters import title
from rest_framework.decorators import api_view
from rest_framework.response import Response
from posts.models import Post
from posts.serializers import PostSerializer, PostValidateSerializer
from rest_framework import status

@api_view(http_method_names=['GET', 'POST'])
def post_list_create_api_view(request):
    if request.method == 'GET':
        print(request.query_params)
        search = request.query_params.get('search', '')

        #step 1: Collect  (QuerySet)
        post = Post.objects.select_related('category').prefetch_related('search_word', 'comments').filter(title__icontains=search)

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
    elif request.method == 'POST':
        #step 0: validation of data(existing, typing)
        serializer = PostValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        title = serializer.data.get('title') #None
        text = serializer.data.get('text')
        is_active = serializer.data.get('is_active')
        view_count = serializer.data.get('view_count')
        category_id = serializer.data.get('category_id')
        search_word = serializer.data.get('search_word')

        post = Post.objects.create(
            title=title,
            text=text,
            is_active=is_active,
            view_count=view_count,
            category_id=category_id,

        )
        post.search_word.set(search_word)
        post.save()
        return Response(status = status. HTTP_201_CREATED,
                        data = {'post_id': post.id})



@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def post_detail_api_view(request, id):
    # step 1: Collect  (QuerySet)
    try:
        post = Post.objects.get(id = id)
    except Post.DoesNotExist:
        return Response(data={'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        # step 2: Reformat posts to list of Dictionaries (json)
        data = PostSerializer(instance=post, many=False).data

        # step 3: Return response as JSON
        return Response(data=data)

    elif request.method == 'PUT':
        post.title = serializer.data.get('title')
        post.text = serializer.data.get('text')
        post.is_active = serializer.data.get('is_active')
        post.view_count = serializer.data.get('view_count')
        post.category_id = serializer.data.get('category_id')

        post.search_word.set(serializer.data.get('search_word'))
        post.save()
        return Response(data=PostSerializer(post).data,
                        status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
