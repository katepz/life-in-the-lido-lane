# Generated by Django 4.2.16 on 2024-11-29 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LidoSuggestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('lido_idea', models.TextField()),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
