# Generated by Django 3.2 on 2021-04-29 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_usermodel_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='hash',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
