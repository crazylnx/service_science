# Generated by Django 2.1.4 on 2019-01-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_in', '0003_auto_20190103_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.FileField(default='static\\img\\photo\\facebook.png', upload_to='img\\photo\\%Y\\%m\\%d'),
        ),
    ]
