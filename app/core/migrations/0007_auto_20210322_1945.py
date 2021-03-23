# Generated by Django 3.1.2 on 2021-03-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210322_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminmodel',
            name='skill',
        ),
        migrations.AddField(
            model_name='adminmodel',
            name='skill',
            field=models.ManyToManyField(related_name='skill', to='core.Skill'),
        ),
    ]
