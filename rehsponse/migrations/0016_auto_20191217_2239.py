# Generated by Django 3.0 on 2019-12-17 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rehsponse', '0015_rehsponse_reply'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rehsponse',
            old_name='parent',
            new_name='replying_to',
        ),
    ]