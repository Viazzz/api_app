# Generated by Django 5.0.4 on 2024-05-16 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TblForWrite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wr_id', models.IntegerField(max_length=400)),
                ('wr_created', models.DateTimeField(auto_now_add=True)),
                ('wr_modified', models.DateTimeField(auto_now=True)),
                ('wr_body', models.TextField()),
            ],
        ),
    ]
