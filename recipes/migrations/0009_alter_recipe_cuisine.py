# Generated by Django 4.2.13 on 2024-07-15 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_alter_recipe_cuisine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.IntegerField(choices=[(0, 'Mediterranean'), (1, 'Asian'), (2, 'Middle-Eastern'), (3, 'European'), (4, 'African'), (5, 'American'), (6, 'Latin-American'), (7, 'Caribbean'), (8, 'Desserts')], default=0),
        ),
    ]