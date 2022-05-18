# Generated by Django 3.2.13 on 2022-05-18 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banco', '0003_auto_20220517_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='fone',
            field=models.BigIntegerField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='agencia',
            name='tipo1',
            field=models.BigIntegerField(blank=True, choices=[('1', 'Fixo'), ('0', 'Celular')]),
        ),
    ]
