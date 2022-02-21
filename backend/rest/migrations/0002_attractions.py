# Generated by Django 4.0 on 2022-02-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attractions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.CharField(max_length=100)),
                ('loc', models.CharField(max_length=200)),
                ('website', models.URLField(max_length=500)),
                ('open_time', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('reviews', models.IntegerField()),
                ('star_rating', models.DecimalField(decimal_places=5, max_digits=10)),
            ],
        ),
    ]