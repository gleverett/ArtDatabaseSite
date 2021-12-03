# Generated by Django 3.2.9 on 2021-12-03 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artData', '0002_auto_20211127_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('street_num', models.IntegerField()),
                ('street_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('age', models.IntegerField()),
                ('art_medium', models.CharField(max_length=50)),
                ('art_style', models.CharField(max_length=50)),
                ('art_type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ArtShowModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.TimeField()),
                ('street_num', models.IntegerField()),
                ('street_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BuyerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('street_num', models.IntegerField()),
                ('street_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('phone_num', models.CharField(max_length=25)),
                ('num_purchase', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CollectorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('collector_id', models.IntegerField()),
                ('collection_type', models.CharField(max_length=50)),
                ('collection_style', models.CharField(max_length=50)),
                ('collection_medium', models.CharField(max_length=50)),
                ('street_num', models.IntegerField()),
                ('street_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('phone_num', models.CharField(max_length=50)),
                ('artist_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RenterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('renter_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('street_num', models.IntegerField()),
                ('street_name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('phone_num', models.CharField(max_length=25)),
                ('num_rents', models.IntegerField()),
            ],
        ),
    ]
