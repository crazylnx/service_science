# Generated by Django 2.1.4 on 2019-01-06 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0008_auto_20190106_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=1000),
        ),
    ]
