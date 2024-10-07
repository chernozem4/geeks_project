from django.db import models
from django.utils.translation.trans_null import npgettext

class AbsrtactModel(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

class Category(AbsrtactModel):
    pass

class SearchWord(AbsrtactModel):
    pass


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    search_word = models.ManyToManyField(SearchWord, blank=True)
    title = models.CharField(max_length=255)
    text = models.TextField(null = True)
    is_active= models.BooleanField(default=True, null = True)
    view_count = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    @property
    def search_word_list(self):
        return [i.name for i in self.search_word.all()]

STARS = (
    (1, '*'),
    (2, '**'),
    (3, '***'),
    (4, '****'),
    (5, '*****'),

)


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    stars = models.IntegerField(choices=STARS, default=5)

    def __str__(self):
        return self.text



