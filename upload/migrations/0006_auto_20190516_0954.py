# Generated by Django 2.2 on 2019-05-16 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_auto_20190516_0944'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cover',
            new_name='image',
        ),
    ]