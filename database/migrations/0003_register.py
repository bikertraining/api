# Generated by Django 5.1.1 on 2024-09-18 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.JSONField(max_length=255)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register_schedule', to='database.schedule', verbose_name='Schedule')),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registration',
                'db_table': 'register',
                'default_permissions': (),
            },
        ),
    ]
