# Generated by Django 2.1.7 on 2019-03-20 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_comment_target'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='target',
            new_name='post',
        ),
    ]
