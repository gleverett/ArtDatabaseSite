# Generated by Django 3.2.9 on 2021-12-03 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artData', '0013_query3_query4_query5_query6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artworkmodel',
            name='type',
        ),
    ]
