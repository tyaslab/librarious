# Generated by Django 2.1.3 on 2019-01-08 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarious', '0008_worldborder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worldborder',
            old_name='mpoly',
            new_name='geom',
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='fips',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='iso2',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='iso3',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='pop2005',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='region',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='subregion',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='un',
            field=models.IntegerField(),
        ),
    ]
