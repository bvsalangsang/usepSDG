# Generated by Django 5.0.6 on 2024-10-17 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgDashApp', '0005_alter_sdgindicator_inddesc_alter_sdgoals_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDGScorecard',
            fields=[
                ('sdgScoreId', models.AutoField(primary_key=True, serialize=False)),
                ('susStratId', models.CharField(max_length=20)),
                ('greenMetId', models.CharField(max_length=20)),
                ('sdgInitName', models.CharField(max_length=800)),
                ('sdgImpYear', models.CharField(max_length=10)),
                ('sdgDesc', models.CharField(max_length=1024)),
                ('outputs', models.CharField(max_length=500)),
                ('outcome', models.CharField(max_length=500)),
                ('personnel', models.CharField(max_length=255)),
                ('links', models.CharField(max_length=850)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'sdg_scorecard',
            },
        ),
        migrations.CreateModel(
            name='SDGScorecardDet',
            fields=[
                ('ctr', models.AutoField(primary_key=True, serialize=False)),
                ('sdgScoreId', models.CharField(max_length=10)),
                ('sdgId', models.CharField(max_length=20)),
                ('targetId', models.CharField(max_length=20)),
                ('indId', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'sdg_scorecard_det',
            },
        ),
        migrations.CreateModel(
            name='SustainStrat',
            fields=[
                ('susStratId', models.AutoField(primary_key=True, serialize=False)),
                ('susStratName', models.CharField(max_length=500)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'man_sustian_strat',
            },
        ),
        migrations.CreateModel(
            name='UIGreenMetric',
            fields=[
                ('greenMetId', models.AutoField(primary_key=True, serialize=False)),
                ('greeName', models.CharField(max_length=250)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'man_green_metric',
            },
        ),
    ]
