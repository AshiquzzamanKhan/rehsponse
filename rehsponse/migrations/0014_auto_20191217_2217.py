# Generated by Django 3.0 on 2019-12-17 16:17

from django.db import migrations, models
import rehsponse.models


class Migration(migrations.Migration):

    dependencies = [
        ('rehsponse', '0013_auto_20191216_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='rehsponse',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rehsponse',
            name='rehsponse_image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=rehsponse.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='rehsponse',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]