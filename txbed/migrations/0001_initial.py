# Generated by Django 3.2.4 on 2022-07-07 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AohsFile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=512)),
                ('extra', models.JSONField()),
            ],
        ),
    ]