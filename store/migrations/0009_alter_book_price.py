# Generated by Django 4.0.2 on 2023-04-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
