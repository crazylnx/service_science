# Generated by Django 2.1.4 on 2019-01-03 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0002_auto_20190103_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(default='static\\img\\photo\\facebook.png', upload_to='static\\img\\photo'),
        ),
    ]
