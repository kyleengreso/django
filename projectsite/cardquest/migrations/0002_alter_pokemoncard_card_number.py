# Generated by Django 4.2.7 on 2023-12-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncard',
            name='card_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
