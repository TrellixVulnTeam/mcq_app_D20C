# Generated by Django 2.2.7 on 2019-11-28 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0009_auto_20191128_1957'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='user',
            name='Test_Id',
        ),
    ]
