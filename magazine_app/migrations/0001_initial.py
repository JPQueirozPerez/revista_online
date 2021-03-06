# Generated by Django 3.0.5 on 2020-04-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagazineApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Título')),
                ('slug', models.SlugField(verbose_name='Atajo')),
                ('synopsis', models.TextField(verbose_name='Sinopsis')),
                ('author', models.CharField(max_length=120, verbose_name='Autor')),
                ('genre', models.CharField(max_length=120, verbose_name='Género')),
            ],
            options={
                'verbose_name': 'Historia',
                'verbose_name_plural': 'Historias',
                'ordering': ['title'],
            },
        ),
    ]
