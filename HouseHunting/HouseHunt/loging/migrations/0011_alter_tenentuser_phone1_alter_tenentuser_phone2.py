# Generated by Django 4.1.1 on 2022-09-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loging', '0010_alter_tenentuser_phone1_alter_tenentuser_phone2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenentuser',
            name='phone1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tenentuser',
            name='phone2',
            field=models.IntegerField(),
        ),
    ]
