# Generated by Django 5.0.6 on 2024-10-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgDashApp', '0003_sdgindicator_sdgtarget'),
    ]

    operations = [
        migrations.AddField(
            model_name='sdgindicator',
            name='targetId',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AddField(
            model_name='sdgtarget',
            name='sdgId',
            field=models.CharField(default=1, max_length=20),
        ),
    ]