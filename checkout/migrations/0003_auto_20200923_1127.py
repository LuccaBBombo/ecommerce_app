# Generated by Django 3.1 on 2020-09-23 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20200922_1741'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='city',
            new_name='town_or_city',
        ),
    ]