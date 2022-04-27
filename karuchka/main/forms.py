from datetime import date

from django import forms

from karuchka.common.helpers import BootstrapFormMixin, DisabledFieldsFormMixin
from karuchka.main.models import Vehicle
from karuchka.common.validators import MaxDateValidator


class CreateVehicleForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        vehicle = super().save(commit=False)

        vehicle.user = self.user
        if commit:
            vehicle.save()

        return vehicle

    class Meta:
        model = Vehicle
        exclude = ('user',)
        widgets = {
            'manufacturer': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
        }

    def clean_manufacturer_date(self):
        MaxDateValidator(date.today())(self.cleaned_data['manufacturer_date'])
        return self.cleaned_data['manufacturer_date']


class EditVehicleForm(BootstrapFormMixin, forms.ModelForm):
    MIN_DATE_OF_BIRTH = date(1920, 1, 1)
    MAX_DATE_OF_BIRTH = date.today()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def clean_manufacturer_date(self):
        MaxDateValidator(date.today())(self.cleaned_data['manufacturer_date'])
        return self.cleaned_data['manufacturer_date']

    class Meta:
        model = Vehicle
        exclude = ('user_profile',)


class DeleteVehicleForm(BootstrapFormMixin, DisabledFieldsFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self._init_disabled_fields()

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Vehicle
        exclude = ('user_profile',)

