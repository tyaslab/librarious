# Generated by Django 2.1.3 on 2019-01-07 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('librarious', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Borrow',
            new_name='Borrowing',
        ),
    ]
