from rest_framework import serializers
from posts.models import Post, SearchWord, Category

class SearchWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchWord
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many = False)
    search_word= SearchWordSerializer(many = True)
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = 'id comments title view_count category_name category search_word created'.split()
        # depth = 1


    def get_category_name(self, post):
        return post.category.name if post.category else None



        #добавить все
        #fields = '__all__'

        #исключение
        #exclude = 'created text'.split()





