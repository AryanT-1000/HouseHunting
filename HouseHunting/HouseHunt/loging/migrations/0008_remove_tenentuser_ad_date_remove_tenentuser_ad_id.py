# Generated by Django 4.1.1 on 2022-09-11 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loging', '0007_rename_admin_tenentadmin_rename_user_tenentuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tenentuser',
            name='ad_date',
        ),
        migrations.RemoveField(
            model_name='tenentuser',
            name='ad_id',
        ),
    ]
