# Generated by Django 4.2.3 on 2023-07-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodeNo', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('Age', models.IntegerField()),
                ('Salary', models.IntegerField()),
                ('Address', models.CharField(max_length=150)),
                ('Work', models.CharField(max_length=50)),
            ],
        ),
    ]
