# Generated by Django 5.2.1 on 2025-05-24 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_users_email_alter_users_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
