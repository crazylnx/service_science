# Generated by Django 2.1.4 on 2019-01-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='static\\img\\photo\\facebook.png', max_length=200, upload_to='static\\img\\photo'),
        ),
    ]
