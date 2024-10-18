from django.db import models

# Create your models here.

#Goals
class SDGoals(models.Model):
    sdgId = models.AutoField(primary_key=True, editable=True)
    sdgName = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    isActive = models.CharField(max_length=1, default='Y') 

    class Meta:
        db_table = "man_sdg"


class SDGTarget(models.Model):
    targetId = models.AutoField(primary_key=True, editable=True)
    sdgId = models.CharField(max_length=20,default=1)
    targetCode = models.CharField(max_length=50)
    targetDesc = models.CharField(max_length=800)
    isActive = models.CharField(max_length=1,default='Y')

    class Meta:
        db_table = "man_sdg_target"


class SDGIndicator(models.Model):
    indId = models.AutoField(primary_key=True, editable=True)
    targetId = models.CharField(max_length=20,default=1)
    indCode = models.CharField(max_length=50)
    indDesc = models.CharField(max_length=800)
    isActive = models.CharField(max_length=1,default='Y')

    class Meta:
        db_table = "man_sdg_indicator"


#sustain strategic
class SustainStrat(models.Model):
    susStratId = models.AutoField(primary_key=True, editable=True)
    susStratName = models.CharField(max_length=500)
    isActive = models.CharField(max_length=1,default='Y')

    class Meta:
        db_table = "man_sustian_strat"

#Green Metric    
class UIGreenMetric(models.Model):
    greenMetId = models.AutoField(primary_key=True, editable=True)
    greenName = models.CharField(max_length=250)
    isActive = models.CharField(max_length=1,default='Y') 

    class Meta:
        db_table = "man_green_metric"

class SDGScorecard(models.Model):
    sdgScoreId = models.AutoField(primary_key=True,editable=True)
    susStratId = models.CharField(max_length=20)
    greenMetId = models.CharField(max_length=20)
    sdgInitName = models.CharField(max_length=800)  
    sdgImpYear = models.CharField(max_length=10)
    sdgDesc = models.CharField(max_length=1024)
    outputs = models.CharField(max_length=500)
    outcome = models.CharField(max_length=500)
    personnel = models.CharField(max_length=255)
    links = models.CharField(max_length=850)
    isActive = models.CharField(max_length=1,default='Y') 

    class Meta: 
        db_table = "sdg_scorecard"

class SDGScorecardDet(models.Model):
    ctr = models.AutoField(primary_key=True, editable=True)
    sdgScoreId = models.CharField(max_length=10)
    sdgId = models.CharField(max_length=20)
    targetId = models.CharField(max_length=20)
    indId = models.CharField(max_length=20)
    class Meta: 
        db_table = "sdg_scorecard_det"

