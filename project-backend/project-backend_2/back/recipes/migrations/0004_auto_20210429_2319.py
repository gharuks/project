# Generated by Django 3.1.7 on 2021-04-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210429_1820'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]