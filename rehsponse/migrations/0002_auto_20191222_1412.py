# Generated by Django 3.0 on 2019-12-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehsponse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]