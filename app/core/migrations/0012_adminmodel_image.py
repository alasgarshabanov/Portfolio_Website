# Generated by Django 3.1.2 on 2021-03-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210323_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminmodel',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
