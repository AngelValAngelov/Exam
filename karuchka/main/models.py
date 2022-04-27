import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from karuchka.common.validators import MaxFileSizeInMbValidator, MinDateValidator

UserModel = get_user_model()


class Vehicle(models.Model):
    NEW = 'NEW'
    USED = 'USED'

    VEHICLE_TYPE = [(x, x) for x in (NEW, USED)]

    AUTOMATIC = 'AUTOMATIC'
    MANUAL = 'MANUAL'
    SEMI_AUTOMATIC = 'SEMI_AUTOMATIC'

    GEARING_TYPE = [(x, x) for x in (AUTOMATIC, MANUAL, SEMI_AUTOMATIC)]

    MANUFACTURER_MAX_LENGTH = 30
    MANUFACTURER_MIN_LENGTH = 1

    MODEL_MAX_LENGTH = 30
    MODEL_MIN_LENGTH = 1

    BODY_COLOR_MAX_LENGTH = 30
    BODY_COLOR_MIN_LENGTH = 1

    BODY_MAX_LENGTH = 30
    BODY_MIN_LENGTH = 1

    NUMBER_OF_DOORS_MIN_VALUE = 1

    NUMBER_OF_SEATS_MIN_VALUE = 1

    FUEL_MAX_LENGTH = 30
    FUEL_MIN_LENGTH = 1

    GEARS_MIN_VALUE = 1

    WEIGHT_MIN_VALUE = 1

    VEHICLE_POWER = 1

    VEHICLE_PRICE_MIN_VALUE = 1

    VEHICLE_KILOMETERS_MIN_VALUE = 0
    MIN_DATE = datetime.date(1920, 1, 1)
    VALIDATE_FILE_MAX_SIZE_IN_MB = 5

    manufacturer = models.CharField(
        max_length=MANUFACTURER_MAX_LENGTH,
        validators=(
            MinLengthValidator(MANUFACTURER_MIN_LENGTH),
        )
    )

    model = models.CharField(
        max_length=MODEL_MAX_LENGTH,
        validators=(
            MinLengthValidator(MODEL_MIN_LENGTH),
        )
    )

    body_color = models.CharField(
        max_length=BODY_COLOR_MAX_LENGTH,
        validators=(
            MinLengthValidator(BODY_COLOR_MIN_LENGTH),
        )
    )

    body = models.CharField(
        max_length=BODY_MAX_LENGTH,
        validators=(
            MinLengthValidator(BODY_MIN_LENGTH),
        )
    )

    number_of_doors = models.IntegerField(
        validators=(
            MinValueValidator(NUMBER_OF_DOORS_MIN_VALUE),
        )
    )

    number_of_seats = models.IntegerField(
        validators=(
            MinValueValidator(NUMBER_OF_SEATS_MIN_VALUE),
        )
    )

    fuel = models.CharField(
        max_length=FUEL_MAX_LENGTH,
        validators=(
            MinLengthValidator(FUEL_MIN_LENGTH),
        )
    )

    vehicle_type = models.CharField(
        max_length=max(len(x) for (x, _) in VEHICLE_TYPE),
        choices=VEHICLE_TYPE,
    )

    gearing_type = models.CharField(
        max_length=max(len(x) for (x, _) in GEARING_TYPE),
        choices=GEARING_TYPE,
    )

    gears = models.IntegerField(
        validators=(
            MinValueValidator(GEARS_MIN_VALUE),
        )
    )

    weight = models.IntegerField(
        validators=(
            MinValueValidator(WEIGHT_MIN_VALUE),
        )
    )

    vehicle_power = models.IntegerField(
        validators=(
            MinValueValidator(VEHICLE_POWER),
        )
    )

    manufacturer_date = models.DateField(
        validators=(
            MinDateValidator(MIN_DATE),
        )
    )

    vehicle_price = models.FloatField(
        validators=(
            MinValueValidator(VEHICLE_PRICE_MIN_VALUE),
        )
    )

    vehicle_kilometers = models.FloatField(
        validators=(
            MinValueValidator(VEHICLE_KILOMETERS_MIN_VALUE),
        )
    )

    photo = models.ImageField(
        validators=(
            MaxFileSizeInMbValidator(VALIDATE_FILE_MAX_SIZE_IN_MB),
        ),
    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )

    description = models.TextField()

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.manufacturer_date.year

    def __str__(self):
        return f'{self.manufacturer} {self.model}'



class Like(models.Model):
    LIKES = 0
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    likes = models.IntegerField(
        default=LIKES
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Dislike(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    likes = models.IntegerField(
        default=0
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

class Comment(models.Model):
    text = models.TextField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )