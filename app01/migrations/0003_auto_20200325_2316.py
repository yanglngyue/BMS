# Generated by Django 2.1.1 on 2020-03-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200325_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='kprice_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='kprice_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='company',
            name='remove_date',
            field=models.DateTimeField(),
        ),
    ]
