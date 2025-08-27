# forms.py
from django import forms
from django import forms
from .models import IndividualDev, Registration

# -----------------------------
# Step 1 Form (company details)
# Form to create a new registration
# -----------------------------
class Step1Form(forms.Form):
    company_name = forms.CharField(max_length=255, required=True)
    stage = forms.ChoiceField(choices=[
        ('Sole Proprietorship', 'Sole Proprietorship'),
        ('Limited Liability Company (LLC)', 'Limited Liability Company (LLC)'),
        ('Limited Liability Partnership (LLP)', 'Limited Liability Partnership (LLP)')
    ], required=True)
    official_email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    registration_number = forms.CharField(max_length=255, required=True)
    contact_person = forms.CharField(max_length=255, required=True)
    date_of_establishment = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    physical_address = forms.CharField(widget=forms.Textarea, required=True)

    def clean_company_name(self):
        company_name = self.cleaned_data.get("company_name", "").strip()
        if Registration.objects.filter(company_name__iexact=company_name).exists():
            raise forms.ValidationError(
                f"A company with the name '{company_name}' already exists."
            )
        return company_name


# -----------------------------
# Step 2 Form (extra details)
# Form to create a new registration
# -----------------------------
class Step2Form(forms.Form):
    tax_identification_number = forms.CharField(max_length=100, required=True)
    employees = forms.IntegerField(min_value=1, required=True)
    business_model = forms.ChoiceField(choices=[
        ('B2B', 'B2B'),
        ('B2C', 'B2C'),
        ('SaaS', 'SaaS'),
        ('Marketplace', 'Marketplace')
    ], required=True)
    company_description = forms.CharField(widget=forms.Textarea, required=True)
    nature = forms.ChoiceField(choices=[
        ('Software Development', 'Software Development'),
        ('Web Services', 'Web Services'),
        ('Mobile Apps', 'Mobile Apps'),
        ('Desktop Apps', 'Desktop Apps'),
        ('IoT Apps', 'IoT Apps')
    ])
    specialization = forms.CharField(max_length=255, required=True)
    sector = forms.CharField(max_length=100, required=True)
    website = forms.URLField(required=False)


# -----------------------------
# Individual Developer Form
# Form to create a new individual developer
# -----------------------------
class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualDev
        exclude = ['user']
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'second_name': forms.TextInput(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'mail': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name", "").strip()
        second_name = cleaned_data.get("second_name", "").strip()

        if first_name and second_name:
            exists = IndividualDev.objects.filter(
                first_name__iexact=first_name,
                second_name__iexact=second_name
            )
            if self.instance.pk:  # exclude self when editing
                exists = exists.exclude(pk=self.instance.pk)

            if exists.exists():
                raise forms.ValidationError(
                    f"A developer with the name {first_name} {second_name} already exists."
                )

        return cleaned_data

# Form for filtering statistics
class StatisticsFilterForm(forms.Form):
    start_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    end_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    sector = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. HealthTech', 'class': 'form-control'})
    )
    industry = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'e.g. Fintech', 'class': 'form-control'})
    )



from django import forms
from .models import IndividualDev, Registration

# Form to edit an existing individual developer
class IndividualDevForm(forms.ModelForm):
    class Meta:
        model = IndividualDev
        fields = ["first_name", "second_name", "id_number", "industry", "nature"]

# Form to edit an existing registration
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = [
            "company_name", "stage", "official_email", "phone_number", 
            "registration_number", "contact_person", "date_of_establishment", 
            "tax_identification_number", "employees", "company_description",
            "nature", "specialization", "sector", "business_model", "website"
        ]
