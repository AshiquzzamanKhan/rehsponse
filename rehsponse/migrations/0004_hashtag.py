# Generated by Django 3.0 on 2019-12-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rehsponse', '0003_auto_20191212_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=120)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
