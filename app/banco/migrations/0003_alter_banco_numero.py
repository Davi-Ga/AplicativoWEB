# Generated by Django 3.2.13 on 2022-06-01 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0002_alter_agencia_fone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banco',
            name='numero',
            field=models.CharField(blank=True, max_length=250, unique=True),
        ),
    ]