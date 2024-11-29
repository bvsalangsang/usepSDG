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
    sdgImpYear = models.IntegerField()
    sdgDesc = models.CharField(max_length=1024)
    outputs = models.CharField(max_length=500)
    outcome = models.CharField(max_length=500)
    personnel = models.CharField(max_length=255)
    links = models.CharField(max_length=850)
    enCodedBy = models.CharField(max_length=10,null=True, blank=True)
    enCodedDate = models.DateField(null=True, blank=True)
    isActive = models.CharField(max_length=1,default='Y') 

    class Meta: 
        db_table = "sdg_scorecard"

class SDGScorecardDet(models.Model):
    ctr = models.AutoField(primary_key=True, editable=True)
    sdgScoreId = models.CharField(max_length=10)
    sdgId = models.CharField(max_length=50)
    targetId = models.CharField(max_length=100)
    indId = models.CharField(max_length=120)
    isActive = models.CharField(max_length=1,default='Y') 
    
    class Meta: 
        db_table = "sdg_scorecard_det"


#Vegetation Map 
class VegetationMap(models.Model):
    vegId = models.AutoField(primary_key=True, editable=True)
    campus = models.CharField(max_length=50)
    campAreaSqm  = models.CharField(max_length=30)
    campAreaHas  = models.CharField(max_length=30)
    forestVegSqm  = models.CharField(max_length=30)
    forestVegHas  = models.CharField(max_length=30)
    forestVegPctTotArea  = models.CharField(max_length=30)   
    plantVegSqm  = models.CharField(max_length=30)
    plantVegHas  = models.CharField(max_length=30)
    plantVegPctTotArea  = models.CharField(max_length=30)    
    waterAbsSqm  = models.CharField(max_length=30)
    waterAbsHas  = models.CharField(max_length=30)
    waterAbsPctTotArea  = models.CharField(max_length=30)   
    isActive = models.CharField(max_length=1,default='Y') 

    class Meta: 
        db_table = "man_vegetation_map"
