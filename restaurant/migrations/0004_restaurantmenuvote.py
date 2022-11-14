# Generated by Django 4.1.3 on 2022-11-10 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_restaurantmenu_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantMenuVote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('vote', models.IntegerField(default=0)),
                ('date', models.DateField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
                ('restaurant_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menu_vote', to='restaurant.restaurant')),
            ],
            options={
                'db_table': 'restaurant_menu_vote',
            },
        ),
    ]
