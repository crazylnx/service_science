# Generated by Django 2.1.4 on 2019-01-06 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_comments', '0004_comment_comment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_type',
        ),
    ]
