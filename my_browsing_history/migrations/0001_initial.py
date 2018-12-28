# Generated by Django 2.1.4 on 2018-12-28 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_comments', '0002_comment'),
        ('log_in', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_date', models.DateTimeField(verbose_name='date published')),
                ('history_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_comments.question')),
                ('history_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log_in.user')),
            ],
        ),
    ]
