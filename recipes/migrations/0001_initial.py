# Generated by Django 4.2.13 on 2024-06-09 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('cuisine', models.IntegerField(choices=[(0, 'International'), (1, 'Mediterranean'), (2, 'Asian'), (3, 'Middle-Eastern'), (4, 'European'), (5, 'African'), (6, 'American'), (7, 'Latin-American'), (8, 'Carribean')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('approval_status', models.IntegerField(choices=[(0, 'Not-Approved'), (1, 'Approved')], default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]