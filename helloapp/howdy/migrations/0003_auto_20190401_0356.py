# Generated by Django 2.1.7 on 2019-03-31 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0002_auto_20190330_1519'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='Person_name',
        ),
    ]
