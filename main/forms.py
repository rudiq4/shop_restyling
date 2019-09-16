from django import forms
from .models import Review


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']

        widgets = {'text': forms.TextInput(attrs={'class': 'form-control'})}

    text = forms.CharField(max_length=1000)
    text.widget.attrs.update({'class': 'form-control'})

