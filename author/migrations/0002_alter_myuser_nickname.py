# Generated by Django 4.1.4 on 2022-12-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
