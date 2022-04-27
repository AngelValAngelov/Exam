from django import forms
from django.views import View


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = ''
            field.widget.attrs['class'] += ' form-control'


class DisabledFieldsFormMixin:
    disabled_fields = '__all__'
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != '__all__' and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, 'attrs'):
                setattr(field.widget, 'attrs', {})
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs['disabled'] = 'readonly'
            else:
                field.widget.attrs['readonly'] = 'readonly'

class PostOnlyView(View):
    form_class = None

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass