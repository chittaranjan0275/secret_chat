# Generated by Django 2.2.12 on 2020-08-12 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret_chat', '0014_auto_20200812_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_table',
            name='chat',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
