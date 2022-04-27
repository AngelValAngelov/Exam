from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from karuchka.accounts.managers import KaruchkaUserManager
from karuchka.common.validators import MaxFileSizeInMbValidator


class KaruchkaUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    email = models.EmailField()

    USERNAME_FIELD = 'username'

    objects = KaruchkaUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 1

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 1

    VALIDATE_FILE_MAX_SIZE_IN_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
    )

    email = models.EmailField(
        unique=True,
    )

    picture = models.ImageField(
        validators=(
            MaxFileSizeInMbValidator(VALIDATE_FILE_MAX_SIZE_IN_MB),
        ),
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        KaruchkaUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


from .signals import *
