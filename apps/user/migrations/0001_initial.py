# Generated by Django 4.1.1 on 2022-10-17 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mailing_address', models.CharField(max_length=200)),
                ('billing_address', models.CharField(max_length=200)),
                ('star_points', models.FloatField(default=0, max_length=200)),
                ('preferred_payment_method', models.IntegerField(blank=True, choices=[(1, 'cash'), (2, 'credit card'), (3, 'check')], null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
