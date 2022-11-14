# Generated by Django 4.1.3 on 2022-11-11 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_restaurantmenuvote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantmenuvote',
            name='restaurant_id',
        ),
        migrations.AddField(
            model_name='restaurantmenuvote',
            name='restaurant_menu_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menu_vote', to='restaurant.restaurantmenu'),
        ),
        migrations.AlterField(
            model_name='uservoterestaurantmenu',
            name='restaurant_menu_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menu_user', to='restaurant.restaurantmenu'),
        ),
    ]