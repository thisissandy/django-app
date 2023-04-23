# Generated by Django 3.1.5 on 2021-04-15 21:18

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('App_1', '0002_auto_20210409_0501'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('man_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='licenseregistration',
            name='doi',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 2, 48, 48, 942973)),
        ),
        migrations.AlterField(
            model_name='rcregister',
            name='reg_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 2, 48, 48, 942973)),
        ),
        migrations.AlterField(
            model_name='vechilefine',
            name='fine',
            field=models.CharField(choices=[('select', 'select'), ('Driving without license', 'Driving without license'), ('Unauthorized use of vehicles', 'Unauthorized use of vehicles'), ('Driving without qualification', 'Driving without qualification'), ('Rash Driving', 'Rash Driving'), ('Speeding', 'Speeding'), ('Drunken Driving', 'Drunken Driving')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vechilefine',
            name='offence_on',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 2, 48, 48, 942973)),
        ),
        migrations.AlterField(
            model_name='vechilefine',
            name='paid_upto',
            field=models.DateField(default=datetime.datetime(2021, 6, 16, 2, 48, 48, 942973)),
        ),
    ]
