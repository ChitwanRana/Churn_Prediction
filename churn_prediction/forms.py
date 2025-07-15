from django import forms

class CustomerForm(forms.Form):
    gender = forms.ChoiceField(
        choices=[('Female', 'Female'), ('Male', 'Male')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    senior_citizen = forms.ChoiceField(
        choices=[(0, 'No'), (1, 'Yes')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    partner = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    dependents = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tenure = forms.IntegerField(
        min_value=0, max_value=100,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Months'})
    )
    phone_service = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    multiple_lines = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No phone service', 'No phone service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    internet_service = forms.ChoiceField(
        choices=[('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    online_security = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    online_backup = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    device_protection = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    tech_support = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    streaming_tv = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    streaming_movies = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No'), ('No internet service', 'No internet service')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    contract = forms.ChoiceField(
        choices=[('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    paperless_billing = forms.ChoiceField(
        choices=[('Yes', 'Yes'), ('No', 'No')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    payment_method = forms.ChoiceField(
        choices=[
            ('Electronic check', 'Electronic check'),
            ('Mailed check', 'Mailed check'),
            ('Bank transfer (automatic)', 'Bank transfer (automatic)'),
            ('Credit card (automatic)', 'Credit card (automatic)')
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    monthly_charges = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monthly charges in $'})
    )
    total_charges = forms.FloatField(
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Total charges in $'})
    )