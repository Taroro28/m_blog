# Generated by Django 2.1.7 on 2019-03-22 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190322_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='target_subcategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.SubCategory'),
        ),
    ]
