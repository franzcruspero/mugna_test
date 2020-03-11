# Generated by Django 3.0.4 on 2020-03-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('normal', 'Normal'), ('fighting', 'Fighting'), ('flying', 'Flying'), ('poison', 'Poison'), ('ground', 'Ground'), ('rock', 'Rock'), ('bug', 'Bug'), ('ghost', 'Ghost'), ('steel', 'Steel'), ('fire', 'Fire'), ('water', 'Water'), ('grass', 'Grass'), ('electric', 'Electric'), ('psychic', 'Psychic'), ('ice', 'Ice'), ('dragon', 'Dragon'), ('dark', 'Dark'), ('fairy', 'Fairy')], max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('weight', models.IntegerField(null=True)),
                ('description', models.TextField(blank=True, max_length=300, null=True)),
                ('image_url', models.CharField(blank=True, max_length=100, null=True)),
                ('evolution_id', models.IntegerField(null=True)),
                ('speed', models.IntegerField(null=True)),
                ('special_defense', models.IntegerField(null=True)),
                ('special_attack', models.IntegerField(null=True)),
                ('defense', models.IntegerField(null=True)),
                ('attack', models.IntegerField(null=True)),
                ('hp', models.IntegerField(null=True)),
                ('abilities', models.ManyToManyField(to='pokedex.Ability')),
                ('types', models.ManyToManyField(to='pokedex.Type')),
            ],
        ),
    ]