# Generated by Django 2.1.4 on 2019-01-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0005_auto_20190104_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='signature',
            field=models.CharField(default='这个人很懒，什么都没留下', max_length=2000),
        ),
    ]
