# Generated by Django 3.2.9 on 2021-12-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artData', '0006_query1'),
    ]

    operations = [
        migrations.AddField(
            model_name='customermodel',
            name='customer_id',
            field=models.IntegerField(default=100000),
            preserve_default=False,
        ),
    ]
