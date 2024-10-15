from rest_framework import serializers
from posts.models import Post, SearchWord, Category
from rest_framework.exceptions import ValidationError

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
        fields = 'id comments title view_count category_name category search_word search_word_list created'.split()
        # depth = 1


    def get_category_name(self, post):
        return post.category.name if post.category else None



        #добавить все
        #fields = '__all__'

        #исключение
        #exclude = 'created text'.split()


class PostValidateSerializer(serializers.Serializer):
    title = serializers.CharField(min_length=5, max_length=255)
    text = serializers.CharField(required=False)
    is_active = serializers.BooleanField()
    view_count = serializers.IntegerField(min_value=0, max_value=100)
    category_id= serializers.IntegerField(min_value=1)
    search_word = serializers.ListField(child=serializers.IntegerField(min_value=1))


    # def validate(self, attrs):
    #     category_id = attrs.get('category_id') #99
    #     try:
    #         Category.objects.get(id=category_id)
    #     except Category.DoesNotExist:
    #         raise ValidationError('Category does not exist')
    #     return attrs

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exist')
        return category_id


    def validate_search_word(self, search_word):   #[1,2,99]
        search_word_db=SearchWord.objects.filter(id__in=search_word)
        if len(search_word_db) != len(search_word):
            raise ValidationError('search word is not exist')
        return search_word








