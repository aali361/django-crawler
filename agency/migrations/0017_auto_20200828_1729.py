# Generated by Django 3.0.5 on 2020-08-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0016_auto_20200828_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='load_sleep',
            field=models.IntegerField(default=4),
        ),
        migrations.AlterField(
            model_name='page',
            name='crawl_interval',
            field=models.IntegerField(default=2),
        ),
    ]
