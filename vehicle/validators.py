import re

from rest_framework.exceptions import ValidationError


class TitleValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'^[А-Я][а-я0-9.\- ]{1,19}$')
        tmp_val = dict(value).get(self.field)
        if not bool(reg.match(tmp_val)):
            raise ValidationError('Неверно указано наименование.')
        return value


class MinMileageValidator:

    def __call__(self, value):
        if value <= 100:
            raise ValidationError('Пробег не может быть меньше 100.')

        return value


class MaxYearValidator:

    def __call__(self, value):
        if value > 2026:
            raise ValidationError('Год не может быть больше настоящего.')

        return value


class CarMotoTogetherValidator:

    def __init__(self, car_field, moto_field):
        self.car_field = car_field
        self.moto_field = moto_field

    def __call__(self, value):
        car_value = dict(value).get(self.car_field)
        moto_value = dict(value).get(self.moto_field)

        if car_value and moto_value:
            raise ValidationError('Пробег не может быть одновременно указан и для машины, и для мотоцикла')

        elif not car_value and not moto_value:
            raise ValidationError('Пробег не может быть одновременно указан ни для машины, ни для мотоцикла')
        return value