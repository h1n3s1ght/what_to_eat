# Generated by Django 4.0.6 on 2022-07-19 16:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_recipe_recipedateadded_recipe_recipedateupdated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='RecipeDateUpdated',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 16, 2, 55, 348691, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='UserDateAdded',
            field=models.DateField(default=datetime.datetime(2022, 7, 19, 16, 2, 55, 408616, tzinfo=utc)),
        ),
    ]
