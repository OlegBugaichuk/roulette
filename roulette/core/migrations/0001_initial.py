# Generated by Django 3.1.3 on 2020-11-09 05:50

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
                ('title', models.CharField(max_length=30, verbose_name='title')),
                ('image', models.ImageField(upload_to='img/items/', verbose_name='image')),
                ('number', models.PositiveIntegerField(verbose_name='number')),
                ('visible', models.BooleanField(default=True, verbose_name='visible')),
            ],
        ),
    ]
