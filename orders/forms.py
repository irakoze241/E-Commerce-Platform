from django import forms


class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'John Doe',
            'id': 'id_full_name',
        })
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': '123 Main Street, City, Country',
            'id': 'id_address',
        })
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+1 234 567 8900',
            'id': 'id_phone',
        })
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()
        if len(phone) < 7:
            raise forms.ValidationError('Enter a valid phone number.')
        return phone
