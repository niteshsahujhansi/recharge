# Generated by Django 4.1.1 on 2022-12-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internet',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('net', models.CharField(max_length=40)),
                ('vald', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
    ]
