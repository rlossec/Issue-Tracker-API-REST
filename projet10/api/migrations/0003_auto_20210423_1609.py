# Generated by Django 3.2 on 2021-04-23 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_persmission_contributor_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='permission',
            field=models.CharField(choices=[('not allowed', 'not allowed'), ('allowed', 'allowed')], max_length=128),
        ),
        migrations.AlterField(
            model_name='project',
            name='type',
            field=models.CharField(choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('iOS', 'iOS'), ('Android', 'Android')], max_length=128),
        ),
    ]