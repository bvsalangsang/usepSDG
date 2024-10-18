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