# Generated by Django 2.1.4 on 2018-12-28 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_name', models.CharField(max_length=100)),
                ('ad_path', models.CharField(max_length=1000)),
            ],
        ),
    ]
