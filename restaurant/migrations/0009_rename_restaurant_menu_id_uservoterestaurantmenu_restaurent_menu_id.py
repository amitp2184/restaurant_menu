# Generated by Django 4.1.3 on 2022-11-13 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_restaurantmenu_vote'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uservoterestaurantmenu',
            old_name='restaurant_menu_id',
            new_name='restaurent_menu_id',
        ),
    ]
