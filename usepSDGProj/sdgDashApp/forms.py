from django import forms
from .models import *


class SDGForms(forms.ModelForm):
    class Meta:
        model = SDGoals
        fields = ['sdgId','sdgName','description']

        widgets = {
            'sdgId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'sdgName':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
            'description':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
       }
        

class SDGTargetForms(forms.ModelForm):
    class Meta:
        model = SDGTarget
        fields = ['targetId','targetCode','targetDesc']
        widgets = {
                'targetId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
                'targetCode':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
                'targetDesc':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
        }
        

class SDGIndicatorForms(forms.ModelForm):
    class Meta:
        model = SDGIndicator
        fields = ['indId','indCode','indDesc']
        widgets = {
                'indId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
                'indCode':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
                'indDesc':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
        }
        


class SDGIndicatorForms(forms.ModelForm):
    class Meta:
        model = SDGIndicator
        fields = ['indId','indCode','indDesc']
        widgets = {
                'indId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
                'indCode':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
                'indDesc':forms.Textarea(attrs={'rows':'4', 'class':'form-control', 'style':'margin-bottom:10px'})
        }

class SustainStratForms(forms.ModelForm):
    class Meta:
        model =SustainStrat      
        fields = ['susStratId','susStratName']
        widgets = {
            'susStratId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'susStratName':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
        }

class UIGreenForms(forms.ModelForm):
    class Meta:
        model = UIGreenMetric      
        fields = ['greenMetId','greenName']
        widgets = {
            'greenMetId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'greenName':forms.TextInput(attrs={'class':'form-control', 'style':'margin-bottom:10px'}),
        }

class SDGScorecard(forms.ModelForm):
    class Meta:
        model = SDGScorecard
        fields = ['sdgScoreId','sdgInitName','sdgDesc','outputs','outcome','personnel','links']
        widgets = {
            'sdgScoreId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'sdgInitName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Initiative Name' }),
            'sdgDesc':forms.Textarea(attrs={'rows':'4', 'class':'form-control','placeholder':'Description'}),
            'outputs':forms.TextInput(attrs={'class':'form-control','placeholder':'Output'}),
            'outcome':forms.TextInput(attrs={'class':'form-control','placeholder':'Outcome'}),
            'personnel':forms.TextInput(attrs={'class':'form-control','placeholder':'Personnel'}),
            'links':forms.TextInput(attrs={'class':'form-control','placeholder':'Links'}),
   
        }


class vegetationMap(forms.ModelForm):
    class Meta:
        model = VegetationMap
        fields = ['vegId','campus','campAreaSqm','campAreaHas', 'forestVegSqm','forestVegHas', 
                  'forestVegPctTotArea', 'plantVegSqm', 'plantVegHas', 'plantVegPctTotArea', 'waterAbsSqm',
                  'waterAbsHas', 'waterAbsPctTotArea']
        
        widgets = {
            'vegId':forms.TextInput(attrs={'class':'form-control','style':'margin-bottom:10px'}),
            'campus':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Campus' }),
            'campAreaSqm':forms.TextInput(attrs={'class':'form-control','placeholder':'Campus Area (Sqm)'}),
            'campAreaHas':forms.TextInput(attrs={'class':'form-control','placeholder':'Campus Area (Has)'}),
            'forestVegSqm':forms.TextInput(attrs={'class':'form-control','placeholder':'Forest Veg. (Sqm)'}),
            'forestVegHas':forms.TextInput(attrs={'class':'form-control','placeholder':'Forest Veg. (Has)'}),
            'forestVegPctTotArea':forms.TextInput(attrs={'class':'form-control','placeholder':'Forest Veg Pct'}),
            'plantVegSqm':forms.TextInput(attrs={'class':'form-control','placeholder':'Plant Veg. (Sqm)'}),
            'plantVegHas':forms.TextInput(attrs={'class':'form-control','placeholder':'Plant Veg. (Has)'}),
            'plantVegPctTotArea':forms.TextInput(attrs={'class':'form-control','placeholder':'Plant Veg Pct'}),
            'waterAbsSqm':forms.TextInput(attrs={'class':'form-control','placeholder':'Water Abs (Sqm)'}),
            'waterAbsHas':forms.TextInput(attrs={'class':'form-control','placeholder':'Water Abs (Has)'}),
            'waterAbsPctTotArea':forms.TextInput(attrs={'class':'form-control','placeholder':'Water Abs Pct'}),
        }


