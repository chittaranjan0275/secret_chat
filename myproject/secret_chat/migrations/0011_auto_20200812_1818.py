# Generated by Django 2.2.12 on 2020-08-12 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret_chat', '0010_auto_20200812_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_table',
            name='chat',
            field=models.CharField(max_length=1000),
        ),
    ]