# Generated by Django 5.1.1 on 2024-09-18 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_register', '0002_delete_contact'),
        ('database', '0003_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
            ],
            options={
                'verbose_name': 'Client Register',
                'verbose_name_plural': 'Client Registrations',
                'proxy': True,
                'default_permissions': (),
                'indexes': [],
                'constraints': [],
            },
            bases=('database.register',),
        ),
    ]
