# Generated by Django 3.2.5 on 2021-07-30 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudantes',
            old_name='situação',
            new_name='situacao',
        ),
    ]
