# Generated by Django 3.2.9 on 2021-11-26 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20211122_0621'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartproduct',
            old_name='qtr',
            new_name='qty',
        ),
    ]
