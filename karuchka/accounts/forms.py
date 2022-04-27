from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.contrib.auth.forms import AuthenticationForm
# from petstagram.common.models import Comment
# from django.contrib.auth.models import User


from karuchka.accounts.models import Profile
from karuchka.common.helpers import BootstrapFormMixin
from django.contrib.auth import get_user_model

from karuchka.main.models import Comment

User = get_user_model()


class LoginForm(BootstrapFormMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    email = forms.EmailField()

    picture = forms.ImageField()
    description = forms.CharField(
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

        for field_name in ['email', 'password1', 'password2', 'username']:
            self.fields[field_name].help_text = None

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is not unique")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is not unique")
        return email

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:

        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'picture', 'description', 'email')
        help_texts = {
            'password': None,
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter last name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, auth_forms.UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )
    email = forms.EmailField()
    picture = forms.ImageField()
    description = forms.CharField(
        widget=forms.Textarea,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            picture=self.cleaned_data['picture'],
            description=self.cleaned_data['description'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'picture', 'description',)

# class DeleteProfileForm(BootstrapFormMixin, forms.ModelForm):
#     def save(self, commit=True):
#         self.instance.delete()
#         vehicles = list(self.instance.vehicle_set.all())
#         VehiclePhoto.objects.filter(tagged_vehicle__in=vehicles).delete()
#         self.instance.delete()
#
#         return self.instance
#
#     class Meta:
#         model = Profile
#         fields = ()


class ProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('picture',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)