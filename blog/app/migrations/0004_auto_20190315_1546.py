# Generated by Django 2.1.7 on 2019-03-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190315_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='headline2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='headline3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='blog',
            name='text2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='text3',
            field=models.TextField(blank=True),
        ),
    ]