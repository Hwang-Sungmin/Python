# Generated by Django 2.2.7 on 2019-11-14 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_auto_20191114_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boards',
            old_name='created_by',
            new_name='creator',
        ),
    ]
