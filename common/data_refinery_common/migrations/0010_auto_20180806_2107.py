# Generated by Django 2.0.2 on 2018-08-06 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data_refinery_common', '0009_auto_20180802_1758'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='processor',
            unique_together={('name', 'version', 'docker_image', 'environment')},
        ),
    ]