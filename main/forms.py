from django import forms
from .models import Review


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating', 'product', 'user']

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
        }

    text = forms.CharField(max_length=1000)
    text.widget.attrs.update({'class': 'form-control'})
