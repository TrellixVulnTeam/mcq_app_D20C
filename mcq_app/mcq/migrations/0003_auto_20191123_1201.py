# Generated by Django 2.2.6 on 2019-11-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcq', '0002_test_test_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='Test_Description',
            field=models.TextField(default=''),
        ),
    ]
