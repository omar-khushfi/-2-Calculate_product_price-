from django import forms
from .models import *
class productform(forms.ModelForm):
    class Meta:
        model=Product;
        fields=[
            'name',
             'selling_price',
             'image',
        ]
        widgets= {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'selling_price':forms.NumberInput(attrs={'class':'form-control'}),
        'image':forms.FileInput(attrs={'class':'form-control'}),
        }
        
class materialform(forms.ModelForm):
    class Meta:
        model=Material;
        fields=[
            'name',
             'price', 
        ]
        widgets= {
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'price':forms.NumberInput(attrs={'class':'form-control'}),
        }
        

class conform(forms.ModelForm):
    
    class Meta:
        model=Con;
        queryset=Material.objects.all()
        fields=[
            'material', 
            'weight',
        ]
        widgets= {
        'material': forms.Select(attrs={'class': 'form-control','id':'materialid'},choices=queryset),
        'weight':forms.NumberInput(attrs={'class':'form-control','id':'weightid'}),
        
        }
        
        

