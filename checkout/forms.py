from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """Creates form model for the checkout page"""
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'street_address1',
                  'street_address2', 'city', 'postcode', 'county', 'country')

    def __init__(self, *args, **kwargs):
        """
        *** Code taken from Code Institute Lesson ***

        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'city': 'City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False