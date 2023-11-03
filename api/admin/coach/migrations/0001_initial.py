# Generated by Django 4.2.7 on 2023-11-03 19:25

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
            ],
            options={
                'verbose_name': 'Admin Coach',
                'verbose_name_plural': 'Admin Coaches',
                'ordering': ['name'],
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('database.coach',),
        ),
    ]
