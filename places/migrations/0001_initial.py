# Generated by Django 3.2 on 2021-04-09 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(help_text='Enter the description of this place..', max_length=3000)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=100)),
                ('type_of_place', models.CharField(max_length=100)),
            ],
        ),
    ]
