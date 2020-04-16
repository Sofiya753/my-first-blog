# Generated by Django 2.2.12 on 2020-04-14 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('author', models.CharField(max_length=120)),
                ('location', models.CharField(max_length=120)),
                ('date', models.DateTimeField()),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
