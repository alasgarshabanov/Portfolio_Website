# Generated by Django 3.1.2 on 2021-03-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_adminmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminmodel',
            name='skill',
            field=models.IntegerField(verbose_name='Skill'),
        ),
    ]
