# Generated by Django 2.1.5 on 2019-01-24 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('inventory', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]