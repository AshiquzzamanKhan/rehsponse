# Generated by Django 3.0 on 2019-12-14 07:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehsponse', '0007_auto_20191214_0338'),
    ]

    operations = [
        migrations.AddField(
            model_name='rehsponse',
            name='loved',
            field=models.ManyToManyField(blank=True, related_name='loved', to=settings.AUTH_USER_MODEL),
        ),
    ]