# Generated by Django 4.1.1 on 2022-09-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loging', '0009_delete_tenentadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenentuser',
            name='phone1',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='tenentuser',
            name='phone2',
            field=models.IntegerField(max_length=10),
        ),
    ]
