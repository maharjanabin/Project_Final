# Generated by Django 3.1.7 on 2021-05-02 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisementpost',
            old_name='thumbnail',
            new_name='poster',
        ),
    ]