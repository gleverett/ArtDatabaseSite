# Generated by Django 3.2.9 on 2021-12-03 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artData', '0005_remove_customermodel_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='query1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
