# Generated by Django 5.1.1 on 2024-09-16 04:57

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0003_queryhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('earnings', models.FloatField(default=0.0)),
                ('description', models.TextField(default='Apex Engine User')),
                ('image', models.URLField(max_length=2000)),
                ('payment_method', models.CharField(max_length=500)),
                ('payment_info', models.TextField(default=' ')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
