# Generated by Django 2.1.1 on 2020-03-27 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_remove_company_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComDepart',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.ComDepart'),
        ),
    ]
