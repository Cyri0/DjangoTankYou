# Generated by Django 3.2.2 on 2021-05-11 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tank_api', '0003_remove_tankevent_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TankEvent',
        ),
    ]
