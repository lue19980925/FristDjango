# Generated by Django 3.0.8 on 2020-07-31 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookApp', '0003_auto_20200730_0739'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name_plural': '图书管理'},
        ),
        migrations.AlterModelOptions(
            name='hero',
            options={'verbose_name_plural': '人物管理'},
        ),
    ]
