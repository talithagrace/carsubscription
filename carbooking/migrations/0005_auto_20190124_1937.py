# Generated by Django 2.1.5 on 2019-01-24 19:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carbooking', '0004_auto_20190124_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='end_date',
            field=models.DateField(null=True, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='booking',
            name='start_date',
            field=models.DateField(null=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(null=True, verbose_name='end'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(null=True, verbose_name='start'),
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('driver', 'car', 'start_time', 'end_time', 'start_date', 'end_date')},
        ),
    ]