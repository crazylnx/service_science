# Generated by Django 2.1.4 on 2018-12-28 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_date', models.DateTimeField(verbose_name='date published')),
                ('comment_content', models.CharField(max_length=5000)),
                ('comment_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_comments.question')),
            ],
        ),
    ]
