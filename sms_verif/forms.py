from django import forms

class Code(forms.Form):
    verif_num = forms.CharField(max_length=6)

