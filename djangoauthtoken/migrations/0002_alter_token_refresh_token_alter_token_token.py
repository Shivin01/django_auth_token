# Generated by Django 5.0.3 on 2024-03-12 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoauthtoken', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='refresh_token',
            field=models.CharField(max_length=511),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=511),
        ),
    ]