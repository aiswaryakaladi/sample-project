# Generated by Django 4.1.4 on 2023-01-26 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0005_applymodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='applymodel',
            name='company',
            field=models.CharField(default='exit', max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='applymodel',
            name='title',
            field=models.CharField(default='title', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applymodel',
            name='fname',
            field=models.CharField(max_length=40),
        ),
    ]
