# Generated by Django 3.2.8 on 2021-10-23 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discrepancies', '0009_alter_discrepancy_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discrepancy',
            options={'ordering': ['-date_resolved', '-occurrences', '-date_discovered']},
        ),
    ]