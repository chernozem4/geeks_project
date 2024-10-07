# Generated by Django 5.1.1 on 2024-10-03 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_category_searchword_alter_post_is_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='posts.category'),
        ),
        migrations.AddField(
            model_name='post',
            name='search_word',
            field=models.ManyToManyField(blank=True, to='posts.searchword'),
        ),
    ]
