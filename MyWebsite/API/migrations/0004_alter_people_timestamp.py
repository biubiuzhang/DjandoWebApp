# Generated by Django 4.1.2 on 2022-10-16 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0003_alter_people_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
