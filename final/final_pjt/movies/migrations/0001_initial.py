# Generated by Django 2.2.6 on 2020-06-12 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Production_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Production_country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget', models.FloatField()),
                ('movie_id', models.IntegerField()),
                ('overview', models.TextField()),
                ('popularity', models.FloatField()),
                ('poster_path', models.TextField()),
                ('production_companies', models.TextField()),
                ('production_countries', models.TextField()),
                ('release_date', models.CharField(max_length=30)),
                ('revenue', models.IntegerField()),
                ('runtime', models.IntegerField()),
                ('spoken_language', models.CharField(max_length=30)),
                ('tagline', models.TextField()),
                ('title', models.TextField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('genre', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
    ]
