# Generated by Django 3.2.13 on 2023-05-19 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('profile_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('original_language', models.CharField(max_length=10, null=True)),
                ('original_title', models.CharField(max_length=100, null=True)),
                ('overview', models.TextField(null=True)),
                ('release_date', models.DateField(null=True)),
                ('popularity', models.FloatField(null=True)),
                ('vote_count', models.IntegerField(null=True)),
                ('vote_average', models.FloatField(null=True)),
                ('poster_path', models.CharField(max_length=200, null=True)),
                ('backdrop_path', models.CharField(max_length=200, null=True)),
                ('runtime', models.IntegerField(null=True)),
                ('director', models.ManyToManyField(to='movies.Director')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('keywords', models.ManyToManyField(to='movies.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=50)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
            ],
        ),
    ]