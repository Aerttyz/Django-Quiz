# Generated by Django 5.0.6 on 2024-05-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
