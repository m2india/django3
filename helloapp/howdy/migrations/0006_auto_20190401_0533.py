# Generated by Django 2.1.7 on 2019-04-01 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0005_person_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]