# Generated by Django 2.1.7 on 2019-03-30 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20190330_1828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='main_sentance',
            new_name='main_sentence',
        ),
    ]
