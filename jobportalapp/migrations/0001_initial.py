# Generated by Django 4.1.4 on 2022-12-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='regmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('cpassword', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=25)),
            ],
        ),
    ]
