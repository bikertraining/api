# Generated by Django 5.1.1 on 2024-09-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_register_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='contact',
        ),
        migrations.AddField(
            model_name='register',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='amount',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='city',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='class_type',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='coupon_code',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='credit_card_number',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='dln',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='dls',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='dob',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='email',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='first_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='last_name',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='phone',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='schedule_date',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='schedule_day',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='state',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='xpl',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='zipcode',
            field=models.TextField(null=True),
        ),
    ]
