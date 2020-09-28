from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='image', required=True, widget=CustomClearableFileInput)

    def ___ini__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_name
