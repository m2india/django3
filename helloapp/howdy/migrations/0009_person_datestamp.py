# Generated by Django 2.1.7 on 2019-04-01 00:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('howdy', '0008_auto_20190401_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='datestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
