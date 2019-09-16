from django import forms
from .models import Review


class AddReviewForm(forms.Form):
    text = forms.CharField(max_length=1000)

    def save(self):
        new_review = Review.objects.create(text=self.cleaned_data['text'])
        return new_review
