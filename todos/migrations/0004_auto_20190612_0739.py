# Generated by Django 2.2.1 on 2019-06-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_auto_20190612_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='amount',
            field=models.IntegerField(default='3'),
        ),
    ]
