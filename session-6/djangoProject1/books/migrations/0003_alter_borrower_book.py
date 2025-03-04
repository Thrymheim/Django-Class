# Generated by Django 5.1.5 on 2025-02-02 14:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_borrower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
