# Generated by Django 3.2.7 on 2021-09-17 01:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]