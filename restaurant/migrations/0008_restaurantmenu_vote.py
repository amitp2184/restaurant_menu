# Generated by Django 4.1.3 on 2022-11-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_uservoterestaurantmenu_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantmenu',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
