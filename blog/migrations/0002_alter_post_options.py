# Generated by Django 3.2.9 on 2021-11-19 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-titulo']},
        ),
    ]
