# Generated by Django 3.1.2 on 2021-03-22 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_article_category_project_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
