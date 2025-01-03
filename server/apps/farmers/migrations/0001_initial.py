# Generated by Django 5.1.3 on 2024-11-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('farmerId', models.AutoField(primary_key=True, serialize=False)),
                ('farmName', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('farmType', models.CharField(max_length=50)),
                ('certifications', models.TextField(blank=True, null=True)),
                ('verificationStatus', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'tblFarmer',
            },
        ),
    ]
