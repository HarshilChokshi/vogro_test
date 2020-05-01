# Generated by Django 3.0.5 on 2020-04-29 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vogro_api', '0009_delete_livegrocerypost'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveGroceryPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grocery_store_address', models.TextField()),
                ('grocery_store_address_name', models.CharField(max_length=50)),
                ('grocery_store_name', models.CharField(max_length=30)),
                ('time_of_grocery_shopping', models.DateTimeField()),
                ('grocery_item_list', models.TextField()),
                ('earliest_time', models.DateTimeField()),
                ('latest_time', models.DateTimeField()),
                ('time_of_post', models.DateTimeField()),
                ('receipt_image_ref', models.CharField(default='', max_length=100)),
                ('grocery_total_amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('state_of_volunteer', models.CharField(max_length=20)),
                ('client_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.ClientUser')),
                ('volunteer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vogro_api.VolunteerUser')),
            ],
        ),
    ]