"""Forms of the project."""
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput(attrs={'min': 0, 'max': 100}),

        }

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 0 or quantity > 100:
            raise forms.ValidationError("Quantity must be between 0 and 100")
        return quantity
# Create your forms here.
