# Generated by Django 4.0.2 on 2023-04-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_review_customer_alter_review_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='charitypoints',
            field=models.CharField(choices=[('0', '0'), ('400', '400')], max_length=10, null=True),
        ),
    ]
