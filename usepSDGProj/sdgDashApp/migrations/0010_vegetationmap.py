# Generated by Django 5.0.6 on 2024-11-27 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sdgDashApp', '0009_sdgscorecarddet_isactive_alter_sdgscorecarddet_indid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VegetationMap',
            fields=[
                ('vegId', models.AutoField(primary_key=True, serialize=False)),
                ('campus', models.CharField(max_length=50)),
                ('campAreaSqm', models.CharField(max_length=30)),
                ('campAreaHas', models.CharField(max_length=30)),
                ('forestVegSqm', models.CharField(max_length=30)),
                ('forestVegHas', models.CharField(max_length=30)),
                ('forestVegPctTotArea', models.CharField(max_length=30)),
                ('plantVegSqm', models.CharField(max_length=30)),
                ('plantVegHas', models.CharField(max_length=30)),
                ('plantVegPctTotArea', models.CharField(max_length=30)),
                ('waterAbsSqm', models.CharField(max_length=30)),
                ('waterAbsHas', models.CharField(max_length=30)),
                ('waterAbsPctTotArea', models.CharField(max_length=30)),
                ('isActive', models.CharField(default='Y', max_length=1)),
            ],
            options={
                'db_table': 'man_vegetation_map',
            },
        ),
    ]