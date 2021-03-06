# Generated by Django 2.1.7 on 2019-03-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_post_target_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
    ]
