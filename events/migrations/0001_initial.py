# Generated by Django 3.2.8 on 2021-10-17 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Aircraft', '0003_auto_20211017_0033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(blank=True, max_length=100)),
                ('event_date', models.DateField(blank=True, null=True)),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('event_date_end', models.DateField(blank=True, null=True)),
                ('lives_saved', models.IntegerField(blank=True)),
                ('aircraft', models.ManyToManyField(blank=True, to='Aircraft.Aircraft')),
            ],
        ),
    ]
