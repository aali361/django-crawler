# Generated by Django 3.0.5 on 2020-08-28 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0015_page_telegram_channel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='telegram_channel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
