# Generated by Django 5.0.6 on 2024-12-06 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgDashApp', '0010_vegetationmap'),
    ]

    operations = [
        migrations.CreateModel(
            name='sdgPolicies',
            fields=[
                ('sdgPolId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('imgPath', models.CharField(max_length=500)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'man_sdg_policy',
            },
        ),
    ]
