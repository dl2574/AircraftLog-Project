# Generated by Django 3.2.8 on 2021-10-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discrepancies', '0003_auto_20211016_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discrepancy',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]
