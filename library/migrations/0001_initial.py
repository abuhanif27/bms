# Generated by Django 5.1.6 on 2025-03-05 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(choices=[('fic', 'Fiction'), ('nfic', 'Non-Fiction'), ('mys', 'Mystery'), ('bio', 'Biography'), ('fan', 'Fantasy'), ('sci', 'Science'), ('his', 'History')], max_length=4)),
                ('published_date', models.DateField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
