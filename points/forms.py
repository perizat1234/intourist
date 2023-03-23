from django import forms
from .models import Point,Feedback

class PointForm(forms.ModelForm):
    class Meta:
        model = Point
        fields = ['name', 'location', 'description']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields =['place', 'text']




